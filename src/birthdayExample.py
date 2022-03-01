# Frank Bernal
# Lupita's Lookup V1.0
# CIS 024c Python Programming
# 1 March 2022

import json

# relative path on Frank's device
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
   
    # used to display all data in json file, delete "#" to print entire database
    # print("name = " + name)
    # print("birthday = " + birthday)

    # sets name to associated birthday.
    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
# the following print function was an example
# print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])

# Welcome the user
print("Welcome to Lupita's Lookup...")
# to get user input
name = input("Enter a name of one of Lupita's friends: ")

# If statement for valid name selection
if name in birthdayDictionary:
    print(name + "'s birthday is: " + birthdayDictionary[name])
else:
    print("Lupita doesn't have any friends with that name...")
# GS's example print line
# print("name = " + name)


