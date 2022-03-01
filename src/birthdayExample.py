# Frank Bernal, 2022

import json

#
# this is a relative path to the .json data file
# you can also use a "full" or "absolute path" to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes "/" used in python
# pathToFile = "E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json"
#
# mac (which is built on linux) and linux paths are like this: "a/b/c/d/e/f.json"
#

# relative path
pathToFile = "/Users/frankbernal/Documents/GitHub/LupitasLookupPython/src/birthday.json"


# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]
    # used to display all data in json file
    # print("name = " + name)
    # print("birthday = " + birthday)

    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])

# to get user input
name = input("Enter a name:")
# GS's example print line
# print("name = " + name)
# Test output
print(name + "'s birthday is: " + birthdayDictionary[name])
