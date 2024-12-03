
import speech_recognition as sr
import requests
import os

from moviepy import VideoFileClip, TextClip, CompositeVideoClip


# 配置
video_path = 'input_video.mp4'
output_video_path = 'output_video_with_subtitles.mp4'
api_key = 'YOUR_TRANSLATION_API_KEY'

# 1. 读取视频并提取音频
clip = VideoFileClip(video_path)
audio_path = 'temp_audio.wav'
clip.audio.write_audiofile(audio_path)

# 2. 将音频转换为文本
recognizer = sr.Recognizer()
with sr.AudioFile(audio_path) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language='en-US')

print(f"Recognized text: {text}")

# 3. 调用翻译接口将英文翻译成中文
def translate_text(text, api_key):
    url = 'https://api.example.com/translate'  # 替换为实际的翻译API URL
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'source_language': 'en',
        'target_language': 'zh'
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['translated_text']
    else:
        raise Exception(f"Translation failed: {response.status_code}, {response.text}")

translated_text = translate_text(text, api_key)
print(f"Translated text: {translated_text}")

# 4. 将中文字幕添加到视频的每一帧
def add_subtitles_to_video(video_path, translated_text, output_video_path):
    clip = VideoFileClip(video_path)
    duration = clip.duration

    # 创建字幕
    txt_clip = TextClip(translated_text, fontsize=24, color='white')
    txt_clip = txt_clip.set_pos('bottom').set_duration(duration)

    # 合成视频和字幕
    video_with_subtitles = CompositeVideoClip([clip, txt_clip])
    video_with_subtitles.write_videofile(output_video_path, codec='libx264')

add_subtitles_to_video(video_path, translated_text, output_video_path)

# 清理临时文件
os.remove(audio_path)