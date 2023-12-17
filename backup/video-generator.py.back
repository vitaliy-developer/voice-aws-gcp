import subprocess

def create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height):
    # Формуємо команду для FFmpeg
    command = [
        'ffmpeg',
        '-loop', '1',  # Повторюємо зображення
        '-i', image_path,  # Шлях до зображення
        '-i', audio_path,  # Шлях до аудіофайлу
        '-c:v', 'libx264',
        '-t', str(duration),  # Тривалість відео в секундах
        '-s', f'{width}x{height}',  # Розміри відео
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',  # Кодек аудіо
        '-strict', 'experimental',  # Включаємо підтримку aac
        output_video_path
    ]

    # Запускаємо команду
    subprocess.run(command)

# Параметри
image_path = 'image/image-test.jpg'
audio_path = 'google-mp3/voice-text-google.mp3'
output_video_path = 'generated-video/video.mp4'
duration = 20  # Тривалість відео в секундах
width = 1080
height = 1920

# Створюємо відео з аудіо
create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height)
