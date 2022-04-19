import json
import os

import shortuuid

from parse_common.main_parser import MainParser
from db_connection.connectMongoDB import ConnectMongoDB

loop_2110 = '2110'
loop_2100 = '2100'
loop_2000 = '2000'
loop1000B = '1000B'
loop_1000A = '1000A'


class Parse835(MainParser):
    def __init__(self, edi_file):
        super().__init__(edi_file)
        self.__count_st = 0
        self.__loop_count = 0
        self.__id = self.__generate_id()
        self.__connection = ConnectMongoDB()
        self.__connection.connect_edi_collection('paymentsColl')
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
        self.index_835 = {
            '835_index': {
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
                self.build_main_dict(True)
                self.__build_st_dict(self.edi_parsed[self.segment])
                self.__connection.insert_edi_collection(self.bpr)
            else:
                self.build_main_dict(True)

    def __build_se_dict(self, param):
        for i in range(len(self.edi_file_info)):
            try:
                self.extract_data()
                if self.segment.split('-')[0] == 'SE':
                    param[self.segment] = {}
                    self.build_data_element(param[self.segment], i, '', True)
                    # for self.data in self.data_element:
                    #     data_element_count = '{:02}'.format(self.count)
                    #     param[self.segment][data_element_count] = self.data
                    #     self.count += 1
                    # self.pop_element(i)
                    break
            except IndexError:
                pass

    def __build_st_dict(self, param):
        try:
            for i in range(len(self.edi_file_info)):
                i = 0
                self.extract_data()
                if self.segment.split('-')[0] == 'BPR':
                    while self.segment.split('-')[0] != 'N1':
                        self.extract_data()
                        if self.segment.split('-')[0] == 'N1':
                            break
                        else:
                            param[self.segment] = {}
                            self.build_data_element(param[self.segment], i, '', True)
                            self.__is_bpr(param, self.__generate_id())
                            self.__is_trn(param)
                self.__build_1000a_loop(param)
                self.__build_1000b_loop(param)
                while True:
                    self.__increment_loop_count()
                    self.__build_2000_loop(param)
                    if self.segment.split('-')[0] == "SE":
                        break
                self.__build_se_dict(param)
                break
        except IndexError:
            pass

    def __build_1000a_loop(self, param):
        param[loop_1000A] = {}
        self.extract_data()
        param[loop_1000A][self.segment] = {}
        self.build_data_element(param[loop_1000A][self.segment], 0, loop_1000A, True)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'N1':
                param[loop_1000A][self.segment] = {}
                self.build_data_element(param[loop_1000A][self.segment], i, loop_1000A, True)
            else:
                break

    def __build_1000b_loop(self, param):
        param[loop1000B] = {}
        self.extract_data()
        param[loop1000B][self.segment] = {}
        self.build_data_element(param[loop1000B][self.segment], 0, loop1000B, True)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'LX':
                param[loop1000B][self.segment] = {}
                self.build_data_element(param[loop1000B][self.segment], i, loop1000B, True)
            else:
                break

    def __build_2000_loop(self, param):
        self.__loop_name = loop_2000 + '-' + str(self.__loop_count)
        param[self.__loop_name] = {}
        self.extract_data()
        param[self.__loop_name][self.segment] = {}
        self.build_data_element(param[self.__loop_name][self.segment], 0, loop_2000, True)
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'CLP':
                param[self.__loop_name][self.segment] = {}
                self.build_data_element(param[self.__loop_name][self.segment], i, loop_2000, True)
            else:
                self.__build_2100_loop(param[self.__loop_name])
                break

    def __build_2100_loop(self, param):
        param[loop_2100] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'SVC':
                param[loop_2100][self.segment] = {}
                self.build_data_element(param[loop_2100][self.segment], i, loop_2100, True)
            else:
                self.__build_2110_loop(param[loop_2100])
                break

    def __build_2110_loop(self, param):
        param[loop_2110] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] == 'SE':
                break
            elif self.segment.split('-')[0] == 'LX':
                break
            else:
                param[loop_2110][self.segment] = {}
                self.build_data_element(param[loop_2110][self.segment], i, loop_2110, True)

    def __generate_id(self):
        return int(shortuuid.ShortUUID(alphabet="0123456789").random(length=10))

    def __is_bpr(self, param, bpr_id):
        if self.segment.split('-')[0] == 'BPR':
            self.bpr = {
                'header_section': {
                    'bpr_id': bpr_id,
                    'file_name': os.path.basename(self.edi_file),
                    "date_created": {
                        "time": self.time,
                        "date": self.date
                    },
                    "current_status": self.get_current_status(),
                    "status_history": [self.get_current_status()],
                }
            }
            self.__bpr_tmp = {
                "BPR": param[self.segment]
            }
            self.bpr.update(self.__bpr_tmp)
            param[self.segment].update({"bpr_id": bpr_id})

    def __is_trn(self, param):
        for i in range(len(self.edi_file_info)):
            if self.segment.split('-')[0] == 'TRN':
                self.__trn_tmp = {
                    "TRN": param[self.segment]
                }
                self.bpr.update(self.__trn_tmp)
            else:
                continue

    def __increment_loop_count(self):
        self.__loop_count += 1
