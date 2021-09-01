import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
hasil = ""
r.pause_threshold = 3

with mic as source:
    print("Mulai bicara")
    rekaman = r.listen(source)
    print("waktu habis")
    
    try:
        hasil = r.recognize_google(rekaman, language = "id-ID")
        print("Kamu bilang:", hasil)
    except sr.UnknownValueError:
        print("Maaf tidak terdeteksi, silahkan coba lagi")
    except Exception as e:
        print(e)

text_file = open("Hasil.txt","w")
text_file.write(hasil)
text_file.close()