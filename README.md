# Pico - Dominican Phonetic Spanglish SSML & Audio Generator

`pico.py` is a Python command-line tool that converts Spanish/English input text into Dominican phonetic Spanglish with SSML formatting and generates an audio file using gTTS (Google Text-to-Speech).

---

## Wiki Sections

### 1. Overview

Pico transforms normal Spanish/English text into a vibrant Dominican Spanglish style, mimicking local slang, dropping some consonants, elongating vowels, and mixing in English phonetics. The output includes:

- **SSML-formatted text** with natural pauses for speech synthesis engines that support SSML
- **An MP3 audio file** generated with Google Text-to-Speech (basic pronunciation, without SSML effects)

This tool is ideal for:

- Creating Caribbean-flavored TTS demos  
- Fun phonetic experiments  
- Linguistic style emulation  

---

### 2. Installation & Usage

#### Requirements

- Python 3.6+  
- `gTTS` library  

Install dependencies with:

```bash
pip install gTTS
```

#### Running Pico

Run the script via command line with text input:

```bash
python pico.py "Tu texto aquÃ­"
```

Or launch without arguments and enter text interactively:

```bash
python pico.py
```

The output will:

- Print the SSML version of your Dominican Spanglish text  
- Save an MP3 audio file named `pico_output.mp3` in the current directory  

---

### 3. Slang & Features

- Drops or replaces final consonants (`r`, `s`, `d`) to mimic Dominican speech  
- Randomly elongates vowels for a laid-back effect  
- Replaces common words with Dominican slang (e.g., `amigo` â `frenn`, `reuniÃ³n` â `meeting`)  
- Incorporates English words with phonetic spelling (e.g., `maybe` â `maaaaaybe`)  
- Includes additional slang like "explain" â "explaine"  
- Inserts `<break time="XXXms"/>` pauses in SSML output for natural rhythm  
- Generates an audio file using Google TTS (without SSML pauses)  

---

If you want to contribute slang or improve the script, please open an issue or pull request!
