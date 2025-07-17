import streamlit as st
import random

st.set_page_config(page_title="Birthday Quest 💖", page_icon="🎂")

# ============================
# Session State untuk Level
# ============================
if "level" not in st.session_state:
    st.session_state.level = 1

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
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3NldjQ0Y2U3dm85eG92Z3NybjNidTMxaGRqbGdqazRoemhiaWhvMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tpVKvAabWt3G5csMkT/giphy.gif", caption="Heheh love youu 💞")
        elif pilihan_kotak == "Kotak C":
            st.success("🎁 You can request anything: ")
            st.markdown("> *“What Do You Want From Me??”*")

    if st.button("Lanjut ke Level 4"):
        naik_level()

# ============================
# LEVEL 4
# ============================
elif st.session_state.level == 4:
    st.header("🎈 Level 4: Coming Soon or Fill This?")
    st.write("Level ini masih kosong dulu yaa... atau kamu bisa pilih ini:")

    pilihan = st.radio(
        "Kalau kamu harus pilih salah satu tempat rayain ulang tahun, kamu pilih yang mana?",
        ["", "🏠 Di rumah aja", "🍽️ Dinner romantis", "🌌 Liat bintang bareng", "🏕️ Duduk santai di cafe"],
        index=0
    )

    if pilihan:
        st.success(f"Okeee! Nanti kita {pilihan} yaa sayaang 😍")
        if st.button("Lanjut ke Level 5"):
            naik_level()
    else:
        if st.button("Lewati duluu & lanjut ke Level 5"):
            naik_level()

# ============================
# LEVEL 5 – Love Maze (Dropdown version)
# ============================
elif st.session_state.level == 5:
    st.header("🌀 Level 5: Love Maze")
    st.write("Kamu ada di labirin cinta, cari jalan ke akuuu 💘")

    langkah1 = st.selectbox("Langkah 1: Mau ke mana dulu?", ["Pilih arah", "Kiri", "Kanan"], key="step1")
    if langkah1 == "Kanan":
        langkah2 = st.selectbox("Langkah 2: Terus ke mana lagi?", ["Pilih arah", "Maju", "Mundur"], key="step2")
        if langkah2 == "Maju":
            langkah3 = st.selectbox("Langkah 3: Satu langkah terakhir!", ["Pilih arah", "Kanan", "Kiri"], key="step3")
            if langkah3 == "Kiri":
                st.success("YEAYY!! Kamu berhasil keluar dari labirin dan nemuin akuuu😍💕")
                st.balloons()
                st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dTB3MTlnd2lsemJ4OHFmZ3RuN2VzdWIwcWhidXlnbmVrNDZsbGhzZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5sokLWDYub7efuAD1M/giphy.gif", caption="Pelukk ahhh~ 💞")
                st.markdown("> *\"Cintaku nggak pernah tersesat, karena jalannya selalu menuju kamu 💖\"*")
                st.snow()
                if st.button("Oke lanjut sayaang"):
                    naik_level()
            elif langkah3 != "Pilih arah":
                st.warning("Wah kamu nyasar, balik lagi yaa dari awal~ 🌀")
        elif langkah2 != "Pilih arah":
            st.warning("Aduh... jalan buntu, coba arah lain yaa 😢")
    elif langkah1 != "Pilih arah":
        st.warning("Oops! Jalan itu ketutup semak-semak cinta~ 🌿 Balik lagi ya 😘")

# ============================
# LEVEL 6 – Lagu + Surat Cinta
# ============================
elif st.session_state.level == 6:
    st.header("🎶 ")
    st.write("Ini lagu buat kamu... yang paling *sempurna* 💖. Jangan Lupa nyalain lagunya untuk dengerin sambil baca love letternya yaaa")
    st.video("https://www.youtube.com/watch?v=Y3eFGpL1q7M")
    st.markdown("> *“Karena kamu yang terbaik, dan tetap sempurna di mataku 💝”*")

    st.header("💌 A Love Letter")
    st.markdown("""
    > Hai My Dearest,

    Di hari spesial pertamamu ini sama aku, I just want to say thaat im so excited untuk nyiapin ini semuaaa. As you know aku adalah orang yang paling ga sabar nunggu ulang tahun kamu. Makasih ya udah jadi my supporter, my guard, and especially for always be my reason to smile everydayy.

    Aku tau kadang aku nyebelin, kadang suka susah dimengerti sama kamu. Tapi aku selalu sayang sama kamu koo sayaang, and it cant be replace. Kamu bakal selalu jadi yang paling *sempurna* di hatiku💖

    Sekali lagi **Happy Birthday, My Love!**  
    Semoga semua hal baik dan indah selalu menyertai langkahmu. Dan semoga aku selalu bisa jadi bagian dari kebahagiaan kamu, setiap tahun, setiap waktu.

    Love you always my baby💋
    """)
    st.balloons()
