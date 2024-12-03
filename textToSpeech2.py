import edge_tts
import asyncio


async def text_to_speech(text, voice, output_file):
    """使用 Edge TTS 将文本合成为语音"""
    communicate = edge_tts.Communicate(text, voice=voice)
    await communicate.save(output_file)
    print(f"语音已保存到 {output_file}")


# 读取文本文件
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 定义语音
male_voice = "zh-CN-YunyangNeural"  # 中文男声
female_voice = "zh-CN-XiaoxiaoNeural"  # 中文女声


# 异步运行
async def main():
    # 读取文本内容
    text_file_path = "D:/movie/3/b2.txt"  # 替换为你的文本文件路径
    text = read_text_file(text_file_path)

    # 男声朗读
    await text_to_speech(text, male_voice, "D:/movie/3/male_b2.mp3")
    # 女声朗读
    await text_to_speech(text, female_voice, "D:/movie/3/female_b2.mp3")


asyncio.run(main())
