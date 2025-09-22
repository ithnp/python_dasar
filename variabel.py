# Variabel adalah "Wadah" atau "kotak" untuk menyimpan data di dalam memori komputer. Dalam python, Variabel bersifat dinamis - tie datanya bisa berubah selama program berjalan
# Analogi sederhana, bayangkan variabel seperti kotak dengan label. Kita bisa memasukan berbagai jenis barang ke dalam kotak tersebut, dan labelnya adalah nama variabel

# Contoh variabel
nama = "Budi"  # variabel / kotaknya adalah nama berisi text "Budi"
umur = 25  # variabel / kotaknya adalah umur "Berisi int 25"
tinggi = 170.5  # variabel / kotaknya adalah tinggi "berisi float 170.5"
is_login = False  # variabel / kotaknya adalah is_login "berisi bool False"

# Aturan nama variabel
# 1. Tidak boleh dimulai dengan angka ( kecuali di tengah atau dibelakang )
# 2. Tidak boleh menggunakan tanda mines
# 3. Tidak boleh menggunakan keyword dari pyhton contohnya if
# 4. Tidak boleh ada spasi


# Jika ingin mengubah data varibel yang sudah dibuat bisa langsung menggunakan tanda = ( sama dengan )
# Assignment dasar
nama = "Alice"
umur = 30
tinggi = 165.0
is_active = True

# Multiple Assignment
x = y = z = 0               # Semua variabel bernilai 0
a, b, c = 1, 2, 3           # a=1, b=2, c=3
name, age = "Bob", 25       # name = "Bob", age = 25

# Mengubah nilai variabel
skor = 80
print(skor)     # 80
skor = 100      # Mengubah nilai
print(skor)     # 100

# Cara penggunaan variabel dalam sebuah operasi
nama_depan = "Jhon"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)

# Menggunakan varibel dalam print
print("Nama Lengkap : ", nama_lengkap)
print("Luas persegi panjang : ", luas)
