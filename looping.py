# 1. Membuat Looping 1-100
for i in range(1, 101):
    print(i)

# 2. Mengecek apakah bilangan tersebut adalah genap / ganjil. Jika genap maka jalankan dan jika ganjil maka skip
# Menggunakan if else
for i in range(1, 101):
    if i % 2 == 0:
        continue
    else:
        print(i)

# 3. Mengecek apakah bilangan itu genap atau ganjil
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

# Menggunakan loop for untuk melakukan iterasi dari 1 hingga 100
for i in range(1, 101):
    # Memanggil fungsi cek_ganjil_genap untuk mengecek apakah bilangan tersebut ganjil atau genap
    hasil_cek = cek_ganjil_genap(i)
    # Mencetak bilangan beserta keterangan ganjil atau genap
    print(i, "adalah bilangan", hasil_cek)