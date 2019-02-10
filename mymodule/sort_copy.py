import re

def sort(file, year):
    f = open(file).readlines()
    f = f[14:1241786]
    with open('locations.csv', mode='w') as out:
        current = ""
        for line in range(len(f)):
            if "\t\t\t\t\t\t" in f[line]:
                f[line] = f[line].split("\t\t\t\t\t\t")
                if "\t" in f[line][-1]:
                    f[line][-1] = f[line][-1].split("\t")[0]
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if len(f[line][0][1]) > 4:
                    f[line][0][1] = f[line][0][1][:4]
                number = re.findall('[1-2][0-9][0-9][0-9]', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split(number[-1])
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):

                        f[line][0][1] = number[-1]
                    else:
                        f[line][0][1] = number[0]
                    f[line][0][0] = f[line][0][0][:-1]

            elif "\t\t\t\t\t" in f[line]:
                f[line] = f[line].split("\t\t\t\t\t")
                if "\t" in f[line][-1]:
                    f[line][-1] = f[line][-1].split("\t")[0]
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if len(f[line][0][1]) > 4:
                    f[line][0][1] = f[line][0][1][:4]
                number = re.findall('[1-2][0-9][0-9][0-9]', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split(number[-1])
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):
                        f[line][0][1] = number[-1]
                    else:
                        f[line][0][1] = number[0]
                    f[line][0][0] = f[line][0][0][:-1]

            elif "\t\t\t\t" in f[line]:
                f[line] = f[line].split("\t\t\t\t")
                if "\t" in f[line][-1]:
                    f[line][-1] = f[line][-1].split("\t")[0]
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if len(f[line][0][1]) > 4:
                    f[line][0][1] = f[line][0][1][:4]
                number = re.findall('[1-2][0-9][0-9][0-9]', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split(number[-1])
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):
                        f[line][0][1] = number[-1]
                    else:
                        f[line][0][1] = number[0]
                    f[line][0][0] = f[line][0][0][:-1]
                if "{" in f[line][0][0]:
                    f[line][0][0] = f[line][0][0].split("{")[0]

            elif "\t\t\t" in f[line]:
                f[line] = f[line].split("\t\t\t")
                if "\t" in f[line][-1]:
                    f[line][-1] = f[line][-1].split("\t")[0]
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if len(f[line][0][1]) > 4:
                    f[line][0][1] = f[line][0][1][:4]
                number = re.findall('[1-2][0-9][0-9][0-9]', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split(number[-1])
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):
                        f[line][0][1] = number[-1]
                    else:
                        f[line][0][1] = number[0]
                    f[line][0][0] = f[line][0][0][:-1]
                if "{" in f[line][0][0]:
                    f[line][0][0] = f[line][0][0].split("{")[0]

            elif "\t\t" in f[line]:
                f[line] = f[line].split("\t\t")
                if "\t" in f[line][-1]:
                    f[line][-1] = f[line][-1].split("\t")[0]
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if len(f[line][0][1]) > 4:
                    f[line][0][1] = f[line][0][1][:4]
                number = re.findall('[1-2][0-9][0-9][0-9]', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split("(" + number[-1] + ")")
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):
                        if len(f[line][0]) == 1:
                            f[line][0].insert(1, number[-1])
                        else:
                            f[line][0][1] = number[-1]
                    else:
                        if len(f[line][0]) == 1:
                            f[line][0].insert(1, number[0])
                        else:
                            f[line][0][1] = number[0]

            else:
                f[line] = f[line].split("\t")
                if "\n" in f[line][-1]:
                    f[line][-1] = f[line][-1][:-1]
                if "(" in f[line][-1]:
                    f[line][-1] = f[line][-2]
                number = re.findall('\d\d\d\d', f[line][0])
                if len(number) > 0:
                    f[line][0] = f[line][0].split(number[-1])
                    if len(number[0]) != 4 or (number[0].isdigit() and int(number[0]) < 1800):
                        f[line][0][1] = number[-1]
                    else:
                        f[line][0][1] = number[0]
                    f[line][0][0] = f[line][0][0][:-1]
            if f[line][0][1] == year:
                if f[line][0][0] == current:
                    continue
                else:
                    current = f[line][0][0]
                    out.write(str(f[line][0][0].strip()) + ";" + str(f[line][0][1]) + ";" + str(f[line][1]) + "\n")
