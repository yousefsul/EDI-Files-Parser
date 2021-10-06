import glob
import json
import shutil

from db_connection.connectMongoDB import ConnectMongoDB
from parse_276.parse_276 import Parse276
from parse_277CA.parse_277ca import Parse277CA
from parse_837.parse_837 import Parse837
from parse_999.parse_999 import Parse999

if __name__ == '__main__':
    edi_files = glob.glob('edi_files/*.*')
    for edi_file in edi_files:
        if edi_file.split('.')[-1] == '999':
            parse999 = Parse999(edi_file)
            # print(parse999.edi_parsed)
            # print(json.dumps(parse999.edi_parsed , indent= 4))
            print()
            # print(parse999.extract_index_data())
            # print(json.dumps(parse999.extract_index_data(), indent=4 ))
            connection = ConnectMongoDB()
            connection.connect_edi_collection('ack_coll')
            connection.insert_edi_collection(parse999.edi_parsed)
            connection.connect_index_collection('index_coll')
            connection.insert_index_collection(parse999.extract_index_data())
            # shutil.move(edi_file, 'processed_edi_files/999_files/')

        if edi_file.split('.')[-1] == '837':
            parse837 = Parse837(edi_file)
            print(parse837.edi_parsed)
            print()
            print(parse837.extract_index_data())
            connection = ConnectMongoDB()
            # connection.connect_edi_collection('837DictColl')
            connection.connect_edi_collection('837_dict_coll')
            connection.insert_edi_collection(parse837.edi_parsed)
            connection.connect_index_collection('index_coll')
            connection.insert_index_collection(parse837.index_837)
            # shutil.move(edi_file, 'processed_edi_files/837_files/')

        if edi_file.split('.')[-1] == '276':
            parse276 = Parse276(edi_file)
            print(parse276.edi_parsed)
            print()
            print(parse276.extract_index_data())
            # shutil.move(edi_file, 'processed_edi_files/276_files/')

        if edi_file.split('.')[-1] == '277CA':
            parse277ca = Parse277CA(edi_file)
            print(parse277ca.edi_parsed)
            print()
            print(parse277ca.extract_index_data())
            # shutil.move(edi_file, 'processed_edi_files/277ca_files/')


