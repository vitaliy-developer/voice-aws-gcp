import subprocess
from pydub import AudioSegment
from PIL import Image

def get_duration(file_path):
    audio = AudioSegment.from_mp3(file_path)
    duration_in_seconds = round(len(audio) / 1000)
    return duration_in_seconds

def resize_and_pad_image(input_path, output_path, target_width, target_height):
    original_image = Image.open(input_path)
    
    # Розраховуємо нові розміри
    new_width = target_width
    new_height = int(target_width / original_image.width * original_image.height)

    # Змінюємо розміри та отримуємо середній колір
    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    average_color = get_average_color(resized_image)

    # Заповнюємо область заливкою середнього кольору
    padded_image = Image.new('RGB', (target_width, target_height), average_color)
    padded_image.paste(resized_image, ((target_width - new_width) // 2, (target_height - new_height) // 2))
    padded_image.save(output_path)

def get_average_color(image):
    pixels = list(image.getdata())
    red = sum([pixel[0] for pixel in pixels]) // len(pixels)
    green = sum([pixel[1] for pixel in pixels]) // len(pixels)
    blue = sum([pixel[2] for pixel in pixels]) // len(pixels)
    return (red, green, blue)

if __name__ == "__main__":
    mp3_file_path = "google-mp3/voice-text-google.mp3"
    duration = get_duration(mp3_file_path)
    print(duration)

    time_mp3 = duration

def create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height):
    # Розраховуємо нову ширину та висоту для співвідношення сторін 9:16
    new_width = int(height * 9 / 16)

    # Змінюємо розміри зображення та отримуємо середній колір
    resized_image_path = 'image/resized-image.jpg'
    resize_and_pad_image(image_path, resized_image_path, new_width, height)

    # Формуємо команду для FFmpeg
    command = [
        'ffmpeg',
        '-loop', '1',
        '-i', resized_image_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-t', str(duration),
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
duration = time_mp3
width = 1080
height = 1920

# Створюємо відео з аудіо та новим співвідношенням сторін
create_video_with_audio(image_path, audio_path, output_video_path, duration, width, height)
