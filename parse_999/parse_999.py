import json
import os

from parse_common.main_parser import MainParser

loop_2000 = '2000'
loop_2100 = '2100'
loop_2110 = '2110'


class Parse999(MainParser):
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
        self.index_999 = {'999_index': {
            'header_section': {
                'file_name': os.path.basename(self.edi_file),
                "date_created": {
                    "date": self.time,
                    "time": self.date
                },
                "current_status": self.get_current_status(),
                "status_history": [self.get_current_status()],
            }
        }}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'AK1':
                self.bulid_main_dict()
                self.__bulid_ak9_dict(self.edi_parsed[self.segment])
            elif self.segment.split('-')[0] == 'AK2':
                self.bulid_main_dict()
                self.edi_parsed[self.segment]['loop_name'] = loop_2000
                self.__bulid_ak2_dict(self.edi_parsed[self.segment])
            else:
                self.bulid_main_dict()

    def __bulid_ak9_dict(self, param):
        for i in range(len(self.edi_file_info)):
            try:
                if self.edi_file_info[i].split('*')[0] == 'AK9':
                    self.data_element = self.edi_file_info[i].split('*')
                    self.index += 1
                    self.segment = self.data_element.pop(0) + '-' + str(self.index)
                    param[self.segment] = {}
                    self.count = 1
                    for self.data in self.data_element:
                        data_element_count = '{:02}'.format(self.count)
                        param[self.segment][data_element_count] = self.data
                        self.count += 1
                    self.pop_element(i)
                    break
            except IndexError:
                pass

    def __bulid_ak2_dict(self, param):
        for i in range(len(self.edi_file_info)):
            i = 0
            try:
                if self.edi_file_info[i].split('*')[0] == 'IK3':
                    self.extract_data()
                    param[self.segment] = {}
                    self.bulid_data_element(param[self.segment], 0)
                    param[self.segment]['loop_name'] = loop_2100
                    self.__bulid_ik3_dict(param[self.segment])

                if self.edi_file_info[i].split('*')[0] == 'IK5':
                    self.extract_data()
                    param[self.segment] = {}
                    self.bulid_data_element(param[self.segment], 0)
                    break
            except IndexError:
                pass

    def __bulid_ik3_dict(self, param):
        for i in range(len(self.edi_file_info)):
            i = 0
            try:
                if self.edi_file_info[i].split('*')[0] == 'CTX':
                    self.extract_data()
                    param[self.segment] = {}
                    self.bulid_data_element(param[self.segment], 0)

                elif self.edi_file_info[i].split('*')[0] == 'IK4':
                    self.extract_data()
                    param[self.segment] = {}
                    self.bulid_data_element(param[self.segment], 0)
                    param[self.segment]['loop_name'] = loop_2110
                    self.__bulid_ik4_dict(param[self.segment])
                else:
                    break
            except IndexError:
                pass

    def __bulid_ik4_dict(self, param):
        for i in range(len(self.edi_file_info)):
            i = 0
            try:
                if self.edi_file_info[i].split('*')[0] == 'CTX':
                    self.extract_data()
                    param[self.segment] = {}
                    self.bulid_data_element(param[self.segment], 0)
            except IndexError:
                pass

    def extract_index_data(self):
        for data in self.edi_parsed:
            segment = data.split('-')[0]
            if segment == 'ISA':
                self.index_999[segment] = {}
                self.index_999[segment]['05'] = self.edi_parsed[data]['05']
                self.index_999[segment]['06'] = self.edi_parsed[data]['06']
                self.index_999[segment]['07'] = self.edi_parsed[data]['07']
                self.index_999[segment]['08'] = self.edi_parsed[data]['08']
            if segment == 'GS':
                self.index_999[segment] = {}
                self.index_999[segment]['02'] = self.edi_parsed[data]['02']
                self.index_999[segment]['03'] = self.edi_parsed[data]['03']
                self.index_999[segment]['06'] = self.edi_parsed[data]['06']

            if segment == 'AK1':
                self.index_999[segment] = {}
                self.index_999[segment]['01'] = self.edi_parsed[data]['01']
                self.index_999[segment]['02'] = self.edi_parsed[data]['02']
                self.index_999[segment]['03'] = self.edi_parsed[data]['03']

            if segment == 'AK2':
                self.index_999[segment] = {}
                self.index_999[segment]['01'] = self.edi_parsed[data]['01']
                self.index_999[segment]['02'] = self.edi_parsed[data]['02']
                self.index_999[segment]['03'] = self.edi_parsed[data]['03']
        return self.index_999
