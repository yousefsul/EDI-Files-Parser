import os

import shortuuid

from parse_common.main_parser import MainParser


class Parse837(MainParser):
    def __init__(self, edi_file):
        super().__init__(edi_file)
        self.__count_st = 0
        self.__bht_list = []
        self.__id = self.__generate_id()
        self.edi_parsed = {
            'header_section': {
                'trans_src_id': self.__id,
                'file_name': os.path.basename(self.edi_file),
                "date_created": {
                    "time": self.time,
                    "date": self.date
                },
                "current_status": self.get_current_status(),
                "status_history": [self.get_current_status()],
            }}
        self.index_837 = {
            '837_index': {
                'header_section': {
                    'trans_src_id': self.__id,
                    'file_name': os.path.basename(edi_file),
                    "date_created": {
                        "time": self.time,
                        "date": self.date
                    },
                    "current_status": self.get_current_status(),
                    "status_history": [self.get_current_status()],
                }
            }
        }
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'ST':
                self.__count_st += 1
                self.build_main_dict()
                self.edi_parsed[self.segment]['status'] = 'pending'
                self.__build_st_dict(self.edi_parsed[self.segment])
            else:
                self.build_main_dict()

    def __build_se_dict(self, param):
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

    def __build_st_dict(self, param):
        try:
            for i in range(len(self.edi_file_info)):
                i = 0
                self.extract_data()
                if self.segment.split('-')[0] == 'BHT':
                    param[self.segment] = {}
                    self.__bht_list.append(self.data_element[2])
                    self.build_data_element(param[self.segment], i)
                self.__build_1000a_loop(param)
                self.__build_1000b_loop(param)
                self.__build_2000a_loop(param)
                self.__build_2000b_loop(param)
                self.__build_2300_loop(param)
                self.__build_se_dict(param)
                break
        except IndexError:
            pass

    def __build_1000a_loop(self, param):
        param['1000A'] = {}
        self.extract_data()
        param['1000A'][self.segment] = {}
        self.build_data_element(param['1000A'][self.segment], 0)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'PER':
                param['1000A'][self.segment] = {}
                self.build_data_element(param['1000A'][self.segment], i)
            else:
                break

    def __build_1000b_loop(self, param):
        param['1000B'] = {}
        self.extract_data()
        param['1000B'][self.segment] = {}
        self.build_data_element(param['1000B'][self.segment], 0)

    def __build_2000a_loop(self, param):
        param['2000A'] = {}
        self.extract_data()
        param['2000A'][self.segment] = {}
        self.build_data_element(param['2000A'][self.segment], 0)
        self.__build_2010aa_loop(param['2000A'])

    def __build_2010aa_loop(self, param):
        param['2010AA'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'HL':
                param['2010AA'][self.segment] = {}
                self.build_data_element(param['2010AA'][self.segment], i)
            else:
                break

    def __build_2000b_loop(self, param):
        param['2000B'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'NM1':
                param['2000B'][self.segment] = {}
                self.build_data_element(param['2000B'][self.segment], i)
            else:
                self.__build_2010ba_loop(param['2000B'])
                self.__build_2010bb_loop(param['2000B'])
                break

    def __build_2010ba_loop(self, param):
        param['2010BA'] = {}
        self.extract_data()
        param['2010BA'][self.segment] = {}
        self.build_data_element(param['2010BA'][self.segment], 0)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'NM1':
                param['2010BA'][self.segment] = {}
                self.build_data_element(param['2010BA'][self.segment], i)
            else:
                break

    def __build_2010bb_loop(self, param):
        param['2010BB'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'CLM':
                param['2010BB'][self.segment] = {}
                self.build_data_element(param['2010BB'][self.segment], i)
            else:
                break

    def __build_2300_loop(self, param):
        param['2300'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'NM1':
                param['2300'][self.segment] = {}
                self.build_data_element(param['2300'][self.segment], i)
            else:
                self.__build_2310b_loop(param['2300'])
                self.__build_2310c_loop(param['2300'])
                self.__build_2400_loop(param['2300'])
                break

    def __build_2310b_loop(self, param):
        param['2310B'] = {}
        self.extract_data()
        param['2310B'][self.segment] = {}
        self.build_data_element(param['2310B'][self.segment], 0)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'NM1':
                param['2310B'][self.segment] = {}
                self.build_data_element(param['2310B'][self.segment], i)
            else:
                break

    def __build_2310c_loop(self, param):
        param['2310C'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'LX':
                param['2310C'][self.segment] = {}
                self.build_data_element(param['2310C'][self.segment], i)
            else:
                break

    def __build_2400_loop(self, param):
        param['2400'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'SE':
                param['2400'][self.segment] = {}
                self.build_data_element(param['2400'][self.segment], i)
            else:
                break

    def extract_index_data(self):
        for data in self.edi_parsed:
            segment = data.split('-')[0]
            if segment == 'ISA':
                self.index_837['837_index'][segment] = self.edi_parsed.get(data)
            if segment == 'GS':
                self.index_837['837_index'][segment] = self.edi_parsed.get(data)
            if segment == 'ST':
                self.index_837['837_index'][segment] = {}
                self.index_837['837_index'][segment]['01'] = self.edi_parsed.get(data).get('01')
                self.index_837['837_index'][segment]['02'] = self.edi_parsed.get(data).get('02')
                self.index_837['837_index'][segment]['count_st'] = self.__count_st
                break
        self.index_837['837_index']['BHTs'] = self.__bht_list
        return self.index_837

    def __generate_id(self):
        return int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))
