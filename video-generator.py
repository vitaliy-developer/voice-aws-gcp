import subprocess
# time
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
# end time 

def create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height):
    # Розраховуємо нову ширину, забезпечуючи співвідношення сторін 9:16
    new_width = int(height * 9 / 16)

    # Формуємо команду для FFmpeg
    command = [
        'ffmpeg',
        '-loop', '1',
        '-i', image_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-t', str(duration),
        '-vf', f'scale={new_width}:{height}',  # Встановлюємо нові розміри відео
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_video_path
    ]

    # Запускаємо команду
    subprocess.run(command)

# Параметри
image_path = 'image/image-test.jpg'
audio_path = 'google-mp3/voice-text-google.mp3'
output_video_path = 'generated-video/video.mp4'
duration = time_mp3  # Тривалість відео в секундах
width = 1080
height = 1920

# Створюємо відео з аудіо та новим співвідношенням сторін
create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height)
