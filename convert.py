import cc_dat_utils,json
import cc_json_utils

testData = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
#print(str(testData))

from pprint import pprint

with open('data/sunghohw_cc1.json') as data_file:
    data = json.load(data_file)
pprint(data)

#jsonData = cc_json_utils.make_cc_data_from_json("data/sunghohw_cc1.json")
#cc_dat_utils.write_cc_data_to_dat(jsonData,"data/sunghohw_cc1.dat")