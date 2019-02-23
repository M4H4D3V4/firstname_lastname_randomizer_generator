import random
#importing random, which will help us later on to randomize the order of fname and lname from the list.

def in_list():
    """This function is used to extract the list of first names
    form list1.txt file and append the strings into fname[] list."""
    fname = []
    with open("list1.txt", "r") as list1:
        fileRead = list1.readlines()
        for line in fileRead:
            fname.append(line.strip("\n"))
        return fname

def in_list_2():
    """This function is used to extract the list of last names
    form list2.txt file and append the strings into lname[] list. """
    lname = []
    with open("list2.txt", "r") as list2:
        fileread = list2.readlines()
        for line in fileread:
            lname.append(line.strip("\n"))
        return lname


num_random = list(range(len(in_list())))
random.shuffle(num_random)

num_random2 = list(range(len(in_list_2())))
random.shuffle(num_random2)

print(num_random) #prints the random number for testing
print(num_random2)

new_name_list = []
def two_name_joiner():
    """This function joins first name and last name which are ordered randomly."""
    for x in range(len(in_list())):
        for y in range(1):
            new_name_list.append(in_list()[num_random[x]]+ " "+in_list_2()[num_random2[x]])

two_name_joiner()

print(new_name_list)
def write_new_file():
    """This function generates the new name list."""
    with open("generated_name.txt","a") as write:
        for x in range(len(new_name_list)):
            write.write(new_name_list[x])
            write.write("\n")
write_new_file()


