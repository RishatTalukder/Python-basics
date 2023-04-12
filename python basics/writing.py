file_name = "writing_python.txt"

with open(file_name,'a') as file:
    file.write("I love ITVAYA!!!!\n")
    file.write(" I love biriyani")

with open(file_name,'r') as file:
    content = file.read()

print(content)


# file_name = "writing_python.txt"

# with open(file_name,'w') as file:
#     file.write("I love ITVAYA!!!!")
#     file.write(" I love biriyani")

# with open(file_name,'r') as file:
#     content = file.read()

# print(content)