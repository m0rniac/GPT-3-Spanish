#[GPT-3; Español].
import os
from os import system
from colorama import *
from util import esp_trans
import speech_recognition
import pyttsx3
import openai

init()
detect_sys = os.name

#[Corpus; Limpieza de ventana].
if detect_sys == 'posix':
    system('clear')
else:
    system('cls')

#[Corpus; Credenciales].
openai.api_key = '[OpenAI-Key]'

#[Corpus; Main].
recognizer = speech_recognition.Recognizer()
print(Back.BLACK + Fore.YELLOW + Style.BRIGHT)
print("[GPT-3; Inteligencia Artificial].")

print(Back.BLACK + Fore.CYAN + Style.BRIGHT)
print("                                                                                     [Reconocimiento de voz; " + Back.BLACK + Fore.RED + Style.BRIGHT + "Activado" + Back.BLACK + Fore.CYAN + Style.BRIGHT + "].")


#[Corpus; Creación de proceso en bucle].
while True:
    try:
        #[subCorpus; Preparación de micrófono].
        with speech_recognition.Microphone() as mic:

            #[subCorpus; Creación de entrada].
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            #[subCorpus; Preparación de traducción]
            s1 = recognizer.recognize_google(audio, language='es-ES')
            s2 = esp_trans("es", "en", s1)
            SpeechText = s2.lower()

            #[subCorpus; Preset para tecnología GPT-3].
            myPrompt = """
            The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
            Human: Hello, who are you?
            AI: I am an AI created by OpenAI. How can I help you today?
            Human:{SpeechText}
            AI:"""


            #[subCorpus; Parámetros GPT-3].
            start_sequence = "\nAI:"
            restart_sequence = "\nHuman: "
            Addon = "\n"

            #[subCorpus; Creación de motor GPT-3].
            response = openai.Completion.create(
                engine="davinci",
                temperature=0.9,
                max_tokens=900,
                top_p=1,
                prompt = str(myPrompt.replace("{SpeechText}", SpeechText)),
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", "Human:", "AI:"]
            )
            
            #[subCorpus; Resultados de proceso primario].
            prompt = myPrompt.replace("{SpeechText}", SpeechText),
            lan = f'Human:{SpeechText}\nAI:{response.choices[0].text}'
            lan2 = esp_trans("en", "es", lan)

            print(Back.BLACK + Fore.GREEN + Style.BRIGHT)
            print(lan2)

            #[subCorpus; Preparación de traducción final].
            m = str(response.choices[0].text)
            m2 = m.replace(".", "")
            m3 = esp_trans("en", "es", m2)

            print(Back.BLACK + Fore.CYAN + Style.BRIGHT)
            print("[GPT-3]: " + m3)

            #[subCorpus; Creación de lector].
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 130)
            volume = engine.getProperty('volume')
            engine.setProperty('volume', 70.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(m3)
            engine.runAndWait()

    except speech_recognition.UnknownValueError:
        print(Back.BLACK + Fore.RED + Style.BRIGHT)
        print("[Orson]: Sin comprensión a lo dicho.")
        recognizer = speech_recognition.Recognizer()