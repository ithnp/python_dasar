# Tipe data
# 1. Integer (int) = Bilangan Bulat
# 2. Float - Bilangan Desimal ( ada komanya )
# 3. String (str) = Teks
# 4. Boolean (bool) = True/False

####################### START INTEGER ( int ) #######################
# Contoh bilangan bulat positif dan negatif ( int )
umur = 25
tahun_lahir = 1998
saldo = -50000
nol = 0
print("======= TIPE DATA INTEGER =======")
print("# Contoh bilangan bulat positif dan negatif ( int )")
print(umur)
print(tahun_lahir)
print(saldo)
print(nol)


# Contoh bilangan besar ( python bisa handle angka sangat besar )
populasi_dunia = 780000000000
angka_besar = 1234567890987766542134556689901298715
print("# Contoh bilangan besar ( python bisa handle angka sangat besar )")
print(populasi_dunia)
print(angka_besar)
####################### END INTEGER ( int ) #######################

####################### START FLOAT  #######################
# Bilangan dengan koma
tinggi_badan = 170.5
pi = 3.14159
suhu = -10.5

# Notasi Scientific
speed_of_light = 3e8

print("======= TIPE DATA FLOAT =======")
print("# Bilangan dengan koma")
print(speed_of_light)
print(pi)
print("# Notasi Scientific")
print(speed_of_light)
####################### END FLOAT #######################

####################### START STRING (str)  #######################
# String bisa menggunakan qoutes atau double qoutes

# String dengan double qoutes
alamat = "Jl. Merdeka No. 123"
pesan = "Selamat datang di python"
print("======= TIPE DATA STRING =======")
print("# String dengan double qoutes")
print(alamat)
print(pesan)

# String dengan triple qoutes ( Multi-line )
puisi = """
Hallo saya adalah AI
kenapa anda membutuhkan saya ? 
tolong jawab !
"""
print("# String dengan triple qoutes ( Multi-line )")
print(puisi)

# String Kosong
empty_string = ""
####################### END STRING (str) #######################
####################### START BOOLEAN (bool)  #######################
# Boolean values
is_student = True
is_active = False
has_license = True
print("======= TIPE DATA BOOLEAN =======")
print("# Boolean values")
print("# Kondisi penulisan harus menggunakan huruf besar pada boolean True / False")
print(is_active)
print(is_student)
print(has_license)

####################### END BOOLEAN (bool) #######################

####################### START CARA MENGECEK TIPE DATA  #######################
# cara mengecek tipe data
print("======= CARA MENGECEK TIPE DATA =======")
print("# Tipe Data")
print(type(umur))
print(type(is_active))
print(type(tinggi_badan))
print(type(pesan))
####################### END CARA MENGECEK TIPE DATA  #######################


# HASIL

# ======= TIPE DATA INTEGER =======
# # Contoh bilangan bulat positif dan negatif ( int )
# 25
# 1998
# -50000
# 0
# # Contoh bilangan besar ( python bisa handle angka sangat besar )
# 780000000000
# 1234567890987766542134556689901298715
# ======= TIPE DATA FLOAT =======
# # Bilangan dengan koma
# 300000000.0
# 3.14159
# # Notasi Scientific
# 300000000.0
# ======= TIPE DATA STRING =======
# # String dengan double qoutes
# Jl. Merdeka No. 123
# Selamat datang di python
# # String dengan triple qoutes ( Multi-line )

# Hallo saya adalah AI
# kenapa anda membutuhkan saya ?
# tolong jawab !

# ======= TIPE DATA BOOLEAN =======
# # Boolean values
# # Kondisi penulisan harus menggunakan huruf besar pada boolean True / False
# False
# True
# True
# ======= CARA MENGECEK TIPE DATA =======
# # Tipe Data
# <class 'int'>
# <class 'bool'>
# <class 'float'>
# <class 'str'>
