import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Birthday Quest💖", page_icon="🎂")

# Judul utama
st.title("🎉 Birthday Quest: Love Level Challenge")
st.write("Selamat ulang tahun sayang! 🥰 Yuk isi pertanyaan duluu~")

# ----------------------------
# LEVEL 1: Tanggal Jadian
# ----------------------------
st.header("💌 Level 1: Our Anniv Date")
jawaban1 = st.text_input("Kapan kita jadian? (format: dd-mm)")

if jawaban1:
    if jawaban1 == "09-11":
        st.success("Yeeeaayy kamu inget!🥹💕 Oke lanjuutt!")

        # ----------------------------
        # LEVEL 2: Tentang Kamu
        # ----------------------------
        st.header("🧠 Level 2: About You💘")
        q2 = st.radio(
            "Kegiatan yang paling bikin kamu happy seharian itu apa?",
            [
                "Makan enak trus rebahan 🥱",
                "Main game sampe lupa waktu 🎮",
                "Ngobrol sama aku 😘",
                "Ngambekin aku tanpa sebab 😅",
                "Scroll TikTok seharian sampe lupa mandi 😘"
            ]
        )

        if q2:
            st.balloons()
            st.info("Oke noted! Makasih udah jujur hehe 😆")

            # ----------------------------
            # LEVEL 3: Kotak Hadiah
            # ----------------------------
            st.header("🎁 Level 3: Choose One..")
            pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

            if st.button("Buka Kotaknya"):
                kotak_berisi = random.choice(["Kotak A", "Kotak B", "Kotak C"])
                if pilihan_kotak == kotak_berisi:
                    st.balloons()
                    st.success("YAYY! You received the giftt 🎉")
                    st.markdown("> *“Selamat ulang tahun cintaku! Semoga harimu selalu indah ya sayaang. Glad me to have youu💖”*")
                else:
                    st.warning("Yahh belum ketemu hadiahnya 😢 Tapi cintaku nggak random kok, selalu buat kamu~ 😚")

            # ----------------------------
            # FINAL: Pilih Tempat Rayain
            # ----------------------------
            st.header("🎈 Pilih Tempat Rayain Ulang Tahun")
            tempat = st.radio(
                "Kamu mau rayain ulang tahunnya di mana nih?",
                [
                    "🏠 Di rumah aja, sambil ngbrol tapi ada yang recokin, heheh",
                    "🍽️ Romantic Dinner",
                    "🌌 Jalan-jalan, malmingan",
                    "🏕️ Rayain di cafe"
                ]
            )

            if tempat:
                st.success(f"Okeee! Nanti kita {tempat.split(' ')[1]} ya sayang 😍")
                st.snow()
                st.markdown("## 🥂 Cheers for You!")
                st.write("Terima kasih udah main sampai akhir. Love You Sayaang💕")

        # ----------------------------
        # Lagu Penutup
        # ----------------------------
        st.header("🎶 Lagu untuk Kamu")
        st.write("Ini lagu buat kamu... yang paling *sempurna* 💖")
        st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
        st.markdown("> *“Karena kamu yang terbaik, dan tetap sempurna di mataku 💝”*")

    else:
        st.warning("Bukan itu sayang 😗 coba ingat-ingat lagiii~")
