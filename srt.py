import speech_recognition as sr
from pydub import AudioSegment

# Завантажте аудіофайл
audio_file_path = "google-mp3/voice-text-google.mp3"
audio = AudioSegment.from_file(audio_file_path, format="mp3")

# Визначте інтервали для розпізнавання мови (наприклад, кожні 10 секунд)
interval = 10000  # мілісекунди
chunks = [audio[i:i + interval] for i in range(0, len(audio), interval)]

# Використовуйте SpeechRecognition для розпізнавання мови
recognizer = sr.Recognizer()
subtitles = []

for i, chunk in enumerate(chunks):
    chunk.export("subtitles-srt/temp.wav", format="wav")
    with sr.AudioFile("subtitles-srt/temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="uk-UA")  # Змініть на відповідну мову
            start_time = i * (interval / 1000)  # Початковий час у секундах
            end_time = (i + 1) * (interval / 1000)  # Закінчений час у секундах
            subtitles.append(f"{i + 1}\n{start_time:.3f} --> {end_time:.3f}\n{text}\n")
        except sr.UnknownValueError:
            subtitles.append(f"{i + 1}\n{start_time:.3f} --> {end_time:.3f}\nРозпізнавання не вдалося\n")

# Збережіть субтитри у файл у форматі SRT
srt_file_path = "subtitles-srt/subtitles.srt"
with open(srt_file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(subtitles))

print(f"Субтитри збережено у файл {srt_file_path}")