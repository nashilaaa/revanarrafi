import time
import sys

# Utilitas
def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def wait(seconds=1):
    time.sleep(seconds)

# Game logic
def start_game():
    score = 0
    slow_print("🎉 Selamat datang di Birthday Love Quest! 🎂💖")
    slow_print("Petualangan cinta spesial untuk ulang tahunmu dimulai sekarang...\n")
    wait(1)

    # Level 1
    slow_print("📍 Level 1: Tempat Pertama Bertemu")
    slow_print("Kapan kita pertama kali ketemu?")
    print("1. Di kampus")
    print("2. Di warung kopi")
    print("3. Lewat tugas kelompok")
    print("4. Lupa 😅")
    answer1 = input("Jawabanmu (1-4): ")

    if answer1 == "3":
        slow_print("✨ Yesss, kamu inget! 🥹💕")
        score += 1
    else:
        slow_print("😅 Hehe... bukan itu, tapi yang penting kita ketemu~")

    wait(1)

    # Level 2
    slow_print("\n📍 Level 2: Kata Rahasia")
    code = input("Masukkan kata rahasia (6 huruf, kamu panggil aku tiap hari): ").lower()
    if code == "sayang":
        slow_print("💘 Benar! Kamu tahu banget~")
        score += 1
        slow_print("> 'Terima kasih sudah jadi bagian terbaik dalam hidupku.'")
        slow_print("> 'Semoga tahun ini penuh cinta, tawa, dan hal-hal indah!'")
        slow_print("> 'I love you always! 💕'")
    else:
        slow_print("🙈 Belum tepat... tapi kamu pasti tahu itu!")

    wait(1)

    # Level 3
    slow_print("\n📍 Level 3: Misi Kenangan")
    slow_print("Kita pernah nonton film bareng pertama kali. Film apa yang kita tonton?")
    print("1. Kimi no Nawa")
    print("2. Avengers")
    print("3. Laskar Pelangi")
    print("4. Lupa juga 😅")
    answer3 = input("Jawabanmu (1-4): ")

    if answer3 == "1":
        slow_print("💫 Aww iyaaa! Romantis banget waktu itu 😍")
        score += 1
    else:
        slow_print("Hehe bukan itu... tapi tetap seru nontonnya bareng kamu!")

    wait(1)

    # Level 4 – Ulang Tahun di Mana?
    slow_print("\n🎈 Bonus Round: Pilih Tempat Rayain Ulang Tahun!")
    slow_print("Kamu mau rayain ulang tahun kita di mana?")
    print("1. Di pantai sambil liat sunset 🌅")
    print("2. Piknik di taman yang sejuk 🌳")
    print("3. Makan malam romantis di rooftop 🌃")
    print("4. Di rumah aja sambil pelukan 😚")
    place = input("Pilih tempatmu (1-4): ")

    if place == "1":
        slow_print("🌅 Wahh romantis banget! Sunset + kamu = combo paling indah 💖")
    elif place == "2":
        slow_print("🍃 Piknik sambil bawa bekal buatan kamu... priceless 🧺")
    elif place == "3":
        slow_print("🌌 Candlelight dinner di atas kota... kayak drama Korea 😘")
    elif place == "4":
        slow_print("🏠 Pelukan? YES! Tempat ternyaman di dunia adalah pelukanmu 💞")
    else:
        slow_print("Hmm itu tempat baru ya? Yang penting bareng kamu 😄")

    score += 1

    wait(1)
    # Final
    slow_print("\n📜 Pesan Rahasia")
    final = input("Ketik 'love' untuk buka pesan rahasia: ").lower()
    if final == "love":
