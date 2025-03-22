# ドバイ対談：仮想通貨の未来と教育的役割

このリポジトリは、ヒカルとByBit CEO ベン氏によるドバイでの対談に関する文字起こしと要約レポートを含んでいます。

## 概要

人気YouTuberのヒカルが仮想通貨取引所「ByBit」のCEO・ベン氏とドバイで対談し、仮想通貨業界の現状や未来、インフルエンサーの教育的役割について議論した内容をまとめています。

## コンテンツ

このリポジトリには以下のファイルが含まれています：

1. **ボイス文字起こし** - `ボイス写し.md`
   - 対談の完全な文字起こしデータ

2. **要約レポート** - `ヒカル×ByBit CEOベン ドバイ対談レポート.md`
   - 対談内容を整理し、重要なポイントを分かりやすくまとめたレポート

3. **文字起こし処理コード** - `whisper_large_v3.py`
   - 音声データから文字起こしを行うためのPythonスクリプト
   - OpenAIのWhisper Large v3モデルを使用

## 文字起こし処理

音声データの文字起こしには、OpenAIのWhisper Large v3モデルを使用しています。以下のコードで処理を実行しました：

```python
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
```

## 対談の主なトピック

- ByBitの概要と2,200億円のハッキング事件への対応
- ベン氏の経営哲学と危機管理アプローチ
- 仮想通貨の現状と将来性（世界での普及率約5%、日本では10%未満）
- インフルエンサーの教育的役割とステーブルコインの重要性
- 日本市場への展開戦略
- 仮想通貨×ゲームの融合プロジェクト

## 注記

要約レポートはGPT-4o-miniでは短くなりすぎるため、Claude AIを使用して手動で作成しています。より詳細な内容を確認したい場合は、原文の文字起こしファイルをご参照ください。
