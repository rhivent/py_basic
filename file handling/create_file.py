'''
Membuat text file dan write in it
caranya dengan built-in function pada python yaitu open()

file handling
use open() function to open the file. The open() function
two parameters; filename and mode

deskripsi open()
mode : r ==> utk Read ==> Default value. Opens a file just for reading. Throws Error if file does not exist
mode : r+ ==> Read + Write ==> Opens a file for both reading and writing
mode : w ==> Opens a file for writing, creates the file if it doesn't exist. Overwrites the file if file exist
mode : w+ ==> Opens a file for both writing and reading, create the file if it does not exist. Overwrites the file is file exists
mode : a ==> append Opens a file for appending
mode : b ==> Binary Mode (e.g. images)
'''

# fh = open('demo.txt','w')
fh = open('demo.txt','a') # for menambah data ke file yg sama tanpa Overwrites file lama

# menulis string di dalam file ini
# fh.write('MSAKDMAKSDMAK \nSMDKAMSKD')
# setelah ditulis maka tutup dngn close() the file

# bisa juga menggunakan exception try and finally
try:
    for i in range(10):
        # start from 0 till 9
        # fh.write("this is line no %d\n" % i)
        # start from 1 to 10
        fh.write("this is line no %d\n" % (i+1))

finally:
    fh.close()

# code try and finally diatas sama dengan dengan kode di bawah ini
with open('module/demo.txt','w') as fh:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+1))
