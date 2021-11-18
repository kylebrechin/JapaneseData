import json
import csv
#############################################
# Start Tutorial Code
#############################################














#############################################
# 4. Convert CSV to JSON
#############################################
with open('01_names.csv', 'r', encoding="utf8") as f:
    # read the csv file
    reader = csv.reader(f)                                                # prints csv.reader OBJ
    next(reader) # skips header row
    # create the name of the json file
    data = {"names": []}
    for row in reader:
        data["names"].append({"firstname":"ゆき", "age": "三十八"})

with open("created_names.json", 'w', encoding="utf8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)



#############################################
# 3. WRITE JSON
#############################################
    # REFERENCE:
    # https://www.geeksforgeeks.org/append-to-json-file-using-python/
# def write_json(data, filename="01_names.json"):
#
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4)
#
# with open("01_names.json") as json_file:
#
#
#     data = json.load(json_file)
#     # get the data under NAMES
#     temp = data["names"]
#     # create a new set of data
#     y = {"firstname": "Joe", "age": 30}
#     # append data
#     temp.append(y)
#
# # write new data file over old
# write_json(data)


#############################################
# 2. WRITE JSON
#############################################
# def write_json(data, filename="01_names.csv"):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4)
#
# data= ["Bob", "Cindy"]
# write_json(data)

# with open(file, 'r') as json_file:
#     data = json.load(json_file)
#     write_json(data)

#############################################
# 1. READ JSON
#############################################
# file = '01_names.json'
# with open(file, 'r') as json_file:
#     # gets the main dictionary
#     data = json.load(json_file)
#     # get all the data under NAMES
#     name_data = data["names"]
#     # print each set of data
#     for i in name_data:
#         # in the set, get the value from the key firstname
#         name = i["firstname"]
#         # in the set, get the value from the key age
#         age = i["age"]
#         print(f"{name} is {age}")


#############################################
# End Tutorial Code
#############################################
