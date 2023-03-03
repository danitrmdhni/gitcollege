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