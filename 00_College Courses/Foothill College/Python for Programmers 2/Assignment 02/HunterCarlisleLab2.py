#!/usr/bin/env python3
"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Two

This program counts the number of entries in one or more phonebook files, and
prints out a result message and number of entries for a valid address text file.
It then creates a second file, HunterCarlislePhonebook.txt, containing abridged entries
from all input files.

Inputs: Address book filenames (.txt)
Prints: Number of entries in Inputs
Output: HunterCarlislePhonebook.txt
"""


def get_existing_filename():
    """ Gets user input filename and validates that it can be opened """
    while True:
        file_name = input("Please enter the file name to read <Hit Enter to Quit>: ")
        if file_name == "":
            break
        try:
            open_valid_file(file_name)
            continue
        except IOError:
            print("Error: file not found.")
            continue


def open_valid_file(file_name):
    """ Opens file and checks if valied address book """
    addressbook = open(file_name, 'r').readlines()
    if len(addressbook) % 5 == 0:
        print(f"You have {int(len(addressbook) / 5)} entries in your {file_name} address book")
        write_entries(addressbook)
    else:
        print(f"{file_name} does not contain complete entries.")


def write_entries(addressbook):
    """ Writes entries in input file list to new/existing HunterCarlislePhonebook.txt file """
    new_phonebook = open('HunterCarlislePhonebook.txt', 'a+')
    new_phonebook.seek(0,0)
    new_phonebook_content = new_phonebook.readlines()
    trimmed_address_list = trim_list(addressbook)
    for item in trimmed_address_list:
        if item not in new_phonebook_content:
            new_phonebook.write(item)
    new_phonebook.close()


def trim_list(address_book):
    """ Removes unnecessary data from address book """
    trimmed_address_list = []
    for index in range(0, len(address_book)):
        if index % 5 == 0 or index % 5 == 1 or index % 5 == 4:
            trimmed_address_list.append(address_book[index])
    return trimmed_address_list


get_existing_filename()

"""
 PROGRAM RUN
"C:/Users/hunterc/Dropbox/Code/CS-Coursework/Foothill College/Python for Programmers 2/Assignment 2/HunterCarlisleLab2.py"
Please enter the file name to read <Hit Enter to Quit>: nofile.txt
Error: file not found.
Please enter the file name to read <Hit Enter to Quit>: err.txt
err.txt does not contain complete entries.
Please enter the file name to read <Hit Enter to Quit>: demo.txt
You have 2 entries in your demo.txt address book
Please enter the file name to read <Hit Enter to Quit>: addressbook.txt
You have 6 entries in your addressbook.txt address book
Please enter the file name to read <Hit Enter to Quit>: 

Process finished with exit code 0
"""
