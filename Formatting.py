import re

my_file = open("/Users/darren/Documents/Keylogger/keyLog.txt")

class Cleanup:
    def format_output():
        string_list = my_file.readlines()
        string_list.pop(0)

        date_time = "\d{4}\W\d{2}\W\d{2}\s\d{2}\W\d{2}\W\d{2}"
        words = "[a-zA-Z]"
        numbers = "\W\d\W"
        space = "Key.space"
        enter = "Key.enter"

        keyLogger_output = []

        for x in string_list:
            if(keyLogger_output == []):
                keyLogger_output += re.findall(date_time, x)
            if len(re.findall(words, x)) == 1:
                keyLogger_output += re.findall(words, x)
            if re.findall(space, x):
                keyLogger_output += re.findall(space, x)
            if re.findall(enter, x):
                keyLogger_output += re.findall(enter, x)
            if re.findall(numbers, x):
                keyLogger_output += re.findall(numbers, x)

        date_time = keyLogger_output[0]

        for i, item in enumerate(keyLogger_output):
            if(item == space):
                keyLogger_output[i] = " "
            if(item == enter):
                keyLogger_output[i] = "\n"
            if(re.findall("\d", item)):
                keyLogger_output[i] = re.findall("\d", item)[0]

        keyLogger_output = ''.join(keyLogger_output[1:])
        print(date_time + " \n" + keyLogger_output)

        with open('keyLogFormatted.txt', 'w') as f:
            f.write(date_time + " \n" + keyLogger_output)


Cleanup.format_output()