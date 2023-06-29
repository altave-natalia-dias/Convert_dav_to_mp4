import os
import time
from moviepy.editor import VideoFileClip

def convert_dav_to_mp4(dav_file):
    mp4_file = os.path.splitext(dav_file)[0] + ".mp4"
    video_clip = VideoFileClip(dav_file)
    video_clip.write_videofile(mp4_file)
    video_clip.close()

def process_downloads_folder():
    downloads_folder = os.path.expanduser("~/Downloads")
    processed_files = set()

    while True:
        files = os.listdir(downloads_folder)
        for file in files:
            if file.endswith(".dav") and file not in processed_files:
                print("Converting:", file)
                try:
                    convert_dav_to_mp4(os.path.join(downloads_folder, file))
                    processed_files.add(file)
                    print("Conversion completed.")
                except Exception as e:
                    print("Error occurred during conversion:", str(e))

        time.sleep(10)  # Espera 10 segundos antes de verificar novamente

# Chama a função principal para iniciar o monitoramento
process_downloads_folder()

