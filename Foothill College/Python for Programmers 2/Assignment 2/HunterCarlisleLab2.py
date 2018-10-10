def get_valid_filename():
    file_name = input("Please enter the file name to read <Hit Enter to Quit>: ")
    if file_name == "":
        return 0
    try:
        open_file(file_name)
    except IOError:
        print("Error: file not found.")
    get_valid_filename()

def open_file(file_name):
    opened_file_content = open(file_name, 'r').readlines()
    if len(opened_file_content) % 5 == 0:
        print(f"You have {int(len(opened_file_content) / 5)} entries in your {file_name} address book")
        write_entries(opened_file_content)
    else:
        print(f"{file_name} does not contain complete entries.")

def write_entries(opened_file_list):
    new_file = open('HunterCarlislePhonebook.txt', 'a+')
    new_file.seek(0,0)
    new_file_content = new_file.readlines()
    trimmed_address_list = trim_list(opened_file_list)
    for item in trimmed_address_list:
        if item not in new_file_content:
            new_file.write(item)
    new_file.close()

def trim_list(opened_file_list):
    trimmed_address_list = []
    for index in range(0,len(opened_file_list)):
        if index % 5 == 0 or index % 5 == 1 or index % 5 == 4:
            trimmed_address_list.append(opened_file_list[index])
    return trimmed_address_list

get_valid_filename()


