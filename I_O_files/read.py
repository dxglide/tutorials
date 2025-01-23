# https://www.pythontutorial.net/python-basics/python-read-text-file/ 


# The code in the previous examples works fine with ASCII text files. However, if you’re dealing with other languages such as Japanese, Chinese, and Korean, the text file is not a simple ASCII text file. 
# And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.

# To open a UTF-8 text file, you need to pass the encoding='utf-8' 
# to the open() function to instruct it to expect UTF-8 characters from the file.

import os

print ("-----  I/O FILES   ----  ")
print ("-----  Reading from  a file   ----  ")



# file = 'readme.txt' #
# file_dir = 'I_O_files' # 'Python/tutorials/I_O_files'
# cur_dir = os.getcwd()  #   C:\Users\........\vs-workspace\Python\tutorials
# file = os.path.join(cur_dir, file_dir, file)
def file_path(file, file_dir):
    return os.path.join(os.getcwd(), file_dir, file)
    #return  str(os.getcwd()) + '\\' + file_dir + '\\' + file

file =  file_path('readme.txt', 'I_O_files')

print("---------------------------------------")
print(f'Current working directory: {os.getcwd()}')
print(f'File path: {file}')
print("---------- FILE content ---------------")

print ("-----  Reading from  a file  to end of file. All text  ----  ")
print (file)
if os.path.exists(file):
    print('The file exists')
    with open(file, 'r',  encoding='utf8') as f:
        data = f.read()  # read all the content of the file
        print(data)
else:
    print('The file does not exist')    

print ("-----  Reading from  a file  to end of file.  Read as lines  ----  ")
# file =  file_path('readme.txt', 'I_O_files')
with open(file, 'r',  encoding='utf8') as f:
    [print(line.strip()) for line in f.readlines()]  # strip() removes the newline character at the end of each line.


print ("-----  Reading from  a file  to end of file.  Read line by line  ----  ")
with open(file, 'r',  encoding='utf8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())

print ("-----  Reading from  a file  to end of file.  Read line by line. shorter loop way  ----  ")
# The following code reads the content of the file line by line using a for loop:
with open(file, 'r',  encoding='utf8') as f:
    for line in f:
        print(line.strip())