import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Happy Birthday baby", page_icon="🎂")

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
    st.title("🎉 Mini Games: Dear My BIrthday Boy")
    st.header("💌 Level 1: Our Anniv Date")
    jawaban1 = st.text_input("Kapan yaa kamu nembak aku? (format: dd-mm)")

    if jawaban1:
        if jawaban1 == "09-11":
            st.success("Yeeeaayy kamu inget!🥹💕 Oke lanjuut sayangg")
            st.balloons()
            time.sleep(3)
st.session_state.level += 1
st.rerun()
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
        time.sleep(3)
st.session_state.level += 1
st.rerun()
# ============================
# LEVEL 3
# ============================
elif st.session_state.level == 3:
    st.header("🎁 Level 3: Choose Your Gift!")
    pilihan_kotak = st.selectbox("Pilih salah satu kotak:", ["Kotak A", "Kotak B", "Kotak C"])

    if st.button("Buka Kotaknya"):
        if pilihan_kotak == "Kotak A":
            st.success("YAYY! Kamu dapet hadiah🎉💝")
            st.balloons()
            st.markdown("> *“Semoga harimu selalu penuh cinta dan selalu bahagia sayangku💖”*")
        elif pilihan_kotak == "Kotak B":
            st.success("Yeayyy! Kamu dapet... xtra kiss 😘")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3NldjQ0Y2U3dm85eG92Z3NybjNidTMxaGRqbGdqazRoemhiaWhvMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tpVKvAabWt3G5csMkT/giphy.gif", caption="Heheh love youu 💞")
        elif pilihan_kotak == "Kotak C":
            st.success("🎁 You can request anything: ")
            st.markdown("> *“What Do You Want From Me??”*")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmdlamVpeXg0eTUydmkxYWxlbzJsbmRucmhhZzZ1MGxja2NhcWFycyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wrBURfbZmqqXu/giphy.gif")

    time.sleep(3)
st.session_state.level += 1
st.rerun()
# ============================
# LEVEL 4
# ============================
elif st.session_state.level == 4:
    st.header("🎈 Level 4: Where Do You want To Go To Celebrate It?")
    pilihan = st.radio(
        "Kamu pilih mana sayangku?",
        ["", "🏠 Di rumah aja, jajan dan nonton sama aku", "🍽️ Romantic Dinner di mana yaa..", "🌌 Jalan-jalan malmingaan, sambil ngopii deh", "🏕️ Just sit in Cafe and..."]
    )

    if pilihan:
        st.success(f"Okeee! Nanti kita {pilihan} yaa sayaang 😍")
        time.sleep(3)
st.session_state.level += 1
st.rerun()
   

# ============================
# LEVEL 5
# ============================
elif st.session_state.level == 5:
    st.header("🌀 Level 5: Love Maze")
    st.write("Escape this maze to meet me!")

    langkah1 = st.selectbox("Langkah 1:", ["Pilih arah", "Kiri", "Kanan"], key="step1")
    if langkah1 == "Kanan":
        langkah2 = st.selectbox("Langkah 2:", ["Pilih arah", "Maju", "Mundur"], key="step2")
        if langkah2 == "Maju":
            langkah3 = st.selectbox("Langkah 3:", ["Pilih arah", "Kanan", "Kiri"], key="step3")
            if langkah3 == "Kiri":
                st.success("YEAYY!! You escaped and met me 😍")
                st.balloons()
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExPWVjZjA1ZTQ3dTB3MTlnd2lsemJ4OHFmZ3RuN2VzdWIwcWhidXlnbmVrNDZsbGhzZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5sokLWDYub7efuAD1M/giphy.gif", caption="Pelukkk 💞")
                st.markdown("> *\"Kamu gabakal tersesat, kan sinyal atara kita 5G \"*")
                if st.button("Lanjut ke Level 6"):
                    naik_level()
            elif langkah1 != "Pilih arah":
                st.warning("Yah nyasar yaang, coba ulang sayang😗")
        elif langkah2 != "Pilih arah":
            st.warning("Jalan buntu, coba pilih lagi babee")
    elif langkah3 != "Pilih arah":
        st.warning("Oops, jalannya ketutup. Semangat sayang sedikiit lagi")

time.sleep(3)
st.session_state.level += 1
st.rerun()

# ============================
# LEVEL 6 – Love Letter & Lagu
# ============================
elif st.session_state.level == 6:
    st.header("The Final Session~")
    st. write("Ini lagu buat kamu... yang paling *sempurna*.. Jangan lupa play lagunya yaa sebelum baca love letternyaa")
    
    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
    st.markdown("> *“I Love You Revan Ar Rafi, my only  love..💝”*")

    st.header("💌 A Love Letter")
    st.markdown("""
> Hai My Dearest,

Selamat Ulang Tahun yaa sayang.. 
Di hari spesial pertamamu sama aku ini, as you know aku super excited buat nyiapin ini semua. Makasih ya udah jadi my supporter, my doctor, my parent, my brother, my everything, especiaallyy karna jadi alasanku senyum in every single day. Glad me to have you in my life..

Semoga di hari spesialmu ini kamu panjang umur, makin sehat, selalu dimudahkan segala urusannya sama Allah. Aku bener bener cant describe how much i love you sayang.. maaf yaa kalo web ini masih jelek heheh aku belum se pro itu walau modal chatgpt hihihih

Sayang.. Aku tau kadang aku nyebelin, tapi aku selalu sayang kamu and it cant be replace for any reason, apapun itu. And i will try my best for you, i will try to be better than be4. Kamu bakal selalu jadi yang paling *sempurna* di hatiku sayang💖

Sekali lagi **Happy Birthday, My Love!**  
Semoga semua hal baik dan indah di dunia ini selalu menyertai langkahmu, dan semoga aku bisa terus jadi bagian dari kebahagiaanmu, setiap tahun, setiap waktu. 

Semoga kita bertahan lama sayangg~~

Love you always 💋
    """)
    st.balloons()
