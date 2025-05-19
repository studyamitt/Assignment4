### Task 1: Read a File and Handle Errors
#Write a Python program that:
#1.   Opens and reads a text file named sample.txt.
#2.   Prints its content line by line.
#3.   Handles errors gracefully if the file does not exist.

'''
#Ex1.
fil=open('sample.txt','r')
read_file1=fil.read()
print(read_file1)
fil.close()
'''
#Ex2.
try:
    i=1
    fil2=open('sample.txt','r')
    print('Reading File Contents:')
    for f in fil2:
        print('Line :',i,'-',f.strip())
        i=i+1
    fil2.close()
except FileNotFoundError:
    print("Error: File 'sample.txt' was not found")
finally:
    print("...")



#Ex3.
try:
    fil3=open('sample.txt','r')
    read_file3=fil3.read()
    print('\nReading File Contents: \n')
    print(read_file3)
except FileNotFoundError:
    print("Error: File 'sample.txt' was not found")
finally:
    print("...")