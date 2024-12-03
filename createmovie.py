from moviepy import ImageClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips

# Configuration
audio_file = "D:/movie/3/male_b1.mp3"
image_files = [
    "D:/movie/image/15.jpg",
    "D:/movie/image/21.jpg",
    "D:/movie/image/22.jpg",
    "D:/movie/image/32.jpg",
    "D:/movie/image/16.jpg",
    "D:/movie/image/30.jpg",

]
output_video = "D:/movie/3/jeff/b1.mp4"

# Image duration (seconds)
image_duration = 2
additional_time = 1  # Additional time in seconds to extend the video by 2 seconds

# Create video clips for all images
clips = [ImageClip(img, duration=image_duration).resized(height=720) for img in image_files]

# Add additional blank clip to extend video duration by 2 seconds
additional_clip = ImageClip(image_files[-1], duration=additional_time).resized(height=720)  # Use the last image
clips.append(additional_clip)

# Concatenate all clips into a single video
video = concatenate_videoclips(clips, method="compose")

# Load audio and ensure its length is compatible with video length
audio = AudioFileClip(audio_file)

# Add audio to the video
video = video.with_audio(audio)

# Export the final video
video.write_videofile(output_video, fps=24, codec="libx264", audio_codec="aac")

print(f"视频已成功保存到 {output_video}")
