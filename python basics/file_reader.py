file_name = "text_folder/pi.txt"

with open(file_name) as file:
    lines = file.readlines()

# print(lines)

pi = ""

for line in lines:
    pi = pi + line.rstrip()

bday = input("enter your birthday")
if bday in pi:
    print("yes!!!")

else:
    print("sad,pi ei tore chay nai")


# print(f"{pi[:52]}")
# print(len(pi))
    # for line in file:
    #     print(line+"it vaya")

#content = open("pi.txt").read()

# print(cotent)