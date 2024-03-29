from pydub import AudioSegment

def get_duration(file_path):
    audio = AudioSegment.from_mp3(file_path)
    duration_in_seconds = round(len(audio) / 1000)  # переводимо мілісекунди в секунди та заокруглюємо
    return duration_in_seconds

if __name__ == "__main__":
    mp3_file_path = "google-mp3/voice-text-google.mp3"  # або вкажіть повний шлях до вашого файлу
    duration = get_duration(mp3_file_path)
    print(duration)

    # Зберігаємо отриманий час у змінну
    time_mp3 = duration

    # print("Змінна time_mp3 має значення:", time_mp3)
