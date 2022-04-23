#my_file = open("keyLog.txt", "w")
my_file = open("/Users/darren/Documents/Keylogger/keyLog.txt")

string_list = my_file.readlines()
string_list.pop(0)

for x in string_list:
    print(x)