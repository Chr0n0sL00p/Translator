Real-time Translator

A Python tool that lets you translate text in real time from any window or application (browser, chat, document, etc.).
Simply type your phrase, then press < to instantly replace it with the translated text in the language you selected from the app’s interface.

The program runs quietly in the background and supports multiple languages (English, German, French, Italian, Portuguese, Russian, Chinese, Japanese, Korean, Arabic, Hindi, and more).

Features

Works system-wide — translate text anywhere.

Simple graphical interface to select the target language.

Real-time translation using Google Translate.

Lightweight and non-intrusive background threads.

Hotkey-based activation (< by default).

Installation

Make sure you have Python 3.11 or 3.12 installed (recommended for compatibility).
Then open a terminal (PowerShell or CMD) and run:

pip install keyboard
pip install googletrans==4.0.0-rc1


If you are using Python 3.13 or later, googletrans may not work due to deprecated modules.
In that case, use deep-translator instead:

pip install keyboard deep-translator

Usage

Run the script:

python translator.py


Select your target language from the dropdown menu.

Type in any window (e.g., Google, WhatsApp Web, Word, etc.).

Press < to translate your last phrase.

The original text will be automatically replaced with the translation.

Example
I like to learn languages< → becomes Ich lerne gerne Sprachen

Requirements

Python 3.11 or 3.12

Internet connection

Packages:

keyboard

googletrans==4.0.0-rc1 (or deep-translator for newer Python versions)