from gtts import gTTS

text = "你好，这是一个文本转语音的例子。推荐理由 启发内心成长：这段视频不仅讲述了作者的个人经历，还深入探讨了内在成长的重要性。无论你是在职场奋斗，还是在追求个人梦想，都能从中获得深刻的启示。理解直觉的力量：通过介绍“innsæi”概念，视频揭示了直觉在创造力、同情心和心理敏捷性方面的巨大作用。这对于希望提升个人能力和创新能力的人来说，是一份宝贵的资源。实用的自我提升技巧：视频中提到了冥想和正念练习等方法，帮助人们调节神经系统，提升思维的清晰度。这些方法简单易行，适合任何人尝试。Overall, this video is not only rich in content but also highly inspiring. Whether you're looking to enhance your personal skills or explore new directions for career development, it's well worth watching. It will help you gain a deeper understanding of yourself, uncover your inner strength, and take steps toward a brighter future.总之，这段视频不仅内容丰富，而且富有启发性。无论你是希望提升个人能力，还是寻找职业发展的新方向，都值得一看。它将帮助你更好地理解自己，发现内在的力量，从而迈向更加美好的未来。"
language = "zh"  # 中文

# 生成语音
tts = gTTS(text=text, lang=language, slow=False)
output_file = "D:/movie/voice/gtts_output.mp3"
tts.save(output_file)

print(f"语音已保存到 {output_file}")

import edge_tts
import asyncio


async def text_to_speech():
    text = "你好，这是微软语音合成的示例。推荐理由 启发内心成长：这段视频不仅讲述了作者的个人经历，还深入探讨了内在成长的重要性。无论你是在职场奋斗，还是在追求个人梦想，都能从中获得深刻的启示。理解直觉的力量：通过介绍“innsæi”概念，视频揭示了直觉在创造力、同情心和心理敏捷性方面的巨大作用。这对于希望提升个人能力和创新能力的人来说，是一份宝贵的资源。实用的自我提升技巧：视频中提到了冥想和正念练习等方法，帮助人们调节神经系统，提升思维的清晰度。这些方法简单易行，适合任何人尝试。激励改变：作者通过自己的故事，鼓励观众勇敢面对内心的呼唤，勇于改变现状。这对于那些在职业生涯或生活中感到迷茫的人，是一种极大的鼓舞。丰富的案例分享：视频中提到了海洋探险家 Enric Sala 的成功案例，展示了如何通过内观和直觉取得显著成就。这些真实的故事具有很强的感染力，能够激发观众的共鸣和行动力。总之，这段视频不仅内容丰富，而且富有启发性。无论你是希望提升个人能力，还是寻找职业发展的新方向，都值得一看。它将帮助你更好地理解自己，发现内在的力量，从而迈向更加美好的未来。"
    output_file = "D:/movie/voice/edge_output.mp3"

    # 初始化 Edge TTS
    communicate = edge_tts.Communicate(text, voice="zh-CN-XiaoxiaoNeural")  # 中文女声
    await communicate.save(output_file)

    print(f"语音已保存到 {output_file}")


# 异步运行
asyncio.run(text_to_speech())

import pyttsx3

text = "你好，这是一个离线语音合成的例子。推荐理由 启发内心成长：这段视频不仅讲述了作者的个人经历，还深入探讨了内在成长的重要性。无论你是在职场奋斗，还是在追求个人梦想，都能从中获得深刻的启示。理解直觉的力量：通过介绍“innsæi”概念，视频揭示了直觉在创造力、同情心和心理敏捷性方面的巨大作用。这对于希望提升个人能力和创新能力的人来说，是一份宝贵的资源。实用的自我提升技巧：视频中提到了冥想和正念练习等方法，帮助人们调节神经系统，提升思维的清晰度。这些方法简单易行，适合任何人尝试。激励改变：作者通过自己的故事，鼓励观众勇敢面对内心的呼唤，勇于改变现状。这对于那些在职业生涯或生活中感到迷茫的人，是一种极大的鼓舞。丰富的案例分享：视频中提到了海洋探险家 Enric Sala 的成功案例，展示了如何通过内观和直觉取得显著成就。这些真实的故事具有很强的感染力，能够激发观众的共鸣和行动力。总之，这段视频不仅内容丰富，而且富有启发性。无论你是希望提升个人能力，还是寻找职业发展的新方向，都值得一看。它将帮助你更好地理解自己，发现内在的力量，从而迈向更加美好的未来。"

# 初始化引擎
engine = pyttsx3.init()

# 设置参数
engine.setProperty('rate', 150)  # 语速
engine.setProperty('volume', 1.0)  # 音量 (0.0 - 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 设置语音（0为默认）

# 合成语音
engine.save_to_file(text, 'D:/movie/voice/pyttxs3_output.wav')
engine.runAndWait()

print("语音已保存到 output.wav")
