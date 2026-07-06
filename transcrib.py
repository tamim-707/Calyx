# from testvoice import voi
from faster_whisper import WhisperModel
model = WhisperModel("tiny",device = "cpu", compute_type= "int8")
segments , info = model.transcribe("voice.wav")

for segments in segments :
    print (segments.text)

print()
print("Detected language:", info.language)




"""
model = WhisperModel("tiny",device = "cpu", compute_type= "int8")
-Whisper comes in various types, for my laptop tiny is best
-Whisper can run in CPU/GPU
-compute_type controls how AI stores numbers in memory (similar to image like 4k/1080/720/)

segments,info = model.transcrib("voice.wav")
- .trnscrib() is a method means "hey AI,listen to thi audio"
-Calyx record a each voice.wav each time u speak
-Whisper returns two things the spoken text & the extra info .
  segments is for Spoken text and info is for extra info

for segments in segments :
-That segments is a collection of transcription pieces. this loop collect all the pices in segments

print(segments.txt)
-print(segemnet) will return the object itself we need the text of that thats why .text 

"""