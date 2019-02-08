
# fh = open('path_file','mode')
fh = open('demo.txt') # r sebagai default mode
print(fh.read()) # read semua isi file
print(fh.read(8)) # reading 8 karakter pertama di dlm file
print(fh.readline()) # utk meread satu full line pertama
print(fh.readline()) # utk meread satu full line kedua
print(fh.readline(4)) # utk meread 4 karakter pertama line ketiga,
print(fh.readline()) # read line after 4 karakter pertama pd line 3 till end character
# di atas menunjukkan bahwa line harus dilanjutkan

# read line di dlm list
print(fh.readlines()) # tampilan utk list, tiap data diisi dngn full line
print(fh.readlines()[4]) # read line full pada index ke 4 artinnya line ke 5

# read one by one and add each operation
for line in fh:
    print(len(line)) #menghitung jumlah karakter di dlm satu line
    print(line.split(' ')) # menampilkan full tiap line yg telah di pisah satu persatu tiap ada spasi
    print(len(line.split(' '))) # menampilkan tiap line jumlah kata yg telh di pisah dng spasi

fh.close()

# using with function tidak perlu close(),
# karena sudah di handler oleh with
with open('demo.txt','r') as fh:
    for line in fh:
        print(len(line))
