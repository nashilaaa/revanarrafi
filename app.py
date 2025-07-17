import streamlit as st
import random

st.set_page_config(page_title="Birthday Quest 💖", page_icon="🎂")

# Judul aplikasi
st.title("🎉 Birthday Quest: Love Level Challenge")
st.write("Selamat ulang tahun sayang! 🥰 Yuk selesaikan tantangan cinta ini dulu yaa~")

# LEVEL 1
st.header("💌 Level 1: Tebak Tanggal Jadian")
jawaban1 = st.text_input("Kapan kita jadian? (format: dd-mm)")

if jawaban1:
    if jawaban1 == "14-02":  # Ganti sesuai tanggal jadian kamu
        st.success("Waaah kamu inget banget! 🥹💕 Yuk lanjut ke level 2!")

        # LEVEL 2
        st.header("🧠 Level 2: Kuis Cinta")
        q2 = st.radio("Kalau aku marah, biasanya kamu ngapain?", 
                      ["Biarin dulu", "Peluk aku", "Beliin makanan", "Ngilang 😭"])

        if q2:
            if q2 == "Beliin makanan":
                st.success("Haha makanan emang penyelamat segalanya 🍕💕")
                
                # LEVEL 3
                st.header("🎁 Level 3: Pilih Kotak Hadiah")
                pilihan_kotak = st.selectbox("Pilih salah satu kotak:", 
                                             ["Kotak A", "Kotak B", "Kotak C"])
                if st.button("Buka Kotaknya"):
                    kotak_berisi = random.choice(["Kotak A", "Kotak B", "Kotak C"])
                    if pilihan_kotak == kotak_berisi:
                        st.balloons()
                        st.success("YAYY! Kamu dapat hadiah istimewa 🎉")
                        st.markdown("> *“Selamat ulang tahun cintaku! Semoga harimu penuh cinta dan tawa. Aku beruntung banget punya kamu 💖”*")
                    else:
                        st.warning("Yahh belum ketemu hadiahnya 😢 Tapi cintaku nggak random kok, selalu buat kamu~ 😚")

                # FINAL: Pilih tempat perayaan
                st.header("🎈 Pilih Tempat Rayain Ulang Tahun")
                tempat = st.radio("Kamu mau rayain ulang tahunnya di mana nih?", 
                                  ["🏠 Di rumah aja, sambil ngbrol tapi ada yang recokin",
                                   "🍽️ Romantic Dinner",
                                   "🌌 Jalan-jalan, malmingan",
                                   "🏕️ Rayain di cafe"])

                if tempat:
                    st.success(f"Okeee! Nanti kita {tempat.split(' ')[1]} ya sayang 😍")
                    st.snow()
                    st.markdown("## 🥂 Cheers for You!")
                    st.write("Terima kasih udah main sampai akhir. Aku cinta kamu selalu 💕")

            else:
                st.warning("Hehe coba pikir lagi... makanan kan favorit kamu 🥺")
    else:
        st.warning("Bukan itu sayang 😗 coba ingat-ingat lagiii~")
