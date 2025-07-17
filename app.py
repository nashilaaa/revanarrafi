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
st.write("Silahkan diisii sayaang~")

jawaban2 = st.text_input("Apa kegiatan/hal yang paling bikin kamu happy seharian?")

if jawaban2:
    st.info(f"Okey notedd😘")
    st.success("Okee lannjuut")
            # ===============================
            # LEVEL 3: PIct Your Gift
            # ===============================
            st.header("🎁 Level 3: Choose One..")
            pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

            if st.button("Buka Kotaknya"):
                kotak_berisi = random.choice(["Kotak A", "Kotak B", "Kotak C"])
                if pilihan_kotak == "Kotak A":
                    st.success("YAYY! Kamu dapet hadiah spesial 🎉💝")
                    st.balloons()
                    st.markdown("> *“Selamat ulang tahun cintaku! Semoga harimu selalu penuh cinta dan bahagia. I’m sooo lucky to have you 💖”*")
                elif:
                    pilihan_kotak == "Kotak B":
                    st.success("Yeayyy! Get xtra kiss")
                elif:
                    pilihan_kotak == "Kotak C":
                    st.success(*special gift "What Do You Want From mee?")

                # ===============================
                # LEVEL 4: Choose your place to go
                # ===============================
                st.header("🎈 Level 4: Where do you want to celebrate your day?")
                tempat = st.radio("Kamu mau rayain ulang tahunnya di mana nih?", 
                    [
                        "🏠 Di rumah aja, sambil ngobrol & nonton bareng",
                        "🍽️ Romantic Dinner di tempat spesial",
                        "🌌 Jalan-jalan malmingan liat bintang",
                        "🏕️ Duduk santai di cafe lucu"
                    ])

                if tempat:
                    st.success(f"Okeee! Nanti kita `{tempat}` yaa sayaang 😍")
                    st.markdown("## 🥂 Cheers for You!")
                    st.write("Terima kasih udah main sampai akhir. You are loved so much 💕")

                    # LEVEL 5 - Mini Game Labirin Cinta
st.header("🌀 Level 5: Love Maze")
st.write("Ceritanya kamu lagi ada di labirin dan harus temuin jalan kelaur buat ketemu sama aku, semangat💘")

langkah1 = st.radio("Langkah 1: Mau ke mana dulu?", ["Kiri", "Kanan"], key="step1")

if langkah1:
    if langkah1 == "Kanan":
        langkah2 = st.radio("Langkah 2: Terus ke mana lagi?", ["Maju", "Mundur"], key="step2")

        if langkah2:
            if langkah2 == "Maju":
                langkah3 = st.radio("Langkah 3: Satu langkah terakhir!", ["Kanan", "Kiri"], key="step3")

                if langkah3:
                    if langkah3 == "Kiri":
                        st.balloons()
                        st.success("YEAYY!! Kamu berhasil keluar dari labirin dan nemuin akuuu 😍💕")
                        st.image("https://media.giphy.com/media/WFZvB7VIXBgiz3oDXE/giphy.gif", caption="Pelukk ahhh~ 💞")

                        st.markdown("""
                        ### 🎁 Hadiah Buat Kamu
                        Karena kamu udah nemuin aku... ini hadiah spesial dari akuuu 😘
                        > *"Cintaku nggak pernah tersesat, karena jalannya selalu menuju kamu 💖"*
                        """)
                        st.snow()
                    else:
                        st.warning("Wah kamu nyasar, balik lagi yaa dari awal~ 🌀")
            else:
                st.warning("Aduh... jalan buntu, coba arah lain yaa sayang 😢")
    else:
        st.warning("Oops! Jalan itu ketutup semak-semak cinta~ 🌿 Balik lagi ya 😘")


                    # ===============================
                    # MUSIK: Lagu Romantis
                    # ===============================
                    st.header("🎶 Lagu untuk Kamu")
                    st.write("Ini lagu buat kamu... yang paling *sempurna* 💖")
                    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
                    st.markdown("> *“Karena kamu yang terbaik, dan tetap sempurna di mataku 💝”*")

                    # ===============================
                    # BONUS: Surat Cinta 💌
                    # ===============================
                    st.header("💌 Surat Cinta Buat Kamu")
                    st.markdown("""
                    > Hai sayangku,

                    Di hari spesial pertamamu ini sama aku, aku cuma mau bilang betapa bersyukurnya aku punya kamu. Kamu itu anugerah terindah yang datang di hidupku. Makasih ya udah jadi penyemangatku, pelindungku, dan alasan aku tersenyum tiap hari.

                    Aku tahu kadang aku nyebelin, kadang suka susah dimengerti. Tapi cintaku ke kamu selalu nyata, dan gak akan berubah. Kamu tetap jadi yang paling *sempurna* di mataku 💖

                    **Happy Birthday, Love!**
                    Semoga segala hal indah menyertai langkahmu. Dan semoga aku bisa jadi bagian dari kebahagiaan kamu, setiap tahun, setiap waktu.

                    Love you always 💋
                    """)



    else:
        st.error("Bukan itu sayang 😗 coba ingat-ingat lagiii~")
