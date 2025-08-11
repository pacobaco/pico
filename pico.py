import random
import re
import sys
from gtts import gTTS

def drop_final_consonants(word):
    if re.search(r'[rsd]$', word):
        if word.endswith('r'):
            return word[:-1] + "’"
        elif word.endswith('s'):
            return word[:-1] + ("’" if random.random() > 0.5 else "h")
        elif word.endswith('d'):
            return word[:-1]
    return word

def elongate_vowels(word):
    vowels = "aeiou"
    new_word = ""
    for char in word:
        new_word += char
        if char in vowels and random.random() > 0.6:
            new_word += char * random.randint(1, 4)
    return new_word

def slang_replace(word):
    slang_dict = {
        # Spanish slang
        "amigo": "frenn",
        "hermano": "bro",
        "cosa": "vaina",
        "oficina": "oficinaaa",
        "reunión": "meeting",
        "tráfico": "tapón",
        "colmadito": "colmadito",
        "pero": "peeerooo",
        "tarde": "tar’deee",
        "antes": "befóóóóre",
        "tal vez": "maybe",
        "estaba": "es-taaaaba",
        "bien": "bieeeen",
        "entendiendo": "entendiendo",
        "usted": "tú",
        "qué": "qué",
        "yo": "yo",
        "sí": "sí",
        "uno": "uno",
        "dos": "dos",
        "tres": "tres",
        "gente": "manada",
        "dinero": "plata",
        "trabajo": "joba",
        "fiesta": "jangueo",
        "bailar": "bailao’",
        "bebida": "chela",
        "explicar": "explaine",
        "explain": "explaine",
        "explanation": "explaine’",
        # English phonetics
        "meeting": "meetin’",
        "style": "styyle",
        "fix": "fix",
        "maybe": "maaaaaybe",
        "before": "befóóóóre",
        "brother": "broooo",
        "friend": "frenn",
        "party": "jangueo",
        "cool": "kool",
        "money": "plata",
        "work": "joba",
        "car": "carro",
        "hello": "eyyy",
        "yes": "yaas",
        "no": "noo",
    }
    lw = word.lower()
    if lw in slang_dict:
        if word[0].isupper():
            return slang_dict[lw].capitalize()
        else:
            return slang_dict[lw]
    return word

def dominican_spanglish_ssml(text):
    words = text.split()
    ssml_parts = []
    for w in words:
        w = drop_final_consonants(w)
        w = slang_replace(w)
        w = elongate_vowels(w)
        ssml_parts.append(w)
        
        if random.random() > 0.7:
            pause = random.choice([300, 400, 500, 600])
            ssml_parts.append(f'<break time="{pause}ms"/>')
    ssml_text = " ".join(ssml_parts)
    return f"<speak>{ssml_text}</speak>"

def dominican_spanglish_plain(text):
    words = text.split()
    transformed = []
    for w in words:
        w = drop_final_consonants(w)
        w = slang_replace(w)
        vowels = "aeiou"
        new_word = ""
        for char in w:
            new_word += char
            if char in vowels and random.random() > 0.8:
                new_word += char * random.randint(1, 2)
        transformed.append(new_word)
    return " ".join(transformed)

def main():
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = input("Enter text for Pico to convert:\n")
    
    ssml = dominican_spanglish_ssml(input_text)
    plain_text = dominican_spanglish_plain(input_text)
    
    tts = gTTS(text=plain_text, lang='es')
    audio_file = "pico_output.mp3"
    tts.save(audio_file)
    
    print("\nPico SSML Output:\n")
    print(ssml)
    print(f"\nAudio file saved as: {audio_file}")
    print("Play the audio file to hear Dominican phonetic Spanglish pronunciation (basic, no SSML effects).")

if __name__ == "__main__":
    main()
