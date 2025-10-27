import keyboard
import threading
import time
from googletrans import Translator
import tkinter as tk
from tkinter import ttk

translator = Translator()
buffer = ""
selected_lang = "en"  # idioma por defecto


def translate_and_replace():
    global buffer
    while True:
        if buffer.endswith("<"):  # tecla activadora
            phrase = buffer[:-1]
            if phrase:
                try:
                    traduccion = translator.translate(phrase, dest=selected_lang).text
                    for _ in range(len(phrase) + 1):  # borra texto original + "<"
                        keyboard.send("backspace")
                        time.sleep(0.01)
                    keyboard.write(traduccion)
                except Exception as e:
                    print("Error de traducción:", e)
            buffer = ""
        time.sleep(0.2)


def on_key_event(e):
    global buffer
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "esc":
            print("Saliendo...")
            exit(0)
        elif e.name == "space":
            buffer += " "
        elif e.name == "enter":
            buffer += "\n"
        elif e.name == "backspace":
            buffer = buffer[:-1]
        elif len(e.name) == 1:
            buffer += e.name


def start_key_listener():
    keyboard.hook(on_key_event)
    keyboard.wait()  # mantiene el hilo vivo


def run_gui():
    global selected_lang

    def update_language(event=None):
        nonlocal lang_combobox
        global selected_lang
        selected_lang = lang_dict[lang_combobox.get()]
        print(f"Idioma seleccionado: {lang_combobox.get()} ({selected_lang})")

    root = tk.Tk()
    root.title("Traductor en tiempo real")
    root.geometry("300x180")
    root.resizable(False, False)

    tk.Label(root, text="Selecciona el idioma destino:", font=("Arial", 11)).pack(pady=10)

    lang_dict = {
        "Inglés": "en",
        "Alemán": "de",
        "Francés": "fr",
        "Italiano": "it",
        "Portugués": "pt",
        "Ruso": "ru",
        "Chino (Simplificado)": "zh-cn",
        "Japonés": "ja",
        "Coreano": "ko",
        "Árabe": "ar",
        "Hindi": "hi",
        "Sueco": "sv",
        "Danés": "da",
        "Noruego": "no",
        "Español": "es"
    }

    lang_combobox = ttk.Combobox(root, values=list(lang_dict.keys()), state="readonly")
    lang_combobox.current(0)
    lang_combobox.pack(pady=5)
    lang_combobox.bind("<<ComboboxSelected>>", update_language)

    tk.Label(root, text="Escribe en cualquier ventana\n y usa '<' para traducir", font=("Arial", 10), fg="gray").pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    print("Usa '<' para traducir el texto al idioma seleccionado. Presiona ESC para salir.")

    threading.Thread(target=translate_and_replace, daemon=True).start()
    threading.Thread(target=start_key_listener, daemon=True).start()
    run_gui()
