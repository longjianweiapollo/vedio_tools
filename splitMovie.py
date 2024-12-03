from moviepy.video.io.VideoFileClip import VideoFileClip
import os


def split_video(input_file, output_folder):
    # Load the video file
    video = VideoFileClip(input_file)

    # Calculate duration of each split
    total_duration = video.duration
    split_duration = total_duration / 2  # Duration of each split

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Generate the 10 video parts
    for i in range(2):
        start_time = i * split_duration
        end_time = min(start_time + split_duration, total_duration)  # Handle rounding issues

        # Create the subclip
        subclip = video.subclipped(start_time, end_time)  # Using subclipped instead of subclip

        # Write the subclip to a file
        output_file = os.path.join(output_folder, f"part_{i + 1}.mp4")
        subclip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Saved: {output_file}")

    video.close()


# Input video and output folder
input_file = "D:/movie/3/jeff2.mp4"
output_folder = "D:/movie/jeff"

# Call the function to split the video
split_video(input_file, output_folder)
