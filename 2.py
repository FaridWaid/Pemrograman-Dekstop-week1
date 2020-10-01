x = "ya"
while x=="ya":
    print("Menghitung Luas dan Keliling Persegi Panjang")
    print("Luas Persegi panjang")
    p = int(input("Masukkan nilai p(panjang): "))
    l = int(input("Masukkan nilai l(lebar): "))
    luas = p * l
    print("Luas Persegi panjang tersebut = ",luas)
    print("")
    print("Keliling Persegi panjang")
    p = int(input("Masukkan nilai p(panjang): "))
    l = int(input("Masukkan nilai l(lebar): "))
    keliling = (p + l)*2
    print("Keliling Persegi panjang tersebut = ",keliling)
    x = str(input("Apakah ingin menghitung lagi? (ya/tidak)"))
