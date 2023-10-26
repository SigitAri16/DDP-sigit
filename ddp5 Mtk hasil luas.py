print('''
Silahkan pilih tools dibawah ini dengan mengirimkan nomernya
===============
tools yang tersedia
===============
1.luas persegi
2.luas lingkaran
3.luas segitiga
''')
a = int(input("masukan pilihan mu : "))
match a:
    case 1:
        luaspersegi = int(input("masukan nilai sisi : "))
        hasilluas = luaspersegi*luaspersegi
        print("luas persegi adalah : " ,hasilluas)
    case 2:
        nilaiphi = float(input("masukan nilai phi : "))
        nilaijarijari =  int(input("masukan nilai jari jari :"))
        hasilluas = nilaiphi * nilaijarijari
        print("luas lingkaran adalah : ",hasilluas)
    case 3:
        rumus = float (0.5)
        alas = int(input("masukan nilai alas : "))
        tinggi = int(input("masukan niai tinggi : "))
        hasilluas = rumus*alas*tinggi
        print("luas segitiga adalah : ",hasilluas)
    case _:
        print("hasilluas")