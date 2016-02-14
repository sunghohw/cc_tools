import json
import sys

# Example Data Structure
class Platform:
    def __init__(self):
        self.name = "Unknown"
        self.launch_year = 0


class AtariLynx(Platform):
    def __init__(self):
        self.name = "Atari Lynx"
        self.launch_year = 1989


class Windows3_1(Platform):
    def __init__(self):
        self.name = "Windows 3.1"
        self.launch_year = 1992


class Steam(Platform):
    def __init__(self):
        self.name = "Steam"
        self.launch_year = 2003


class Game:
    def __init__(self, title="Unknown", platform=None, year=0):
        self.title = title
        self.platform = platform
        self.year = year


class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)


def make_game_library_from_json(json_data):
    game_library = GameLibrary()
    for json_game in json_data:
        title = json_game["title"]
        year = json_game["year"]
        platform = json_game["platform"]

        real_platform = None
        if platform["name"] == "Atari Lynx":
            real_platform = AtariLynx()
        elif platform["name"] == "Steam":
            real_platform = Steam()
        elif platform["name"] == "Windows 3.1":
            real_platform = Windows3_1()
        game = Game(title, real_platform, year)
        game_library.add_game(game)
    return game_library


# Initializing example data for testing purposes
game_data = GameLibrary()
game1 = Game("Chip's Challenge", AtariLynx(), 1989)
game2 = Game("Chip's Challenge 2", Steam(), 2015)
game_data.add_game(game1)
game_data.add_game(game2)

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename> <output dat filename>

default_input_json_file = "data/example_data.json"
default_output_dat_file = "data/example_dat.dat"

if len(sys.argv) == 3:
    input_json_file = sys.argv[1]
    output_dat_file = sys.argv[2]
    print("Using command line args:", input_json_file, output_dat_file)
else:
    input_json_file = default_input_json_file
    output_dat_file = default_output_dat_file
    print("Unknown command line options. Using default values:", input_json_file, output_dat_file)

# Reading the JSON data in from the input file
json_reader = open(input_json_file, "r")
json_data = json.load(json_reader)
json_reader.close() #Close the file now that we're done using it

# Build the Python data structure from the JSON data
#  Note: Your code will be making a CCDataFile instead of a Game Library
#        You will want a function similar to this, but called something like
#             make_cc_data_from_json(json_data)
game_library = make_game_library_from_json(json_data)

# This is where you would write the data to the DAT file
#  Note: You will use the cc_data_utils.write_cc_data_to_dat(cc_data, output_dat_file) function to do this
#        This function takes a CCDataFile object and the filename of the output file
#        It converts the CCDataFile object to binary and writes it to the output file
print("I would write the data to this file", output_dat_file)
