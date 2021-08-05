import glob
import shutil

from parse_276.parse_276 import Parse276
from parse_277CA.parse_277ca import Parse277CA
from parse_837.parse_837 import Parse837
from parse_999.parse_999 import Parse999

if __name__ == '__main__':
    edi_files = glob.glob('edi_files/*.*')
    for edi_file in edi_files:

        if edi_file.split('.')[-1] == '999':
            parse999 = Parse999(edi_file)
            print(parse999.edi_parsed)
            print()
            print(parse999.extract_index_data())
            shutil.move(edi_file, 'processed_edi_files/999_files/')

        if edi_file.split('.')[-1] == '837':
            parse837 = Parse837(edi_file)
            print(parse837.edi_parsed)
            print()
            print(parse837.extract_index_data())
            shutil.move(edi_file, 'processed_edi_files/837_files/')

        if edi_file.split('.')[-1] == '276':
            parse276 = Parse276(edi_file)
            print(parse276.edi_parsed)
            print()
            print(parse276.extract_index_data())
            shutil.move(edi_file, 'processed_edi_files/276_files/')

        if edi_file.split('.')[-1] == '277CA':
            parse277ca = Parse277CA(edi_file)
            print(parse277ca.edi_parsed)
            print()
            print(parse277ca.extract_index_data())
            shutil.move(edi_file, 'processed_edi_files/277ca_files/')

