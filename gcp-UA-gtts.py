from gtts import gTTS
import os
import time

start_time = time.time()  # Запам'ятовуємо час початку виконання скрипта

input_file_path = 'text-gtts.txt'
output_file_path = 'voice-text-google.mp3'

# Зчитати текст з файлу
with open(input_file_path, 'r') as file:
    text = file.read()

# Створити gTTS об'єкт
tts = gTTS(text, lang='uk')  # Змініть 'ru' на код вашої мови, якщо потрібно

# Зберегти аудіофайл
tts.save(output_file_path)
print(f"Запис аудіофайлу завершено. Збережено в '{output_file_path}'.")

end_time = time.time()  # Запам'ятовуємо час завершення виконання скрипта
execution_time = end_time - start_time  # Обчислюємо час виконання

print(f"Час виконання скрипта: {execution_time} секунд.")
