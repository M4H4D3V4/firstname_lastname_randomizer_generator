import csv
import random
#importing random, which will help us later on to randomize the order of fname and lname from the list.



def csv_to_text():
    """This function simply converts csv to text file."""
    file_name = input("Name the csv file?:")
    with open("from_csv.txt", "+w") as output:
        with open(file_name+".csv", "r") as inputx:
            [output.write(" ".join(row)+'\n') for row in csv.reader(inputx)]

conversion_required = input("Do you have csv file to be converted to text? (y/n):")
in_loop = True
while in_loop:
    if conversion_required is "y":
        csv_to_text()
        break
    elif conversion_required is "n":
        in_loop = False
        break
    else:
        print("Invalid input")
        in_loop = True
        break


def in_list():
    """This function is used to extract the list of first names
    form list1.txt file and append the strings into fname[] list."""
    fname = []
    with open("firstname.txt", "r") as list1:
        fileRead = list1.readlines()
        for line in fileRead:
            fname.append(line.strip("\n"))
        return fname

def in_list_2():
    """This function is used to extract the list of last names
    form list2.txt file and append the strings into lname[] list. """
    lname = []
    with open("lastname.txt", "r") as list2:
        fileread = list2.readlines()
        for line in fileread:
            lname.append(line.strip("\n"))
        return lname

#generating n amount of numbers where n is the number of first names.
num_random = list(range(len(in_list())))
#randomizing the numbers order.
random.shuffle(num_random)

#generating n amount of numbers where n is the number of last names.
num_random2 = list(range(len(in_list_2())))
#randomizing the numbers order.
random.shuffle(num_random2)

print(num_random) #prints the random number for testing
print(num_random2)#for testing purpose

#an empty list where new names will be placed.
new_name_list = []
def two_name_joiner():
    """This function joins first name and last name which are ordered randomly."""
    for x in range(len(in_list())):
        for y in range(1):
            new_name_list.append(in_list()[num_random[x]]+ " "+in_list_2()[num_random2[x]])

#calling the function to let the new name be stored on empty list made before (New_name_list)
two_name_joiner()

print(new_name_list) #testing either the names are builed perfectly or not.

def write_new_file():
    """This function generates the new name list."""
    with open("generated_name.txt","a") as write:
        for x in range(len(new_name_list)):
            write.write(new_name_list[x])
            write.write("\n")
write_new_file()
#at last all the names generated on (new_name_list) are appended to the text file.

