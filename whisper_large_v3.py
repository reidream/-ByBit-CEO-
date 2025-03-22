import os
from openai import OpenAI
from faster_whisper import WhisperModel
import time

# OpenAIクライアントの初期化
client = OpenAI(api_key=os.getenv("open_ai_key"))

# Whisper Large v3モデルで音声を文字起こし
print("🔄 Whisper Large v3で音声を処理中...")
model = WhisperModel("large-v3", compute_type="float16")


segments, info = model.transcribe("【世界一盗まれた男】北朝鮮に2200億円をハッキングされた大富豪に独占インタビューしてきました.mp3", beam_size=5)

# 転写結果をテキストにまとめる
transcript_text = "\n".join(segment.text for segment in segments)

# 転写結果をファイルに保存
with open("video_transcript3.md", "w", encoding="utf-8") as file:
    file.write(transcript_text)


# 要約プロンプトの作成関数
def create_prompts(text):
    system_prompt = "あなたは日本語で分かりやすく要約して伝えるプロです。マークダウン形式で回答してください。"
    user_prompt = f"以下はテキストの内容です。簡潔でわかりやすい要約を提供してください。\n\n{text}"

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]


# OpenAIを使って要約を生成する関数
def summarize_with_openai(text):
    try:
        print("🚀 OpenAI APIで要約を生成中...")

        messages = create_prompts(text)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            n=1,
            
        )

        summary = response.choices[0].message.content
        print("✅ 要約生成完了")
        return summary

    except Exception as e:
        print(f"エラー発生: {e}")
        return f"エラー発生: {str(e)}"

with open("video_transcript3.md", mode="r", encoding="utf-8") as file:
    transcript_text = file.read()
# 転写したテキストをGPTで要約
summary_text = summarize_with_openai(transcript_text)

# 要約結果をファイルに保存
with open("video_summary2.md", "w", encoding="utf-8") as file:
    file.write(summary_text)

print("🎉 全ての処理が完了しました！")