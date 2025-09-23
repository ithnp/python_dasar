# Cara menggabungkan string
# untuk menggabungkan string, kita bisa menggunakan tanda + (tambah)
# Tipe data string tidak bisa digabungkan dengan tipe data lain seperti integer, float, atau boolean, kita harus konversi dulu tipe data lain menjadi tipe data string

# Contoh
nama = "Budi"  # tipe data string
umur = 23  # tipe data int

# Ketika ingin menggabungkan dalam 1 variabel tidak akan bisa karna umur itu adalah int, contohnya

# pesan = "Nama Saya" + nama + "Umur saya" + umur
# print(pesan)

# akan ada error seperti ini
#     pesan = "Nama Saya" + nama + "Umur saya" + umur
# TypeError: can only concatenate str (not "int") to str

# Maka solusinya perlu dikonversi menjadi string variabel umur tersebut seperti dibawah ini

pesan = "Nama saya : " + nama + "Umur saya : " + str(umur)
print(pesan)
