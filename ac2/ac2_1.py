import speech_recognition as sr
def escrever_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo: ")
        audio=recognizer.listen(source,timeout=10)
        with open("audio.wav","w",encoding="utf-8") as arquivo:
            arquivo.write(audio)
escrever_audio()
