# Cara menggunakan inputan dari user

# kita bisa meminta input dari pengguna menggunakan functio input()
# input() selalu menghasilkan string (teks)

nama = input("Masukan nama anda : ")
print("hello,", nama)

umur_teks = input("Masukan umur anda : ")
print("Umur anda adalah : ", umur_teks)
print("Tipe Umur", type(umur_teks))  # tipe data string

# walaupun menginput angka akan terbaca string!

# Maka perlu di konversikan kedalam tipe data int

# Konversi tipe data adalah mengubah data dari satu tipe ke tipe data lainnya
# Terdapat beberapa function yang bisa digunakan untuk melakukan konversi dari satu tipe data ke tipe data lainnya, diantaranya
# 1. int(), mengubah string atau data lain menjadi integer ( bilangan bulat )
# 2. str(), mengubah integer atau data lain menjadi string (teks)
# 3. float(), mengubah string atau integer menjadi float (bilangan desimal)
# 4. bool(), mengubah data lain menjadi boolean (True/False)

# Cara nya tinggal masukan varibelnya pada int(umur_teks)
umur = int(umur_teks)
print("Tipe umur dirubah menjadi : ", type(umur))


# Hasil

# Masukan nama anda: HeisenBerg
# hello, HeisenBerg
# Masukan umur anda: 57
# Umur anda adalah:  57
# Tipe Umur < class 'str' >
# Tipe umur dirubah menjadi: < class 'int' >
