
def concise_address_file():
    file_name = input("Please enter the file name to read <Hit Enter to Quit>: ")
    if file_name == "":
        return 0
    try:
        opened_file = open(file_name, 'r')
        opened_file_list = opened_file.readlines()
        num_lines = len(opened_file_list)
        if num_lines % 5 == 0:
            print(f"You have {int(num_lines / 5)} entries in your {file_name} address book")
            write_entries(opened_file_list)
            concise_address_file()
        else:
            print("File does not contain complete entries")
            concise_address_file()
    except IOError:
        print("Error: file not found.")
        concise_address_file()

def write_entries(opened_file_list):
    new_file = open('HunterCarlislePhonebook.txt', 'a+')
    new_file.seek(0,0)
    new_file_list = new_file.readlines()
    concise_address_list = trim_list(opened_file_list)
    for new_item in concise_address_list:
        if not new_item in new_file_list:
            new_file.seek(0,2)
            new_file.write(new_item)
    new_file.close()

def trim_list(opened_file_list):
    concise_address_list = []
    for index in range(0,len(opened_file_list)):
        if index % 5 == 0 or index % 5 == 1 or index % 5 == 4:
            concise_address_list.append(opened_file_list[index])
    return concise_address_list

concise_address_file()


