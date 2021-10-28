import os
import subprocess
import uuid

SUPPORTED_VIDEO_FORMATS = ['mp4']


def save_uploaded_video(video, upload_folder):

    if video.filename == '':
        raise RuntimeError('Video file not sent.')

    if video and supported_file(video.filename):
        _, ext = os.path.splitext(video.filename)
        filename = str(uuid.uuid1()) + ext
        video_path = os.path.join(upload_folder, filename)
        video.save(video_path)
        return video_path
    else:
        raise RuntimeError('Video format not supported.')


def supported_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in SUPPORTED_VIDEO_FORMATS


def check_ffmpeg():
    try:
        subprocess.check_output(['which', 'ffmpeg'])
    except Exception as e:
        print(e, e.output)
