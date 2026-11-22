with open("hello.txt","w") as file:
    file.write("hello I am student\n")
    file.write(" of MIT ADT UNIVERSITY\n")
    file.write(" i am from sy 13\n")
    file.write(" adtbuuyguyg\n")

with open("hello.txt","r") as file:
    lines = file.readlines()
    print(lines)

line_count=len(lines)
print("total number of lines : ",line_count)

first_two_lines = lines[:2]

print("\nfirst two lines:")
for line in first_two_lines:
    print(line.strip())

with open("output.txt","w") as file:
    file.writelines(first_two_lines)

    print("\nfirst two lines successfully written to output.txt")
