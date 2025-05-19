### Task 2: Write and Append Data to a File
#Problem Statement: Write a Python program that:
#1.   Takes user input and writes it to a file named output.txt.
#2.   Appends additional data to the same file.
#3.   Reads and displays the final content of the file.

fil=open('output.txt','w')
writing_file=fil.write(input("Write text to enter into 'output.txt' file: ") + '\n')
print("Data has been written into 'output.txt'\n")
fil.close()

fil=open('output.txt','a')
appending_file=fil.write(input("Appends additional data into the 'output.txt' file: ") + '\n')
print("Data has been appended into 'output.txt'\n")
fil.close()


fil=open('output.txt','r')
reading_file=fil.read()
print("-------- Reading content from 'output.txt'--------")
print(reading_file)
fil.close()