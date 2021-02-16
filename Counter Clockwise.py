#NOMOR 2
'''
Asumsikan i = baris, j = kolom

    AWAL                        AKHIR
______________              _____________
i = 0 & j = 0  diisi dengan i = 0 & j = 3
i = 0 & j = 1  diisi dengan i = 1 & j = 3
i = 0 & j = 2  diisi dengan i = 2 & j = 3
i = 0 & j = 3  diisi dengan i = 3 & j = 3
i = 1 daaannn strusnyaa

sehingga 'j' di AWAL dijadikan 'i' di AKHIR
'i' di AWAL dijadikan 'j' diakhir TETAPI dikurangi 4 terlebih dahulu, misal :
- ketika 'i' di awal = 0, maka 'j' di akhir = 3 - i(di awal) = 3
- ketika 'i' di awal = 1, maka 'j' di akhir = 3 - i(di awal) = 2
dst.
'''

List_Awal = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

def counterClockwise (q):
    total = []
    baris = []
    for i in q:                                                 # inisiasi baris
        for j in i :                                            # inisiasi kolom
            baris.append(q[(i.index(j))][3 - (q.index(i))])     # membuat list dengan urutan counter clockwise dari list awal (belum dibagi per 4)
        total.append(baris[(4*q.index(i)):((4*q.index(i))+4)])  # membuat list di dalam list per 4 value nya (seperti format list awal)
    return total

print(counterClockwise(List_Awal))