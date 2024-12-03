import subprocess

def burn_subtitles(video_path, srt_path, output_path):
    try:
        # Convert backslashes to forward slashes for FFmpeg
        video_path = video_path.replace("\\", "/")
        srt_path = srt_path.replace("\\", "/")
        output_path = output_path.replace("\\", "/")

        # FFmpeg command
        command = [
            "ffmpeg",
            "-i", video_path,
            "-vf", f"subtitles='{srt_path}':force_style='FontName=Arial,FontSize=20,PrimaryColour=&H00FFA500,Bold=1'",
            "-c:v", "libx264",  # Re-encode using H.264 for compatibility
            "-c:a", "copy",     # Copy audio without re-encoding
            output_path
        ]

        # Execute command
        subprocess.run(command, check=True)
        print("Subtitles burned successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Paths
video_file = r"D:/movie/3/7TWKKww-F30.mp4"  # Your video file
subtitle_file = r"D:/movie/3/2.srt"         # Your subtitle file
output_file = r"D:/movie/3/jeff.mp4"        # Your output file

burn_subtitles(video_file, subtitle_file, output_file)
