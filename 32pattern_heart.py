
'''
define by col and row to see the logic bisa dibntk
    0 1 2 3 4 5 6
0     * *   * *
1   *     *     *
2   *           *
3     *       *
4       *   *
5         *

row ada 6, col ada 7

baris 0 ==> ada col 0, 3, 6
logikanya yg ini modulus 0,3,6 dibagi 3 = 0 shg jika
modulus != 0 maka print asterix (*)

baris 1 ==> kebalikan dari baris 0, dmn yg terisi col 0,
3, dan 6
shg:
...
    kondisi ==> if(row==0 and col%3 != 0) or (row==1 and col%3 == 0)
...


baris 2,3,4,5 dgn pasangna col 0,1,2,3 ada persamaan
row col  substract(-)
2   0    2-0 =2
3   1    3-1 =2
4   2    4-2 =2
5   3    5-3 =2

shg kondisinya
or (row-col==2)


utk pasangan col 4,5,6 dan baris 4,3,2
row col  add(+)
2   6    2+6 =8
3   5    3+5 =8
4   4    4+4 =8
shg kondisinya : or (row+col==8)


'''

for row in range(6):
    for col in range(7):
        if(row==0 and col%3 != 0) or (row==1 and col%3 == 0) or (row-col==2) or (row+col==8):
            print("*",end="") # end="" berguna utk tetap di line yg sama secara default \n utk print()
        else:
            print(end=" ") # utk kondisi yg tidak terpenuhi
    print() # berguna utk meprint data selanjutnya tetapi next line (enter di keyboard)
