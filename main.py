# nama = "saya"
# x = 2
# y = "2"


# print (x * x)
# print (x * y)

# print("hasilnya adalah:",  x * x , nama)

# nama = input("masukan nama anda: ")
# usia = int(input("masukan usia anda: "))
# nilai = float(input("masukan nilai anda: "))

# print(f"hallo {nama} ")

# if usia >= 7:
#     print("kamu terlalu tua")
# else:
#     print("oke kamu keren")

# if nilai <= 5.2:
#     print("waduh nilai kamu hancur bangetss")
# else:
#     print("wow kamu keren bangets")

# if nilai >= 9:
#     print('''kamu mendapat nilai A
          
# WOW kamu keren bangets''') 
# elif nilai >= 7:
#     print("kamu mendapat nilai B")
# elif nilai >= 5:
#     print("kamu mendapat nilai C")
# elif nilai >= 3:
#     print("kamu mendapat nilai D")

# progres 3

import random
from test import judul_game

nama = input("masukan nama kamu : ")

while nama == "":
    nama =  input("isi dulu nama kamu ya : ")

judul_game(f"selamata datang {nama} di game tebak posisi konbrut")


while True:

    konbrut = random.randint (1,5)

    ember = "[-]"

    ember_isi = [ember] * 5 

    ember_kosong = ember_isi.copy()

    ember_isi[konbrut - 1] = "[8=D]"

    ember_kosong = '  '.join(ember_kosong)
    ember_isi ='  '.join(ember_isi)


    print(f'''COBA KAMU TEBAK DI MANAKAH SI konbrut BERADA? 
        
        {ember_kosong}
        
        ''')

    jawaban = int(input("MASUKAN JAWABAN KAMU [1/2/3/4/5] : "))

    if jawaban == konbrut:
        print(f'''selamat {nama} jawaban kamu benar, landak berada pada {konbrut} dan kamu memilih {jawaban}

        {ember_isi}

        ''')
    else: 
        print(f'''maaf jawaban kamu salah, landak berada pada nomor {konbrut}


    {ember_isi} 

    ''')

    lanjut_game = input("apakah kamu ingin melanjutkan gamenya lagi? [y/n] : ").lower()

    while lanjut_game not in ['y', 'n']:
        lanjut_game = input("[y/n] ? : ").lower()

    if lanjut_game == "y":
        continue
    else:
         exit("game berakhir")
  




# progres 4

# jam = "800"

# ubah_jam = int(jam)

# print(ubah_jam)

# buah = ["nanas", "apel", "melon", "anggur"]

# buah.append ("jeruk")

# print(buah[1])

# usia = ["balita", "remaja", "dewasa", "tua", "lanjut usia"]

# print("******************************")
# print("*** HALLO SELAMAT DATANG ***" )
# print("******************************")

# nama= input("masukan nama kamu : ")

# usia_orang = int(input("masukan usia kamu : "))

# if usia_orang >= 1 and usia_orang <= 6 :
#     print(f"*hallo {nama}* kamu masuk kategory {usia[0]}")
# elif usia_orang >= 7 and usia_orang <= 21:
#     print(f"*hallo {nama}* kamu masuk kategory {usia[1]}") 
# elif usia_orang >= 22 and usia_orang <= 46:
#     print(f"*hallo {nama}* kamu masuk kategory {usia[2]}") 
# elif usia_orang >= 47 and usia_orang <= 57:
#     print(f"*hallo {nama}* kamu masuk kategory {usia[3]}") 
# else:
#     print(f"*hallo {nama}* kamu masuk kategory {usia[4]}")