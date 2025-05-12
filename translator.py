import keyboard
import threading
import time
from googletrans import Translator

translator = Translator()
buffer = ""

def translate_and_replace():
    global buffer
    while True:
        if buffer.endswith("<"):
            phrase = buffer[:-1]  # QUITAR EL GUION
            if phrase:
                try:
                    #LANGUAGES - LENGUAJES
                    # (ES – Español (Spanish) 
                    # EN – Inglés (English) 
                    # DE – Alemán (Deutsch) 
                    # FR – Francés (Français) 
                    # IT – Italiano (Italiano) 
                    # PT – Portugués (Português) 
                    # RU – Ruso (Русский) 
                    # ZH-CN – Chino (中文, Zhōngwén) 
                    # JA – Japonés (日本語, Nihongo) 
                    # KO – Coreano (한국어, Hangugeo) 
                    # AR – Árabe (العربية, 
                    # Al-ʿarabiyyah) 
                    # HI – Hindi (हिन्दी) 
                    # BN – Bengalí (বাংলা) 
                    # NL – Neerlandés (Nederlands) 
                    # SV – Sueco (Svenska) 
                    # FI – Finlandés (Suomi) 
                    # DA – Danés (Dansk) 
                    # NO – Noruego (Norsk))
                    traduccion = translator.translate(phrase, dest='de').text
                    # BORRAR LA FRASE ORIGINAL + EL GUION
                    for _ in range(len(phrase) + 1):
                        keyboard.send("backspace")
                        time.sleep(0.01)
                    keyboard.write(traduccion)
                except Exception as e:
                    print("Error de traducción:", e)
            buffer = ""
        time.sleep(0.2)

threading.Thread(target=translate_and_replace, daemon=True).start()

print("Usa '<' para traducir la frase. Presiona ESC para salir.")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            break
        elif event.name == 'space':
            buffer += ' '
        elif event.name == 'enter':
            buffer += '\n'
        elif event.name == 'backspace':
            buffer = buffer[:-1]
        elif len(event.name) == 1:
            buffer += event.name