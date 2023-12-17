from gtts import gTTS
import boto3
import os
import time

start_time = time.time()  # Запам'ятовуємо час початку виконання скрипта

input_file_path = 'aws-text/text-Polly.txt'
output_file_path = 'aws-mp3/voice-text-Polly.mp3'

# Зчитати текст з файлу
with open(input_file_path, 'r') as file:
    text = file.read()

# Створити Amazon Polly об'єкт
region = 'eu-central-1'  # Змініть регіон на той, який ви хочете використовувати
polly = boto3.client('polly', region_name=region)

# Визначити мову та голос
language = 'en-US'
voice_id = 'Joanna'  # Вибрано голос, який підтримує ядро 'neural'

# Синтез мовлення за допомогою Amazon Polly
print("Розпочато синтез мовлення...")
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId=voice_id,
    LanguageCode=language,
    Engine='neural'  # Вказати ядро 'neural'
)
print("Завершено синтез мовлення.")

# Зберегти аудіофайл
print("Запис аудіофайлу...")
with open(output_file_path, 'wb') as file:
    file.write(response['AudioStream'].read())
print(f"Запис аудіофайлу завершено. Збережено в '{output_file_path}'.")

end_time = time.time()  # Запам'ятовуємо час завершення виконання скрипта
execution_time = end_time - start_time  # Обчислюємо час виконання

print(f"Час виконання скрипта: {execution_time} секунд.")
