# https://www.pythontutorial.net/python-basics/python-write-text-file/

import os

print ("-----  I/O FILES   ----  ")
print ("-----  Writting  to   a file   ----  ")



# file = 'readme.txt' #
# file_dir = 'I_O_files' # 'Python/tutorials/I_O_files'
# cur_dir = os.getcwd()  #   C:\Users\........\vs-workspace\Python\tutorials
# file = os.path.join(cur_dir, file_dir, file)
def file_path(file, file_dir):
    return os.path.join(os.getcwd(), file_dir, file)
    #return  str(os.getcwd()) + '\\' + file_dir + '\\' + file

file =  file_path('writeme.txt', 'I_O_files')

lines_file_not_exist = ['Readme', 'zzHow to write text files in Python']
lines_file_exist = ['Just appending', 'nothing to see there']

print(file)


if os.path.exists(file):
    print('The file exists')
    with open(file, 'a', encoding='utf8') as f:
        f.write('\n'.join(['', 'Append text files', 'The End']))
else:
    print('The file does not exist')
    with open(file, 'w',  encoding='utf8') as f:  # create ne file.  'x' - open for exclusive creation, failing if the file already exists
        f.write('\n'.join(lines_file_not_exist))




#  The following example shows how to use the write() function to write a list of texts to a text file:
# lines = ['Readme', 'How to write text files in Python']
# with open(file, 'w',  encoding='utf8') as f:
#      for line in lines:
#         f.write(line)
#         f.write('\n')


# lines = ['Readme', 'How to write text files in Python']
# with open(file, 'w',  encoding='utf8') as f:
#     f.writelines('\n'.join(lines))