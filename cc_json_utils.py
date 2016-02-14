"""
Methods for encoding and decoding Chip's Challenge (CC) data to and from binary DAT files
Created for the class Programming for Game Designers
"""
import cc_data,json,sys

def make_cc_data_from_json(json_file):
    cc_datafile = cc_data.CCDataFile()
    read = open(json_file, "r")
    json_data = json.load(read)

    for level,leveldata in json_data.items():
        cc_level = cc_data.CCLevel()
        cc_level.level_number = leveldata["level"]
        cc_level.time = leveldata["time"]
        cc_level.num_chips = leveldata["num_chip"]
        cc_level.upper_layer = leveldata["upper_layer"]
        cc_level.lower_layer = leveldata["lower_layer"]
        for type_num,layer_data in leveldata["optional"]:
            if type_num == "type3": cc_level.add_field(cc_data.CCMapTitleField(layer_data))
            elif type_num == "type4": cc_level.add_field(cc_data.CCTrapControlsField(layer_data))
            elif type_num == "type5": cc_level.add_field(cc_data.CCCloningMachineControlsField(layer_data))
            elif type_num == "type6": cc_level.add_field(cc_data.CCEncodedPasswordField(layer_data))
            elif type_num == "type7": cc_level.add_field(cc_data.CCMapHintField(layer_data))
            elif type_num == "type8": cc_level.add_field(cc_data.CCPasswordField(layer_data))
            elif type_num == "type10":
                cc_monsters = []
                for monster,monster_data in layer_data:
                    cord = cc_data.CCCoordinate(monster_data[0],monster_data[1])
                    cc_monsters.append(cord)
                cc_level.add_field(cc_data.CCMonsterMovementField(cc_monsters))
        cc_datafile.add_level(cc_level)
    return cc_datafile





