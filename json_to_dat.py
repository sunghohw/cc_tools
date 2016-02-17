import cc_dat_utils,cc_json_utils,cc_data,sys

if len(sys.argv) == 3:
    input = sys.argv[1]
    output = sys.argv[2]
    print ("input:"+input+" --> output:" + output)
    cc_data = cc_json_utils.make_cc_data_from_json(input)
    cc_dat_utils.write_cc_data_to_dat(cc_data,output)
    print("complete")
else:
    print("wrong number of arguments!")