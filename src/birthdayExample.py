# Frank Bernal
# Lupita's Lookup V1.1
# CIS 024c Python Programming
# 1 March 2022

"""
Version 1.1 includes the advanced solution displayed in GS's example
"""

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

# created list to grab only names to use as *keys*
nameList = []

# loop json list of data and put each name and birthday into the dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"].upper()
    birthday = elem["birthday"]
    # Append all names into a list for searching partial names
    nameList.append(name)
    
    # used to display all data in json file, delete "#" to print entire database
    # print("name = " + name)
    # print("birthday = " + birthday)
    
    # sets name *key* to associated birthday *value*.
    birthdayDictionary[name] = birthday

# nameList should now have a list of all names verbatum in the dictionary

# Welcome the user
print("=============================")
print("Welcome to Lupita's Lookup...")
print("=============================")

# ask to get user input
nameFromUser = input("Enter a name of one of Lupita's friends: ")


print("==================================================")
print("The following people contain the entry \"" + nameFromUser + "\"")
print("==================================================")

# declared this list to gather valid matches from nameList to use as dictionary *keys*
dictionarySearch = []

# iterate through each name in nameList that contains nameFromUser
for person in nameList:
    # If we find a match it'll get appended to dictionarySearch
    if nameFromUser.upper() in person:
        dictionarySearch.append(person)

print(dictionarySearch)
# if dictionaryList is empty
if dictionarySearch == []:
    # print this
    print("Sorry, your entry doesn't match any of Lupita's friends...")
# dictionarySearch now contains a list of valid *keys* to use for fetching data from birthdayDictionary

# iterate through each name from dictionarySearch
for person in dictionarySearch:
    # If the name from dictionarySearch is a valid *key* in birthdayDictionary it'll print the bdays
    if person in birthdayDictionary:
        print(person.title() + "'s birthday is: " + birthdayDictionary[person])
