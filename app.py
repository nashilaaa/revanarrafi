import streamlit as st
import random

st.set_page_config(page_title="Birthday Quest 💖", page_icon="🎂")

# ============================
# Session State untuk Level
# ============================
if "level" not in st.session_state:
    st.session_state.level = 1

# Fungsi Naik Level
def naik_level():
    st.session_state.level += 1
    st.rerun()

# ============================
# LEVEL 1
# ============================
if st.session_state.level == 1:
    st.title("🎉 Birthday Quest: Love Level Challenge")
    st.header("💌 Level 1: Our Anniv Date")
    jawaban1 = st.text_input("Kapan kita jadian? (format: dd-mm)")

    if jawaban1:
        if jawaban1 == "09-11":
            st.success("Yeeeaayy kamu inget!🥹💕 Kamu lulus Level 1!")
            st.balloons()
            if st.button("Lanjut ke Level 2"):
                naik_level()
        else:
            st.error("Bukan itu sayang 😗 coba ingat-ingat lagiii~")

# ============================
# LEVEL 2
# ============================
elif st.session_state.level == 2:
    st.header("🧠 Level 2: Tentang Kamu 💘")
    st.write("Silahkan diisii sayaang~")
    jawaban2 = st.text_input("Apa kegiatan/hal yang paling bikin kamu happy seharian?")

    if jawaban2:
        st.info("Noteddd 😘")
        st.success("Kita lanjut yaa sayang~")
        if st.button("Lanjut ke Level 3"):
            naik_level()

# ============================
# LEVEL 3
# ============================
elif st.session_state.level == 3:
    st.header("🎁 Level 3: Choose Your Gift!")
    pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

    if st.button("Buka Kotaknya"):
        if pilihan_kotak == "Kotak A":
            st.success("YAYY! Kamu dapet hadiah spesial 🎉💝")
            st.balloons()
            st.markdown("> *“Semoga harimu selalu penuh cinta dan bahagia 💖”*")
        elif pilihan_kotak == "Kotak B":
            st.success("Yeayyy! Kamu dapet... xtra kiss 😘")
            st.image("https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", caption="Heheh love youu 💞")

        elif pilihan_kotak == "Kotak C":
            st.success("🎁 Kamu dapet hadiah spesial: *What do you want from me?* 🤭")

    if st.button("Lanjut ke Level 4"):
        naik_level()

# ============================
# LEVEL 4
# ============================
elif st.session_state.level == 4:
    st.header("🎈 Level 4: Where do you want to celebrate?")
    tempat = st.radio("Kamu mau rayain ulang tahunnya di mana nih?", 
        [
            "🏠 Di rumah aja, sambil ngobrol & nonton bareng",
            "🍽️ Romantic Dinner di tempat spesial",
            "🌌 Jalan-jalan malmingan liat bintang",
            "🏕️ Duduk santai di cafe terus photobooth dehh"
        ])

    if tempat:
        st.success(f"Okeee! Nanti kita {tempat} yaa sayaang 😍")
        if st.button("Lanjut ke Level 5"):
            naik_level()

# ============================
# LEVEL 5 – Love Maze
# ============================
elif st.session_state.level == 5:
    st.header("🌀 Level 5: Love Maze")
    st.write("Kamu ada di labirin cinta, cari jalan ke akuuu 💘")

    langkah1 = st.radio("Langkah 1: Mau ke mana dulu?", ["Kiri", "Kanan"], key="step1")
    if langkah1 == "Kanan":
        langkah2 = st.radio("Langkah 2: Terus ke mana lagi?", ["Maju", "Mundur"], key="step2")
        if langkah2 == "Maju":
            langkah3 = st.radio("Langkah 3: Satu langkah terakhir!", ["Kanan", "Kiri"], key="step3")
            if langkah3 == "Kiri":
                st.success("YEAYY!! Kamu berhasil keluar dari labirin dan nemuin akuuu 😍💕")
                st.balloons()
                st.image("https://media.giphy.com/media/WFZvB7VIXBgiz3oDXE/giphy.gif", caption="Pelukk ahhh~ 💞")
                st.markdown("> *\"Cintaku nggak pernah tersesat, karena jalannya selalu menuju kamu 💖\"*")
                st.snow()
                if st.button("Lanjut ke Hadiah Terakhir 🎶"):
                    naik_level()
            else:
                st.warning("Wah kamu nyasar, balik lagi yaa dari awal~ 🌀")
        elif langkah2:
            st.warning("Aduh... jalan buntu, coba arah lain yaa 😢")
    elif langkah1:
        st.warning("Oops! Jalan itu ketutup semak-semak cinta~ 🌿 Balik lagi ya 😘")

# ============================
# LEVEL 6 – Lagu + Surat Cinta
# ============================
elif st.session_state.level == 6:
    st.header("🎶 Lagu & Surat Cinta Untuk Kamu")
    st.write("Ini lagu buat kamu... yang paling *sempurna* 💖")
    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
    st.markdown("> *“Karena kamu yang terbaik, dan tetap sempurna di mataku 💝”*")

    st.header("💌 Surat Cinta Buat Kamu")
    st.markdown("""
    > Hai My Dearest,

    Di hari spesial pertamamu ini sama aku, I just want to say thaat im so excited untuk nyiapin ini semuaaa. Kamu itu anugerah terindah yang datang di hidupku. Makasih ya udah jadi penyemangatku, pelindungku, dan alasan aku tersenyum tiap hari.

    Aku tahu kadang aku nyebelin, kadang suka susah dimengerti. Tapi cintaku ke kamu selalu nyata, dan gak akan berubah. Kamu tetap jadi yang paling *sempurna* di mataku 💖

    **Happy Birthday, Love!**  
    Semoga segala hal indah menyertai langkahmu. Dan semoga aku bisa jadi bagian dari kebahagiaan kamu, setiap tahun, setiap waktu.

    Love you always 💋
    """)
    st.balloons()
