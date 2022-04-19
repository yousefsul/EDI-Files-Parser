import inspect
from application.ConnectMongoDB import ConnectMongoDB


class Specification835:
    def __init__(self, loop, code, segment, cursor):
        self.__loop = loop
        self.__code = code
        self.__segment = segment.split('-')[0]
        self.__cursor = cursor
        self.__cursor.rewind()
        self.__id = str()
        if self.__loop == "":
            self.__loop = 'header'
        else:
            self.__loop = loop
        self.__set_id()

    #     self.__isa = {
    #         'ISA':
    #             {
    #                 'header': {
    #                     'Implementation Name': 'Authorization Qualifier',
    #                     'id': '1'
    #                 }
    #             }
    #     }
    #     self.__gs = {
    #         'GS':
    #             {
    #                 'header': {
    #                     'Implementation Name': 'Functional Identifier Code',
    #                     'id': '17'
    #                 }
    #             }
    #     }
    #     self.__st = {
    #         'ST': {
    #             'header': {
    #                 'Implementation Name': 'Transaction Set Identifier Code',
    #                 'id': '25'
    #             }
    #         }
    #     }
    #     self.__bpr = {
    #         'BPR': {
    #             'header': {
    #                 'Implementation Name': 'Transaction Handling Code',
    #                 'id': '28'
    #             }
    #         }
    #     }
    #     self.__trn = {
    #         'TRN': {
    #             'header': {
    #                 'Implementation Name': 'Trace Type Code',
    #                 'id': '49'
    #             }
    #         }
    #     }
    #     self.__cur = {
    #         'CUR': {
    #             'header': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '53'
    #             }
    #         }
    #     }
    #     self.__ref01 = {
    #         'header': {
    #             'EV': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '74'
    #             },
    #             'F2': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '78'
    #             },
    #         },
    #         '1000A': {
    #             '2U': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '103'
    #             },
    #             'EO': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '103'
    #             },
    #             'HI': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '103'
    #             },
    #             'NF': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '103'
    #             },
    #         },
    #         '1000B': {
    #             '0B': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '149'
    #             },
    #             'D3': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '149'
    #             },
    #             'PQ': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '149'
    #             },
    #             'TJ': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '149'
    #             },
    #         },
    #         '2100': {
    #             '1L': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '1W': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '28': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '6P': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '9A': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '9C': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'BB': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'CE': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'EA': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'F8': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'G1': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'G3': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'IG': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             'SY': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '352'
    #             },
    #             '0B': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1A': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1B': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1C': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1D': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1G': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1H': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             '1J': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             'D3': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             'G2': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #             'LU': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '356'
    #             },
    #         },
    #         '2110': {
    #             '1S': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'APC': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'BB': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'E9': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'G1': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'G3': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             'LU': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '426'
    #             },
    #             '6R': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '430'
    #             },
    #             '0B': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1A': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1B': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1C': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1D': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1G': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1H': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             '1J': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             'D3': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             'G2': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             'HPI': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             'SY': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #             'TJ': {
    #                 'Implementation Name': 'Reference Identification Qualifier',
    #                 'id': '434'
    #             },
    #         },
    #     }
    #     self.__dtm01 = {
    #         'header': {
    #             '405': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '82'
    #             }
    #         },
    #         '2000': {
    #             '232': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '360'
    #             },
    #             '233': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '360'
    #             },
    #             '036': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '366'
    #             },
    #             '050': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '372'
    #             },
    #         },
    #         '2110': {
    #             '150': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '401'
    #             },
    #             '151': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '401'
    #             },
    #             '472': {
    #                 'Implementation Name': 'Date/ Time Qualifier',
    #                 'id': '401'
    #             },
    #         },
    #     }
    #     self.__n101 = {
    #         '1000A': {
    #             'PR': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '88'
    #             },
    #         },
    #         '1000B': {
    #             'PE': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '134'
    #             },
    #         },
    #
    #     }
    #     self.__n301 = {
    #         '1000A': {
    #             'Implementation Name': 'Payer Address Line',
    #             'id': '94'
    #         },
    #         '1000B': {
    #             'Implementation Name': 'Payer Address Line',
    #             'id': '140'
    #         }
    #     }
    #     self.__n401 = {
    #         '1000A': {
    #             'Implementation Name': 'Payer City Name',
    #             'id': '96'
    #         },
    #         '1000B': {
    #             'Implementation Name': 'Payee City Name',
    #             'id': '142'
    #         }
    #     }
    #     self.__per01 = {
    #         '1000A': {
    #             'CX': {
    #                 'Implementation Name': 'Contact Function Code',
    #                 'id': '107'
    #             },
    #             'BL': {
    #                 'Implementation Name': 'Contact Function Code',
    #                 'id': '116'
    #             },
    #             'IC': {
    #                 'Implementation Name': 'Contact Function Code',
    #                 'id': '125'
    #             },
    #         },
    #         '2000': {
    #             'CX': {
    #                 'Implementation Name': 'Contact Function Code',
    #                 'id': '378'
    #             },
    #         }
    #     }
    #     self.__rdm01 = {
    #         '1000B': {
    #             'BM': {
    #                 'Implementation Name': 'Report Transmission Code',
    #                 'id': '153'
    #             },
    #             'EM': {
    #                 'Implementation Name': 'Report Transmission Code',
    #                 'id': '153'
    #             },
    #             'FT': {
    #                 'Implementation Name': 'Report Transmission Code',
    #                 'id': '153'
    #             },
    #             'OL': {
    #                 'Implementation Name': 'Report Transmission Code',
    #                 'id': '153'
    #             },
    #         }
    #
    #     }
    #     self.__lx = {
    #         '2000': {
    #             'Implementation Name': 'Assigned Number',
    #             'id': '158'
    #         }
    #     }
    #     self.__ts3 = {
    #         '2000': {
    #             'Implementation Name': 'Provider Identifier',
    #             'id': '159'
    #         }
    #
    #     }
    #     self.__ts2 = {
    #         '2000': {
    #             'Implementation Name': 'Total DRG Amount',
    #             'id': '183'
    #         }
    #
    #     }
    #     self.__clp = {
    #         '2100': {
    #             'Implementation Name': 'Patient Control Number',
    #             'id': '202'
    #         }
    #
    #     }
    #     self.__cas = {
    #         '2100': {
    #             'CO': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '216'
    #             },
    #             'OA': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '216'
    #             },
    #             'PI': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '216'
    #             },
    #             'PR': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '216'
    #             },
    #         },
    #         '2110': {
    #             'CO': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '407'
    #             },
    #             'OA': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '407'
    #             },
    #             'PI': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '407'
    #             },
    #             'PR': {
    #                 'Implementation Name': 'Claim Adjustment Group Code',
    #                 'id': '407'
    #             },
    #         }
    #     }
    #     self.__nm101 = {
    #         '2100': {
    #             'QC': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '235'
    #             },
    #             'IL': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '247'
    #             },
    #             '74': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '259'
    #             },
    #             '82': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '271'
    #             },
    #             'TT': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '283'
    #             },
    #             'PR': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '295'
    #             },
    #             'GB': {
    #                 'Implementation Name': 'Entity Identifier Code',
    #                 'id': '307'
    #             },
    #         },
    #     }
    #     self.__mia = {
    #         '2100': {
    #             'Implementation Name': 'Covered Days or Visits Count',
    #             'id': '319'
    #         },
    #     }
    #     self.__moa = {
    #         '2100': {
    #             'Implementation Name': 'Covered Days or Visits Count',
    #             'id': '343'
    #         },
    #     }
    #     self.__amt = {
    #         '2000': {
    #             'AU': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'D8': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'DY': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'F5': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'I': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'NL': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'T': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'T2': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'ZK': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'ZL': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'ZM': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'ZN': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #             'ZO': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '387'
    #             },
    #         },
    #         '2110': {
    #             'B6': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'KH': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'T': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'T2': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'ZK': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'ZL': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'ZM': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'ZN': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #             'ZO': {
    #                 'Implementation Name': 'Amount Qualifier Code',
    #                 'id': '442'
    #             },
    #         }
    #     }
    #     self.__qty = {
    #         '2000': {
    #             'CA': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'CD': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'LA': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'LE': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'NE': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'NR': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'OU': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'PS': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'VS': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'ZK': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'ZL': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'ZM': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'ZN': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #             'ZO': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '390'
    #             },
    #         },
    #         '2110': {
    #             'ZK': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '445'
    #             },
    #             'ZL': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '445'
    #             },
    #             'ZM': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '445'
    #             },
    #             'ZN': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '445'
    #             },
    #             'ZO': {
    #                 'Implementation Name': 'Quantity Qualifier',
    #                 'id': '445'
    #             },
    #
    #         }
    #     }
    #     self.__svc = {
    #         '2110': {
    #             'Implementation Name': 'COMPOSITE MEDICAL PROCEDURE IDENTIFIER',
    #             'id': '394'
    #         }
    #     }
    #     self.__lq = {
    #         '2110': {
    #             'HE': {
    #                 'Implementation Name': 'Code List Qualifier Code',
    #                 'id': '449'
    #             },
    #             'RX': {
    #                 'Implementation Name': 'Code List Qualifier Code',
    #                 'id': '449'
    #             },
    #         }
    #     }
    #     self.__plb = {
    #         '2110': {
    #             'Implementation Name': 'Provider Identifier',
    #             'id': '451'
    #         }
    #     }
    #     self.__se = {
    #         'SE': {
    #             'header': {
    #                 'Implementation Name': 'Number of Included Segments',
    #                 'id': '465'
    #             }
    #         }
    #
    #     }
    #     self.__ge = {
    #         'GE': {
    #             'header': {
    #                 'Implementation Name': 'Number of Transaction Sets Included',
    #                 'id': '467'
    #             }
    #         }
    #
    #     }
    #     self.__iea = {
    #         'IEA':
    #             {
    #                 'header': {
    #                     'Implementation Name': 'Number of Included Functional Groups',
    #                     'id': '469'
    #                 }
    #             }
    #     }
    #
    # def __check_isa(self):
    #     if self.__segment in self.__isa.keys():
    #         if self.__loop in self.__isa.get(self.__segment):
    #             return self.__isa.get(self.__segment).get(self.__loop)
    #
    # def __check_gs(self):
    #     if self.__segment in self.__gs.keys():
    #         if self.__loop in self.__gs.get(self.__segment):
    #             return self.__gs.get(self.__segment).get(self.__loop)
    #
    # def __check_st(self):
    #     if self.__segment in self.__st.keys():
    #         if self.__loop in self.__st.get(self.__segment):
    #             return self.__st.get(self.__segment).get(self.__loop)
    #
    # def __check_bpr(self):
    #     if self.__segment in self.__bpr.keys():
    #         if self.__loop in self.__bpr.get(self.__segment):
    #             return self.__bpr.get(self.__segment).get(self.__loop)
    #
    # def __check_trn(self):
    #     if self.__segment in self.__trn.keys():
    #         if self.__loop in self.__trn.get(self.__segment):
    #             return self.__trn.get(self.__segment).get(self.__loop)
    #
    # def __check_cur(self):
    #     if self.__segment in self.__cur.keys():
    #         if self.__loop in self.__cur.get(self.__segment):
    #             return self.__cur.get(self.__segment).get(self.__loop)
    #
    # def __check_ref(self):
    #     if self.__loop in self.__ref01.keys():
    #         if self.__code in self.__ref01.get(self.__loop):
    #             return self.__ref01.get(self.__loop).get(self.__code)
    #
    # def __check_dtm(self):
    #     if self.__loop in self.__dtm01.keys():
    #         if self.__code in self.__dtm01.get(self.__loop):
    #             return self.__dtm01.get(self.__loop).get(self.__code)
    #
    # def __check_n1(self):
    #     if self.__loop in self.__n101.keys():
    #         if self.__code in self.__n101.get(self.__loop):
    #             return self.__n101.get(self.__loop).get(self.__code)
    #
    # def __check_n3(self):
    #     if self.__loop in self.__n301.keys():
    #         return self.__n301.get(self.__loop)
    #
    # def __check_n4(self):
    #     if self.__loop in self.__n401.keys():
    #         return self.__n401.get(self.__loop)
    #
    # def __check_per(self):
    #     if self.__loop in self.__per01.keys():
    #         if self.__code in self.__per01.get(self.__loop):
    #             return self.__per01.get(self.__loop).get(self.__code)
    #
    # def __check_rdm(self):
    #     if self.__loop in self.__rdm01.keys():
    #         if self.__code in self.__rdm01.get(self.__loop):
    #             return self.__rdm01.get(self.__loop).get(self.__code)
    #
    # def __check_lx(self):
    #     if self.__loop in self.__lx.keys():
    #         return self.__lx.get(self.__loop)
    #
    # def __check_ts3(self):
    #     if self.__loop in self.__ts3.keys():
    #         return self.__ts3.get(self.__loop)
    #
    # def __check_ts2(self):
    #     if self.__loop in self.__ts2.keys():
    #         return self.__ts2.get(self.__loop)
    #
    # def __check_clp(self):
    #     if self.__loop in self.__clp.keys():
    #         return self.__clp.get(self.__loop)
    #
    # def __check_cas(self):
    #     if self.__loop in self.__cas.keys():
    #         if self.__code in self.__cas.get(self.__loop):
    #             return self.__cas.get(self.__loop).get(self.__code)
    #
    # def __check_nm101(self):
    #     if self.__loop in self.__nm101.keys():
    #         if self.__code in self.__nm101.get(self.__loop):
    #             return self.__nm101.get(self.__loop).get(self.__code)
    #
    # def __check_mia(self):
    #     if self.__loop in self.__mia.keys():
    #         return self.__mia.get(self.__loop)
    #
    # def __check_moa(self):
    #     if self.__loop in self.__moa.keys():
    #         return self.__moa.get(self.__loop)
    #
    # def __check_amt(self):
    #     if self.__loop in self.__amt.keys():
    #         if self.__code in self.__amt.get(self.__loop):
    #             return self.__amt.get(self.__loop).get(self.__code)
    #
    # def __check_qty(self):
    #     if self.__loop in self.__qty.keys():
    #         if self.__code in self.__qty.get(self.__loop):
    #             return self.__qty.get(self.__loop).get(self.__code)
    #
    # def __check_svc(self):
    #     if self.__loop in self.__svc.keys():
    #         return self.__svc.get(self.__loop)
    #
    # def __check_lq(self):
    #     if self.__loop in self.__lq.keys():
    #         if self.__code in self.__lq.get(self.__loop):
    #             return self.__lq.get(self.__loop).get(self.__code)
    #
    # def __check_plb(self):
    #     if self.__loop in self.__plb.keys():
    #         return self.__plb.get(self.__loop)
    #
    # def __check_se(self):
    #     if self.__segment in self.__se.keys():
    #         if self.__loop in self.__se.get(self.__segment):
    #             return self.__se.get(self.__segment).get(self.__loop)
    #
    # def __check_ge(self):
    #     if self.__segment in self.__ge.keys():
    #         if self.__loop in self.__ge.get(self.__segment):
    #             return self.__ge.get(self.__segment).get(self.__loop)
    #
    # def __check_iea(self):
    #     if self.__segment in self.__iea.keys():
    #         if self.__loop in self.__iea.get(self.__segment):
    #             return self.__iea.get(self.__segment).get(self.__loop)
    #
    # def set_loop(self, loop):
    #     if self.__loop == "":
    #         self.__loop = 'header'
    #     else:
    #         self.__loop = loop
    #
    # def set_code(self, code):
    #     self.__code = code
    def __set_id(self):
        try:
            for config in self.__cursor:
                if self.__segment in config.keys():
                    if self.__loop in config.get(self.__segment).keys():
                        self.__id = config.get(self.__segment).get(self.__loop).get("id")
                        if self.__id is None:
                            self.__id = config.get(self.__segment).get(self.__loop).get(self.__code).get("id")
                        break
        except Exception as e:
            pass
        # try:
        #     for config in self.__cursor:
        #         if self.__loop == "header":
        #             if self.__segment in config.keys():
        #                 if self.__loop in config.get(self.__segment).keys():
        #                     self.__id = config.get(self.__segment).get(self.__loop).get("id")
        #                     if self.__id is None:
        #                         self.__id = config.get(self.__segment).get(self.__loop).get(self.__code).get("id")
        #                     break
        #         else:
        #             if self.__segment in config.keys():
        #                 if self.__loop in config.get(self.__segment).keys():
        #                     self.__id = config.get(self.__segment).get(self.__loop).get(self.__code).get("id")
        #                     break
        # except Exception as e:
        #     pass

    def get_id(self):
        return self.__id
