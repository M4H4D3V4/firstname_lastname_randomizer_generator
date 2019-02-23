import random


def in_list():
    fname = []
    with open("list1.txt", "r") as list1:
        fileRead = list1.readlines()
        for line in fileRead:
            fname.append(line.strip("\n"))
        return fname

def in_list_2():
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

print(num_random)
print(num_random2)

new_name_list = []
def two_name_joiner():
    for x in range(len(in_list())):
        for y in range(1):
            new_name_list.append(in_list()[num_random[x]]+ " "+in_list_2()[num_random2[x]])

two_name_joiner()
print(new_name_list)
def write_new_file():
    with open("generated_name.txt","a") as write:
        for x in range(len(new_name_list)):
            write.write(new_name_list[x])
            write.write("\n")
write_new_file()


