import os
import time
from datetime import datetime

def input_data():
    print("\n===== Data Input FS =====")
    nama = input("Masukkan Nama: ")
    no_hp = input("Masukkan No Hp: ")
    nomor_pk = input("Masukkan Nomor PK: ")
    data = f"{nama},{no_hp},{nomor_pk}\n"

    # Membaca data yang sudah ada
    with open("data.txt", "r") as file:
        existing_data = file.readlines()

    # Memeriksa keberadaan data yang sama
    for line in existing_data:
        if data.strip() == line.strip():
            print("Data sudah ada atau tidak valid.")
            return

    # Menyimpan data baru
    with open("data.txt", "a") as file:
        file.write(data)

    print("Data berhasil disimpan.")

def lihat_data():
    print("\n===== Data Input FS =====")
    with open("data.txt", "r") as file:
        data = file.readlines()

        for i, line in enumerate(data, start=1):
            nama, no_hp, nomor_pk = line.strip().split(",")
            print(f"Data ke-{i}:")
            print(f"Nama: {nama}")
            print(f"No Hp: {no_hp}")
            print(f"Nomor PK: {nomor_pk}")
            print("-" * 30)

def pilih_data():
    print("\n===== Data Input FS =====")
    with open("data.txt", "r") as file:
        data = file.readlines()

    for i, line in enumerate(data, start=1):
        nama, no_hp, nomor_pk = line.strip().split(",")
        print(f"{i}. Nama: {nama}")

    nomor_data = int(input("Masukkan nomor data yang ingin dipilih: "))

    if 1 <= nomor_data <= len(data):
        nama, no_hp, nomor_pk = data[nomor_data - 1].strip().split(",")
        print(f"Data yang terpilih:")
        print(f"Nama: {nama}")
        print(f"No Hp: {no_hp}")
        print(f"Nomor PK: {nomor_pk}")
        hyperlink = f"https://wa.me/62{no_hp}"
        os.system(f"termux-open-url {hyperlink}")
    else:
        print("Nomor data tidak valid.")

def hapus_data():
    print("\n===== Data Input FS =====")
    nama = input("Masukkan Nama: ")

    with open("data.txt", "r") as file:
        data = file.readlines()

    with open("data.txt", "w") as file:
        for line in data:
            if nama not in line:
                file.write(line)

    print("Data berhasil dihapus.")

def lihat_log():
    print("\n===== Log Data FS =====")
    with open("log.txt", "r") as file:
        log_data = file.read()
    print(log_data)

def automasi():
    while True:
        print("\n===== Automasi FS =====")
        print("1. Mulai")
        print("2. Berhenti")
        print("3. Kembali")
        print()

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            with open("data.txt", "r") as file:
                data = file.readlines()

            for line in data:
                nama, no_hp, nomor_pk = line.strip().split(",")
                hyperlink = f"https://wa.me/62{no_hp}?text=Pagi%20Bapak/Ibu%20apa%20kabar%20?%20sehat%20selalu%20ya,%20saya%20Saepul%20Hayat%20dari%20BPR%20Supra%20bagian%20Staff%20Marketing.%0A%0ASaya%20mau%20menawarkan%20kembali%20Bapak/Ibu%20yang%20sudah%20lunas%20ataupun%20akan%20lunas,%20Barangkali%20sudah%20di%20pertimbangkan%20kebutuhan%20nya?%0A%0Asedang%20ada%20promo%20kenaikan%20plafond,sayang%20untuk%20di%20lewatkan,Ada%20khusus%20nasabah%20lama%20dan%20bisa%20langsung%20proses.%0A%0ASaat%20ini%20BPR%20Supra%20ada%20pinjaman%20dengan%20jaminan%20BPJS%20Tk,%20proses%20cepat...%20bawa%20teman%20dapat%20fee%201%25.%0A%0AUntuk%20informasi%20lebih%20lanjut%20beserta%20rincian%20perhitungannya%20boleh%20hubungi%20kembali%20ke%20wa%20ini.terimakasih.%0A%0AApabila%20sudah%20meminjam%20mohon%20abaikan%20pesan%20ini%20&%20tolong%20rekomendasikan%20kami%20kepada%20teman%22%20/%20saudara%20bapak/ibu%20sekalian%20ya%20pa/bu%20terimakasih."
                os.system(f"termux-open-url {hyperlink}")
                waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"Berhasil membuka hyperlink pada {waktu}")
                time.sleep(6)  # Tunggu 6 detik sebelum membuka nomor HP berikutnya

        elif pilihan == "2":
            break
        elif pilihan == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-3.")

# Mengecek apakah file data.txt sudah ada
if not os.path.exists("data.txt"):
    with open("data.txt", "w") as file:
        pass

while True:
    print("===== Data Input FS =====")
    print("Menu:")
    print("1. Input Data")
    print("2. Lihat Data")
    print("3. Pilih Data")
    print("4. Hapus Data")
    print("5. Log Data")
    print("6. Automasi")
    print("7. Keluar")
    print()

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        input_data()
    elif pilihan == "2":
        lihat_data()
    elif pilihan == "3":
        pilih_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        lihat_log()
    elif pilihan == "6":
        automasi()
    elif pilihan == "7":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-7.")
