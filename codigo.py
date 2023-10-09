# instalar o openai-whisper
# instalar ffmpeg

import whisper

modelo = whisper.load_model("base")

resposta = modelo.transcribe("Gravando2.m4a") #coloque o nome do audio
print(resposta)