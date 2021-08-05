import datetime


class MainParser:
    def __init__(self, edi_file):
        self.edi_file = edi_file
        self.count = 1
        self.index = 0
        self.data_element, self.data, self.segment = None, None, None
        self.time = datetime.datetime.now().time().strftime("%H:%M:%S")
        self.date = datetime.datetime.now().date().strftime("%Y%m%d")
        self.edi_parsed = {}
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

    def bulid_main_dict(self):
        self.edi_parsed[self.segment] = {}
        self.bulid_data_element(self.edi_parsed[self.segment], 0)

    def bulid_data_element(self, param, index):
        self.count = 1
        for self.data in self.data_element:
            data_element_count = '{:02}'.format(self.count)
            param[data_element_count] = self.data
            self.count += 1
        self.pop_element(index)

    def pop_element(self, index):
        if self.edi_file_info:
            self.edi_file_info.pop(index)

    def extract_index_data(self):
        pass
    # ISA GS GE IEA
