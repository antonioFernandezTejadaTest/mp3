import mimetypes
import os.path

from glob import glob
from django.http import JsonResponse
from django.http import FileResponse
from django.conf import settings
from pytube import YouTube
from moviepy.editor import VideoFileClip

def obtener_info(url):
    try:
        video = YouTube(url)

        titulo = video.title
        imagen = video.thumbnail_url

    except Exception as e:
        titulo = None
        imagen = None

    return {
        'imagen': imagen,
                         'titulo': titulo
    }

def descargar(url):
    try:
        yt = YouTube(url)

        video_mp4 = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()

        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_app = os.path.abspath(os.path.join(ruta_actual, os.pardir))
        ruta_app = os.path.join(ruta_app, 'Media')
        ruta_app = os.path.join(ruta_app, 'Archivos')

        video_file_name = 'v.mp4'

        video_mp4.download(output_path=ruta_app, filename=video_file_name)

        path_video = os.path.join(ruta_app, video_file_name)

        vfc = VideoFileClip(path_video)

        audio = vfc.audio

        audio_file_name = f"{yt.title}.mp3"

        path_audio = os.path.join(ruta_app, audio_file_name)

        audio.write_audiofile(path_audio, codec='mp3')

        vfc.close()

        os.remove(path_video)

        status = True

    except Exception as e:
        status =  False

    return {
        'status': status
    }

def descargar_file():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_app = os.path.abspath(os.path.join(ruta_actual, os.pardir))
    ruta_app = os.path.join(ruta_app, 'Media')
    ruta_app = os.path.join(ruta_app, 'Archivos')

    archivo = glob(os.path.join(ruta_app, '*.mp3'))[0]

    ruta_app = os.path.abspath(archivo)

    # ruta_app = os.path.join(ruta_app, 'a.mp3')

    mp3 = FileResponse(open(ruta_app, 'rb'), content_type='audio/mpeg')

    return mp3