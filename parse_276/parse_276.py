import json
import os

from parse_common.main_parser import MainParser


class Parse276(MainParser):
    def __init__(self, edi_file):
        super().__init__(edi_file)
        self.edi_parsed = {
            'header_section': {
                'file_name': os.path.basename(self.edi_file),
                "date_created": {
                    "date": self.time,
                    "time": self.date
                },
                "current_status": self.get_current_status(),
                "status_history": [self.get_current_status()],
            }}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'ST':
                self.bulid_main_dict()
                self.edi_parsed[self.segment]['status'] = 'pending'
                self.__bulid_st_dict(self.edi_parsed[self.segment])
            else:
                self.bulid_main_dict()

    def __bulid_st_dict(self, param):
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'BHT':
                param[self.segment] = {}
                self.bulid_data_element(param[self.segment], i)
            self.__bulid_2000a_loop(param)
            self.__bulid_2000b_loop(param)
            self.__bulid_2000c_loop(param)
            self.__bulid_2000d_loop(param)
            self.__bulid_se_dict(param)
            break

    def __bulid_se_dict(self, param):
        for i in range(len(self.edi_file_info)):
            try:
                self.extract_data()
                if self.segment.split('-')[0] == 'SE':
                    param[self.segment] = {}
                    for self.data in self.data_element:
                        data_element_count = '{:02}'.format(self.count)
                        param[self.segment][data_element_count] = self.data
                        self.count += 1
                    self.pop_element(i)
                    break
            except IndexError:
                pass

    def __bulid_2000a_loop(self, param):
        param['2000A'] = {}
        self.extract_data()
        param['2000A'][self.segment] = {}
        self.bulid_data_element(param['2000A'][self.segment], 0)
        self.__bulid_2100a_loop(param['2000A'])

    def __bulid_2100a_loop(self, param):
        param['2100A'] = {}
        self.extract_data()
        param['2100A'][self.segment] = {}
        self.bulid_data_element(param['2100A'][self.segment], 0)

    def __bulid_2000b_loop(self, param):
        param['2000B'] = {}
        self.extract_data()
        param['2000B'][self.segment] = {}
        self.bulid_data_element(param['2000B'][self.segment], 0)
        self.__bulid_2100b_loop(param['2000B'])

    def __bulid_2100b_loop(self, param):
        param['2100B'] = {}
        self.extract_data()
        param['2100B'][self.segment] = {}
        self.bulid_data_element(param['2100B'][self.segment], 0)

    def __bulid_2000c_loop(self, param):
        param['2000C'] = {}
        self.extract_data()
        param['2000C'][self.segment] = {}
        self.bulid_data_element(param['2000C'][self.segment], 0)
        self.__bulid_2100c_loop(param['2000C'])

    def __bulid_2100c_loop(self, param):
        param['2100C'] = {}
        self.extract_data()
        param['2100C'][self.segment] = {}
        self.bulid_data_element(param['2100C'][self.segment], 0)

    def __bulid_2000d_loop(self, param):
        param['2000D'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'NM1':
                param['2000D'][self.segment] = {}
                self.bulid_data_element(param['2000D'][self.segment], i)
            else:
                self.__bulid_2100d_loop(param['2000D'])
                break

    def __bulid_2100d_loop(self, param):
        param['2100D'] = {}
        self.extract_data()
        param['2100D'][self.segment] = {}
        self.bulid_data_element(param['2100D'][self.segment], 0)
        self.__bulid_2200d_loop(param['2100D'])

    def __bulid_2200d_loop(self, param):
        param['2200D'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'SE':
                param['2200D'][self.segment] = {}
                self.bulid_data_element(param['2200D'][self.segment], i)
            else:
                break

    # count st in 276_files file


    # Add your logic for creating index for 276_files
    def extract_index_data(self):
        pass