# https://www.pythontutorial.net/python-basics/python-write-text-file/


print ("-----  I/O FILES   ----  ")
print ("-----  Writting  to   a file   ----  ")



# file = 'readme.txt' #
# file_dir = 'I_O_files' # 'Python/tutorials/I_O_files'
# cur_dir = os.getcwd()  #   C:\Users\........\vs-workspace\Python\tutorials
# file = os.path.join(cur_dir, file_dir, file)
def file_path(file, file_dir):
    return os.path.join(os.getcwd(), file_dir, file)
    #return  str(os.getcwd()) + '\\' + file_dir + '\\' + file

file =  file_path('write.txt', 'I_O_files')

lines = ['Readme', 'How to write text files in Python']
with open(file, 'w',  encoding='utf8') as f:
    f.write('readme')