#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os

# Warna terminal
W  = '\033[0m'
R  = '\033[91m'
G  = '\033[92m'
Y  = '\033[93m'
C  = '\033[96m'

def clear():
    os.system("clear")

def banner():
    print(C + """
╔══════════════════════════════════════════╗
║     🔐 WHATSAPP ILLEGAL REPORT TOOL      ║
║     Made by: Developer AnsXploit 👑      ║
╠══════════════════════════════════════════╣
║   ▸ Tool ini akan membantu kamu          ║
║     melaporkan nomor WhatsApp            ║
║     yang melakukan pelanggaran berat     ║
╚══════════════════════════════════════════╝
""" + W)

def pilih_pelanggaran():
    print(G + "\n[!] Pilih Jenis Pelanggaran:\n")
    pelanggaran_list = [
        "1. Judi Online",
        "2. Penipuan / Scam",
        "3. Spam Chat / Broadcast",
        "4. Konten Dewasa / Porno",
        "5. Ujaran Kebencian / SARA",
        "6. Phishing / Link Palsu",
        "7. Ancaman Kekerasan",
        "8. Lainnya (ketik manual)"
    ]

    for item in pelanggaran_list:
        print(Y + "   " + item + W)

    pilih = raw_input(C + "\nPilih [1-8] : " + W)

    pilihan_dict = {
        "1": "Judi Online",
        "2": "Penipuan / Scam",
        "3": "Spam Chat / Broadcast",
        "4": "Konten Dewasa / Porno",
        "5": "Ujaran Kebencian / SARA",
        "6": "Phishing / Link Palsu",
        "7": "Ancaman Kekerasan",
        "8": None
    }

    pelanggaran = pilihan_dict.get(pilih, None)
    if pelanggaran is None:
        pelanggaran = raw_input(Y + "\n📝 Ketik Jenis Pelanggaran Sendiri: " + W)

    return pelanggaran

def main():
    clear()
    banner()

    print(G + "\n[!] Silakan isi data pelaporan target WhatsApp:\n" + W)
    target      = raw_input(Y + "📌 Nomor Target WhatsApp (+62...) : " + W)
    pelanggaran = pilih_pelanggaran()
    deskripsi   = raw_input(Y + "📝 Deskripsi Singkat Aktivitas Ilegal: " + W)

    # Format isi email
    subject = "Laporan Nomor WhatsApp Melakukan Aktivitas Ilegal"
    body = """
Dear WhatsApp Support,

Saya ingin melaporkan nomor WhatsApp yang terindikasi melakukan aktivitas ilegal dan melanggar ketentuan layanan.

📌 Nomor: {0}
⚠️  Jenis Pelanggaran: {1}
📝 Deskripsi: {2}

Mohon untuk ditindaklanjuti dan diblokir permanen jika terbukti.

Hormat saya,
Pengguna WhatsApp yang Peduli
""".format(target, pelanggaran, deskripsi)

    # Encode URL
    subject_encoded = subject.replace(" ", "%20")
    body_encoded = body.replace("\n", "%0A").replace(" ", "%20")

    mailto = "mailto:support@whatsapp.com?subject={}&body={}".format(subject_encoded, body_encoded)

    print(G + "\n[✔] Membuka Gmail untuk mengirim laporan ke WhatsApp...\n" + W)
    os.system("termux-open '{}'".format(mailto))

main()