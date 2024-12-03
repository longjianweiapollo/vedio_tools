from moviepy import VideoFileClip, concatenate_videoclips

# 配置文件路径
video_file1 = "D:/movie/3/jeff/b1.mp4"  # 第一个视频文件路径
video_file2 = "D:/movie/3/jeff/part_2.mp4"  # 第二个视频文件路径
video_file3 = "D:/movie/3/jeff/b2.mp4"
output_video = "D:/movie/3/jeff/jeff2.mp4"  # 输出视频文件路径

# 加载视频文件
video1 = VideoFileClip(video_file1)
video2 = VideoFileClip(video_file2)
video3 = VideoFileClip(video_file3)
# 拼接视频
final_video = concatenate_videoclips([video1, video2,video3 ], method="compose")

# 导出最终视频
final_video.write_videofile(output_video, fps=24, codec="libx264", audio_codec="aac")

print(f"视频已成功保存到 {output_video}")
