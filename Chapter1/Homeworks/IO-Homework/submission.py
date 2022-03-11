with open('.\student_names.txt', 'r') as f:
    # Read the content of the file
    file_content = f.read()

with open('.\student_names.txt', 'w') as f:
    # Add some random names to the file
    file_content += "\nOmar\nHadil\nIsmail\nRedouane"

    # Write the content to the file
    f.write(file_content)

print("-----------------------------------------------------")
n = int(input("Enter the number of lines you want to read: "))
print("-----------------------------------------------------")
    
lines = file_content.split("\n")

# Read the first n lines of the file
print("Reading the first %d lines of the file" % n)
print(*lines[:n], sep="\n")

print("-----------------------------------------------------")

# Read the last n lines of the file
print("Reading the last %d lines of the file" % n)
print(*lines[-n:], sep="\n")

print("-----------------------------------------------------")
name = input("Enter the name you want to search: ")
print("-----------------------------------------------------")
if name in lines:
    print("%s is in the file" % name)
else:
    print("%s is not in the file" % name)
    
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
for i in range(26):
    with open('.\%s.txt' % chr(i + ord('A')), 'w') as f:
        f.write("")
