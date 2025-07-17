import streamlit as st
import random

st.set_page_config(page_title="Birthday Quest💖", page_icon="🎂")

# ===============================
# JUDUL AWAL
# ===============================
st.title("🎉 Birthday Quest: Love Level Challenge")
st.write("Selamat ulang tahun sayang! 🥰 Yuk isi quest-nya, dan jangan curang yaa~")

# ===============================
# LEVEL 1: Tanggal Jadian
# ===============================
st.header("💌 Level 1: Our Anniv Date")
jawaban1 = st.text_input("Kapan kita jadian? (format: dd-mm)")

if jawaban1:
    if jawaban1 == "09-11":
        st.success("Yeeeaayy kamu inget!🥹💕 Kamu lulus Level 1!")
        st.balloons()

        # ===============================
        # LEVEL 2: Tentang Kamu
        # ===============================
        st.header("🧠 Level 2: Tentang Kamu 💘")
        st.write("Jawab jujur yaa, aku pengen tahu sisi lucu kamu~")
        q2 = st.radio(
            "Kegiatan yang paling bikin kamu happy seharian itu apa?",
            [
                "🍜 Makan enak trus rebahan",
                "🎮 Main game sampe lupa waktu",
                "🫶 Ngobrol sama aku",
                "😗 Ngambekin aku tanpa sebab",
                "📱Scroll TikTok sampe lupa mandi"
            ]
        )

        if q2:
            st.info("Noted yaa hehe 😘")
            st.success("Lanjut ke level 3 yaa~")

            # ===============================
            # LEVEL 3: Tebak Hadiah
            # ===============================
            st.header("🎁 Level 3: Tebak Hadiah di Kotak")
            pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

            if st.button("Buka Kotaknya"):
                kotak_berisi = random.choice(["Kotak A", "Kotak B", "Kotak C"])
                if pilihan_kotak == kotak_berisi:
                    st.success("YAYY! Kamu dapet hadiah spesial 🎉💝")
                    st.balloons()
                    st.markdown("> *“Selamat ulang tahun cintaku! Semoga harimu selalu penuh cinta dan bahagia. I’m sooo lucky to have you 💖”*")
                else:
                    st.warning("Yahh belum ketemu hadiahnya 😢 Tapi cintaku nggak random kok, selalu buat kamu~ 😚")

                # ===============================
                # LEVEL 4: Pilih Tempat Perayaan
                # ===============================
                st.header("🎈 Level 4: Pilih Tempat Rayain Ulang Tahun")
                tempat = st.radio("Kamu mau rayain ulang tahunnya di mana nih?", 
                    [
                        "🏠 Di rumah aja, sambil ngobrol & nonton bareng",
                        "🍽️ Romantic Dinner di tempat spesial",
                        "🌌 Jalan-jalan malmingan liat bintang",
                        "🏕️ Duduk santai di cafe lucu"
                    ])

                if tempat:
                    st.success(f"Okeee! Nanti kita `{tempat}` yaa sayaang 😍")
                    st.snow()
                    st.markdown("## 🥂 Cheers for You!")
                    st.write("Terima kasih udah main sampai akhir. You are loved so much 💕")

                    # ===============================
                    # BONUS: Surat Cinta 💌
                    # ===============================
                    st.header("💌 Surat Cinta Buat Kamu")
                    st.markdown("""
                    > Hai sayangku,

                    Di hari spesial ini, aku cuma mau bilang betapa bersyukurnya aku punya kamu. Kamu itu anugerah terindah yang datang di hidupku. Makasih ya udah jadi penyemangatku, pelindungku, dan alasan aku tersenyum tiap hari.

                    Aku tahu kadang aku nyebelin, kadang suka susah dimengerti. Tapi cintaku ke kamu selalu nyata, dan gak akan berubah. Kamu tetap jadi yang paling *sempurna* di mataku 💖

                    **Happy Birthday, Love!**
                    Semoga segala hal indah menyertai langkahmu. Dan semoga aku bisa jadi bagian dari kebahagiaan kamu, setiap tahun, setiap waktu.

                    Love you always 💋
                    """)

                    # ===============================
                    # MUSIK: Lagu Romantis
                    # ===============================
                    st.header("🎶 Lagu untuk Kamu")
                    st.write("Ini lagu buat kamu... yang paling *sempurna* 💖")
                    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
                    st.markdown("> *“Karena kamu yang terbaik, dan tetap sempurna di mataku 💝”*")

    else:
        st.error("Bukan itu sayang 😗 coba ingat-ingat lagiii~")
