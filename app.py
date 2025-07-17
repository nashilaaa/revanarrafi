import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Birthday Quest 💖", page_icon="🎂")

# ============================
# Session State untuk Level
# ============================
if "level" not in st.session_state:
    st.session_state.level = 1

if "shown" not in st.session_state:
    st.session_state.shown = []

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
            st.success("Yeeeaayy kamu inget!🥹💕 Oke lanjuut sayangg")
            st.balloons()
            if st.button("Lanjut ke Level 2"):
                naik_level()
        else:
            st.error("Bukan itu sayang 😗 coba ingat-ingat lagiii~")

# ============================
# LEVEL 2
# ============================
elif st.session_state.level == 2:
    st.header("🧠 Level 2: About You💘")
    jawaban2 = st.text_input("Apa kegiatan/hal yang paling bikin kamu happy seharian?")

    if jawaban2:
        st.info("Okeeyy noteddd 😘")
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
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3NldjQ0Y2U3dm85eG92Z3NybjNidTMxaGRqbGdqazRoemhiaWhvMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tpVKvAabWt3G5csMkT/giphy.gif", caption="Heheh love youu 💞")
        elif pilihan_kotak == "Kotak C":
            st.success("🎁 You can request anything: ")
            st.markdown("> *“What Do You Want From Me??”*")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmdlamVpeXg0eTUydmkxYWxlbzJsbmRucmhhZzZ1MGxja2NhcWFycyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wrBURfbZmqqXu/giphy.gif")

    if st.button("Lanjut ke Level 4"):
        naik_level()

# ============================
# LEVEL 4
# ============================
elif st.session_state.level == 4:
    st.header("🎈 Level 4: Where Do You want To Go To Celebrate?")
    pilihan = st.radio(
        "Kamu pilih mana sayangku?",
        ["", "🏠 Di rumah aja", "🍽️ Romantic Dinner", "🌌 Jalan malming", "🏕️ Nongkrong cafe"]
    )

    if pilihan:
        st.success(f"Okeee! Nanti kita {pilihan} yaa sayaang 😍")
        if st.button("Lanjut ke Level 5"):
            naik_level()
    else:
        if st.button("Lewati dulu & lanjut ke Level 5"):
            naik_level()

# ============================
# LEVEL 5
# ============================
elif st.session_state.level == 5:
    st.header("🌀 Level 5: Love Maze")
    st.write("Escape this maze to meet me! 💘")

    langkah1 = st.selectbox("Langkah 1:", ["Pilih arah", "Kiri", "Kanan"], key="step1")
    if langkah1 == "Kanan":
        langkah2 = st.selectbox("Langkah 2:", ["Pilih arah", "Maju", "Mundur"], key="step2")
        if langkah2 == "Maju":
            langkah3 = st.selectbox("Langkah 3:", ["Pilih arah", "Kanan", "Kiri"], key="step3")
            if langkah3 == "Kiri":
                st.success("YEAYY!! You escaped and met me 😍")
                st.balloons()
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExPWVjZjA1ZTQ3dTB3MTlnd2lsemJ4OHFmZ3RuN2VzdWIwcWhidXlnbmVrNDZsbGhzZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5sokLWDYub7efuAD1M/giphy.gif", caption="Pelukkk 💞")
                st.markdown("> *\"Cintaku gabakal tersesat, jalannya selalu ke kamu 💖\"*")
                if st.button("Lanjut ke Level 6"):
                    naik_level()
            elif langkah3 != "Pilih arah":
                st.warning("Nyasar, coba ulang sayang 😗")
        elif langkah2 != "Pilih arah":
            st.warning("Jalan buntu, coba lagi ya 😘")
    elif langkah1 != "Pilih arah":
        st.warning("Oops, jalan ketutup. Balik lagi yaa 💖")

# ============================
# LEVEL 6 – Love Letter & Lagu
# ============================
elif st.session_state.level == 6:
    st.header("🎶 A Special Song for You")
    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
    st.markdown("> *“Karena kamu tetap yang paling sempurna 💝”*")

    st.header("💌 A Love Letter")
    st.markdown("""
> Hai My Dearest,

Di hari spesialmu ini, aku super excited nyiapin ini semua. Makasih ya udah jadi pendukung, penjaga, dan alasanku senyum setiap hari.

Aku tau aku kadang nyebelin, tapi aku selalu sayang kamu dan itu ga akan terganti. Kamu selalu jadi yang paling *sempurna* di hatiku 💖

Sekali lagi **Happy Birthday, My Love!**  
Semoga semua hal baik dan indah menyertai langkahmu, dan aku bisa terus jadi bagian dari kebahagiaanmu, setiap tahun, setiap waktu.

Love you always 💋
    """)
    st.balloons()
