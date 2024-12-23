#program HAY Rekening Sederhana
nama = input("masukkan Nama anda:""\n")
while True:
    pin = input("Masukkan PIN anda:""\n")

    if len(pin) == 6 and pin.isdigit():
        print(f"Selamat datang {nama} di HAY Rekening!")
        saldo = 0
        while True:
            print("\nMenu Rekening Sederhana")
            print("1. Cek Saldo")
            print("2. Setor Uang")
            print("3. Tarik Saldo")
            print("4. Keluar")
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                print(f"Sisa saldo: {saldo}")
                ulang = input(f"Apakah Mas/Mbak {nama} ingin Transaksi lagi?(y/n): ")
                if ulang.lower() == "y":
                    continue
                elif ulang.lower() == "n":
                    print(f"Terima kasih {nama} telah menggunakan HAY Rekening!")
                    break
            elif pilihan == 2:
                jumlah = int(input("Masukkan jumlah uang yang ingin disetor:""\n"))
                if jumlah > 0:
                    saldo += jumlah
                    print(f"Setoran berhasil. Sisa saldo: {saldo}")
                    ulang = input(f"Apakah Mas/Mbak {nama} ingin Transaksi lagi?(y/n): ")
                    if ulang.lower() == "y":
                        continue
                    elif ulang.lower() == "n":
                        print(f"Terima kasih {nama} telah menggunakan HAY Rekening!")
                        break
                else:
                    print("Maaf, jumlah setoran harus lebih dari Rp 0.")
            elif pilihan == 3:
                jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: "))
                if jumlah > saldo:
                    print(f"Saldo tidak cukup. Saldo anda {saldo}")
                    ulang = input(f"Apakah Mas/Mbak {nama} ingin Transaksi lagi?(y/n): ")
                    if ulang.lower() == "y":
                        continue
                    elif ulang.lower() == "n":
                        print(f"Terima kasih {nama} telah menggunakan HAY Rekening!")
                        break
                elif jumlah <= 0:
                    print("Maaf, jumlah tarik harus lebih dari Rp 0.")
                else:
                    saldo -= jumlah
                    print(f"Tarik tunai berhasil. Sisa saldo: {saldo}")
                    ulang = input(f"Apakah Mas/Mbak {nama} ingin Transaksi lagi?(y/n): ")
                    if ulang.lower() == "y":
                        continue
                    elif ulang.lower() == "n":
                        print(f"Terima kasih {nama} telah menggunakan HAY Rekening!")
                        break
            elif pilihan == 4:
                print(f"Terimakasih telah berlangganan di HAY Rekening!. Sampai jumpa lagi {nama}!")
                break
            else:
                print(f"Pilihan tidak valid!. Masukkan pilihan yang benar {nama}!")
        ulang = input(f"Apakah ingin mengulangi Program?(y/n): ")
        if ulang.lower() == "y":
            continue
        elif ulang.lower() == "n":
            print(f"Sampa jumpa lagi {nama}! Semoga harimu menyenanagkan!")
            break            
    else:
        print("PIN harus 6 digit")
