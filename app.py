import streamlit as st
import time
import random
from PIL import Image

st.set_page_config(page_title="Happy Birthday baby", page_icon="🎂")
# Inisialisasi session state
if "level" not in st.session_state:
    st.session_state.level = 1

if "shown" not in st.session_state:
    st.session_state.shown = []

if "sudah_liat_lagu" not in st.session_state:
    st.session_state.sudah_liat_lagu = False
# ============================
# Session State untuk Level
# ============================
if "level" not in st.session_state:
    st.session_state.level = 1

# Fungsi naik level otomatis
def naik_level():
    st.session_state.level += 1
    st.rerun()

# ============================
# LEVEL 1
# ============================
if st.session_state.level == 1:
    st.title("🎉 Mini Games: Dear My Birthday Boy")
    st.header("💌 Level 1: Our Anniv Date")
    jawaban1 = st.text_input("Kapan yaa kamu nembak aku? (format: dd-mm)")

    if jawaban1:
        if jawaban1 == "09-11":
            st.success("Yeeeaayy kamu inget!🥹💕 Oke lanjuut sayangg")
            st.balloons()
            time.sleep(2)
            naik_level()
        else:
            st.error("Bukan itu sayang.. coba inget-inget lagiii~")

# ============================
# LEVEL 2
# ============================
elif st.session_state.level == 2:
    st.header("Level 2: About You💘")
    jawaban2 = st.text_input("Apa kegiatan/hal yang paling bikin kamu happy seharian?")

    if jawaban2:
        st.info("Okeeyy noteddd😘")
        st.success("Kita lanjut yaa sayang~")
        st.balloons()
        time.sleep(2)
        naik_level()

# ============================
# LEVEL 3
# ============================
elif st.session_state.level == 3:
    st.header("🎁 Level 3: Choose Your Gift!")
    pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

    if st.button("Buka Kotaknya"):
        if pilihan_kotak == "Kotak A":
            st.success("Yeaay! You received small gift🎉💝")
            st.balloons()
            st.markdown("> *“Semoga harimu selalu dipenuhi cinta dan kebahagiaan sayangku💖”*")
        elif pilihan_kotak == "Kotak B":
            st.success("Yeayyy! Kamu dapet... xtra kiss 😘")
            st.image("https://media.giphy.com/media/tpVKvAabWt3G5csMkT/giphy.gif", caption="Heheh love youu 💞")
        elif pilihan_kotak == "Kotak C":
            st.success("🎁 You can request anything: ")
            st.markdown("> *“What Do You Want From Me??”*")
            st.image("https://media.giphy.com/media/wrBURfbZmqqXu/giphy.gif")
        time.sleep(7)
        naik_level()

# ============================
# LEVEL 4
# ============================
elif st.session_state.level == 4:
    st.header("🎈 Level 4: Where Do You want To Go To Celebrate It?")
    pilihan = st.radio(
        "Kamu pilih mana sayangku?",
        ["", "🏠 Di rumah aja, jajan dan nonton sama aku", "🍽️ Romantic Dinner",
         "🌌 Jalan-jalan malmingaan, sambil ngopii deh", "🏕️ Just sit in Cafe and romantic deeptalk..."]
    )

    if pilihan and pilihan != "":
        st.success(f"Okeee! Nanti kita {pilihan} yaa sayaang 😍")
        time.sleep(4)
        naik_level()

# ============================
# LEVEL 5
# ============================
elif st.session_state.level == 5:
    st.header("🌀 Level 5: Love Maze")
    st.write("Escape this maze to meet me!")

    langkah1 = st.selectbox("Langkah 1:", ["Pilih arah", "Kiri", "Kanan"], key="step1")
    if langkah1 == "Kanan":
        st.success("Yeayy ketemu jalannyaa")
        langkah2 = st.selectbox("Langkah 2:", ["Pilih arah", "Maju", "Mundur"], key="step2")
        if langkah2 == "Maju":
            st.success("Yeaaayy bener lagii, lanjut terus sayaang")
            langkah3 = st.selectbox("Langkah 3:", ["Pilih arah", "Kanan", "Kiri"], key="step3")
            if langkah3 == "Kiri":
                st.success("YEAYY!! You escaped and met me 😍")
                st.balloons()
                st.image("https://media.giphy.com/media/5sokLWDYub7efuAD1M/giphy.gif", caption="Pelukkk duluu sayaang")
                st.markdown("> *\"Kamu gabakal tersesat byy, kan sinyal antara kita 5G heheh\"*")
                time.sleep(7)
                naik_level()
            elif langkah3 != "Pilih arah":
                st.warning("Oops, jalannya ketutup. Semangat sayang sedikiit lagi")
        elif langkah2 != "Pilih arah":
            st.warning("Jalan buntu, coba pilih lagi babee")
    elif langkah1 != "Pilih arah":
        st.warning("Yah nyasar yaang, coba ulang sayang😗")

# ============================
# LEVEL 6 – Love Letter & Lagu
# ============================
elif st.session_state.level == 6:
    st.header("🎵 The Final Session~")

    # Inisialisasi state
    if 'sudah_liat_lagu' not in st.session_state:
        st.session_state.sudah_liat_lagu = False

    # Tampilkan video lagu
    st.write("This song for you yang paling *sempurna* di hati aku, Jangan lupa play lagunya dulu yaa buat baca love letternya~ ")
    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")

    # Tombol untuk lanjut
    if not st.session_state.sudah_liat_lagu:
        if st.button("Press the button to read 💌"):
            st.session_state.sudah_liat_lagu = True
            st.rerun()

    # Setelah tombol ditekan, tampilkan Love Letter di bawahnya
    if st.session_state.sudah_liat_lagu:
        st.header("💌 A Love Letter")
        st.markdown("""
> Hai My Dearest,

Selamat Ulang Tahun yaa sayang.. 
Di hari spesial pertamamu sama aku ini, as you know aku super excited buat nyiapin ini semua. Makasih ya udah jadi my supporter, my doctor, my parent, my brother, my everything, especiaallyy karna jadi alasanku senyum in every single day. Glad me to have you in my life..

Semoga di hari spesialmu ini kamu panjang umur, makin sehat, selalu dimudahkan segala urusannya sama Allah. Aku bener bener cant describe how much i love you sayang.. maaf yaa kalo web ini masih jelek heheh aku belum se pro itu walau modal dibantu chatgpt hihihih

Sayang.. Aku tau kadang aku nyebelin, tapi aku selalu sayang kamu and it cant be replace for any reason, apapun itu. And i will try my best for you, i will try to be better than be4. Kamu bakal selalu jadi yang paling *sempurna* di hatiku sayang💖

Sekali lagi **Happy Birthday, My Love!**  
Semoga seterusnya, semua hal baik dan indah di dunia ini selalu menyertai langkahmu, dan semoga aku bisa terus jadi bagian dari kebahagiaanmu, setiap tahun, dan setiap waktu. 

Semoga kita bertahan lama sayangg~~

Love you always 💋
        """)
        st.balloons()
