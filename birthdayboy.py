import time

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def start_birthday_quest():
    print("🎉 Happy Birthday Sayang! 💖")
    print("Selamat datang di Birthday Love Quest 🎮")
    print("Yuk mulai perjalanan kecil hari ini~\n")
    time.sleep(1.5)

    # Step 1 - Little Quiz
    print("📌 Pertanyaan Pertama")
    print("Kapan kita pertama kali ketemu?")
    options = [
        "1. Di kampus",
        "2. Di warung kopi",
        "3. Lewat tugas kelompok",
        "4. Lupa 😅"
    ]
    for option in options:
        print(option)

    jawaban1 = input("Pilih nomor jawabanmu (1-4): ")

    if jawaban1 == "3":
        print_with_delay("Yesss, kamu inget! 🥹💕", 1.5)
    else:
        print_with_delay("Hehe bukan itu... tapi yang penting kita ketemu ❤", 1.5)

    # Step 2 - Secret Code
    print("\n🔐 Buka Hadiah Spesial")
    code = input("Masukkan kata rahasia (hint: panggilan sayang kita): ").lower()

    if code == "sayang":
        print_with_delay("Benar! 🥰", 1)
        print_with_delay("Ucapan untukmu:", 1)
        print_with_delay("> Terima kasih sudah jadi bagian terbaik dalam hidupku.", 2)
        print_with_delay("> Semoga tahun ini penuh cinta, tawa, dan hal-hal indah.", 2)
        print_with_delay("> I love you always! 💕", 2)
    else:
        print_with_delay("Hint: kata 6 huruf yang kamu panggil aku setiap hari 😚", 2)

    # Final Message
    print("\n🎁 Bonus Love Note")
    lihat_pesan = input("Ketik 'ya' untuk lihat pesan rahasia: ").lower()
    if lihat_pesan == "ya":
        print_with_delay("Setiap hari bersamamu adalah hadiah yang indah.", 2)
        print_with_delay("Selamat ulang tahun ya cinta! 💌", 2)
        print_with_delay("🎈🎈🎈🎈🎈🎈🎈", 1)
    else:
        print("Yaaah, nggak jadi liat pesannya 😢")

# Jalankan program
if __name__ == "__main__":
    start_birthday_quest()
