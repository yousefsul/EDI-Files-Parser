import os

from parse_common.main_parser import MainParser


class Parse277CA(MainParser):
    def __init__(self, edi_file):
        super().__init__(edi_file)
        self.__count_st = 0
        self.__bht_list = []
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
        self.index_277CA = {
            '277ca_index': {
                'header_section': {
                    'file_name': os.path.basename(edi_file),
                    "date_created": {
                        "date": self.time,
                        "time": self.date
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
                self.__build_2000a_loop(param)
                self.__build_2000b_loop(param)
                self.__build_2000c_loop(param)
                self.__build_2000d_loop(param)
                self.__build_se_dict(param)
                break
        except IndexError:
            pass

    def __build_2000a_loop(self, param):
        param['2000A'] = {}
        self.extract_data()
        param['2000A'][self.segment] = {}
        self.build_data_element(param['2000A'][self.segment], 0)
        self.__build_2100a_loop(param['2000A'])

    def __build_2100a_loop(self, param):
        param['2100A'] = {}
        self.extract_data()
        param['2100A'][self.segment] = {}
        self.build_data_element(param['2100A'][self.segment], 0)
        self.__build_2200a_loop(param['2100A'])

    def __build_2200a_loop(self, param):
        param['2200A'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'HL':
                param['2200A'][self.segment] = {}
                self.build_data_element(param['2200A'][self.segment], i)
            else:
                break

    def __build_2000b_loop(self, param):
        param['2000B'] = {}
        self.extract_data()
        param['2000B'][self.segment] = {}
        self.build_data_element(param['2000B'][self.segment], 0)
        self.__build_2100b_loop(param['2000B'])

    def __build_2100b_loop(self, param):
        param['2100B'] = {}
        self.extract_data()
        param['2100B'][self.segment] = {}
        self.build_data_element(param['2100B'][self.segment], 0)
        self.__build_2200b_loop(param['2100B'])

    def __build_2200b_loop(self, param):
        param['2200B'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'HL':
                param['2200B'][self.segment] = {}
                self.build_data_element(param['2200B'][self.segment], i)
            else:
                break

    def __build_2000c_loop(self, param):
        param['2000C'] = {}
        self.extract_data()
        param['2000C'][self.segment] = {}
        self.build_data_element(param['2000C'][self.segment], 0)
        self.__build_2100c_loop(param['2000C'])

    def __build_2100c_loop(self, param):
        param['2100C'] = {}
        self.extract_data()
        param['2100C'][self.segment] = {}
        self.build_data_element(param['2100C'][self.segment], 0)
        self.__build_2200c_loop(param['2100C'])

    def __build_2200c_loop(self, param):
        param['2200C'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'HL':
                param['2200C'][self.segment] = {}
                self.build_data_element(param['2200C'][self.segment], i)
            else:
                break

    def __build_2000d_loop(self, param):
        param['2000D'] = {}
        self.extract_data()
        param['2000D'][self.segment] = {}
        self.build_data_element(param['2000D'][self.segment], 0)
        self.__build_2100d_loop(param['2000D'])

    def __build_2100d_loop(self, param):
        param['2100D'] = {}
        self.extract_data()
        param['2100D'][self.segment] = {}
        self.build_data_element(param['2100D'][self.segment], 0)
        self.__build_2200d_loop(param['2100D'])

    def __build_2200d_loop(self, param):
        param['2200D'] = {}
        for i in range(len(self.edi_file_info)):
            i = 0
            self.extract_data()
            if self.segment.split('-')[0] != 'SE':
                param['2200D'][self.segment] = {}
                self.build_data_element(param['2200D'][self.segment], i)
            else:
                break

    def extract_index_data(self):
        for data in self.edi_parsed:
            segment = data.split('-')[0]
            if segment == 'ISA':
                self.index_277CA['277ca_index'][segment] = self.edi_parsed.get(data)
            if segment == 'GS':
                self.index_277CA['277ca_index'][segment] = self.edi_parsed.get(data)
            if segment == 'ST':
                self.index_277CA['277ca_index'][segment] = {}
                self.index_277CA['277ca_index'][segment]['01'] = self.edi_parsed.get(data).get('01')
                self.index_277CA['277ca_index'][segment]['02'] = self.edi_parsed.get(data).get('02')
                self.index_277CA['277ca_index'][segment]['count_st'] = self.__count_st
                break
        self.index_277CA['277ca_index']['BHTs'] = self.__bht_list
        return self.index_277CA
