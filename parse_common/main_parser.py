import datetime
import inspect

from application.ConnectMongoDB import ConnectMongoDB
from bson import ObjectId
from parse_835.specification835 import Specification835
from application.ConnectMongoDB import ConnectMongoDB


class MainParser:
    def __init__(self, edi_file):
        self.edi_file = edi_file
        self.count = 1
        self.index = 0
        self.data_element, self.data, self.segment = None, None, None
        self.time = datetime.datetime.now().time().strftime("%H:%M:%S")
        self.date = datetime.datetime.now().date().strftime("%Y%m%d")
        self.edi_parsed = {}
        self.__connection = ConnectMongoDB('devDB')
        self.__connection.connect_to_collection('parserConfig')
        self.__parser_config = self.__connection.find_from_collection()
        with open(self.edi_file, 'r') as edi:
            self.edi_file_info = edi.read().strip('~').split('~')

    def get_current_status(self):
        current_status = {
            "status": "new",
            "date": {
                "date": datetime.datetime.now().date().strftime("%Y%m%d"),
                "time": datetime.datetime.now().time().strftime("%H:%M:%S")
            }
        }
        return current_status

    def extract_data(self):
        try:
            self.data_element = self.edi_file_info[0].split('*')
            self.index += 1
            self.segment = self.get_segment() + '-' + str(self.index)
        except IndexError:
            pass

    def get_segment(self):
        return self.data_element.pop(0)

    def build_main_dict(self, call_specification=False):
        self.edi_parsed[self.segment] = {}
        self.build_data_element(self.edi_parsed[self.segment], 0, call_specification=call_specification)

    def build_data_element(self, param, index, loop='', call_specification=False):
        if not call_specification:
            for self.data in self.data_element:
                data_element_count = '{:02}'.format(self.count)
                param[data_element_count] = self.data
                self.count += 1
            self.pop_element(index)
        else:
            self.__specification835_case(param, index, loop)

    def pop_element(self, index):
        if self.edi_file_info:
            self.edi_file_info.pop(index)

    def extract_index_data(self):
        pass

    def __specification835_case(self, param, index, loop):
        self.count = 1
        self.__res_specification_id = None
        self.__res_specification = None
        for self.data in self.data_element:
            data_element_count = '{:02}'.format(self.count)
            if self.count == 1:
                self.__specification = Specification835(loop, self.data, self.segment, self.__parser_config)
                self.__res_specification_id = (self.__specification.get_id())
                # self.__attrs = (getattr(self.__specification, name) for name in dir(self.__specification))
                # self.__methods = filter(inspect.ismethod, self.__attrs)
                # for self.__method in self.__methods:
                #     try:
                #         self.__res_specification = self.__method()
                #         if self.__res_specification is None:
                #             pass
                #         else:
                #             self.__res_specification_id = int(self.__res_specification.get('id'))
                #             break
                #     except TypeError:
                #         pass
            param[str(self.__res_specification_id) + '_' + data_element_count] = self.data
            self.count += 1
            if self.__res_specification_id:
                self.__res_specification_id = int(self.__res_specification_id) + 1
        self.pop_element(index)
