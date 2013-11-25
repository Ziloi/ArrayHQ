import sys

# Get Filename and get file contents
filename = raw_input('Enter a file name: ')
file = open(filename)
filecontents = filename.readlines()
f.close()

# Process... But first get input after how many letters or certain letter
process_option = raw_input('Would you prefer to remove everything from a line after a certain character "1", or after a certain amount of characters "2" (1/2): ')
if process_option == 1:
  letter = raw_input('Which letter?: ')
if process_option == 2:
  number = raw_input('How many characters?: ')
  
  for line in filecontents:
    [line[i:i+number] for i in range(0, len(line), n)]

array_option = raw_input('Would you like to print an array instead of text (y/n): ')
if array_option == "y":
  

if array_option == "n":
