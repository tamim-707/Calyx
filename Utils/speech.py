import os
import soundfile as sf
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("tiny", device="cpu", compute_type="int8")

def speech_to_text():

    sample_rate = 16000

    # Looks like the user is speaking naturally
    print("You: ", end="", flush=True)

    audio_data = []
    is_speaking = False
    silent_chunks = 0
    SILENT_LIMIT = 30

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    ) as stream:

        while True:
            data, overflowed = stream.read(1024)
            volume = np.abs(data).mean()

            if volume > 0.02:
                if not is_speaking:
                    is_speaking = True

                # Reset silence timer whenever voice is heard
                silent_chunks = 0

            elif is_speaking:
                silent_chunks += 1

            # Save audio only after speech starts
            if is_speaking:
                audio_data.append(data)

            # Stop after enough silence
            if is_speaking and silent_chunks >= SILENT_LIMIT:
                break

    audio = np.concatenate(audio_data, axis=0)
    sf.write("voice.wav", audio, sample_rate)

    # Speech → Text
    segments, info = model.transcribe("voice.wav")

    text = ""

    for segment in segments:
        
        text += segment.text

    text = text.strip()

    # Complete the "You: " line
    print(text)

    if os.path.exists("voice.wav"):
        os.remove("voice.wav")

    return text
  



"""
sd.rec() decides how long.
InputStream() lets your program decide.

model = WhisperModel("tiny",device = "cpu", compute_type= "int8")
    -Whisper comes in various types, for my laptop tiny is best
    -Whisper can run in CPU/GPU
    -compute_type controls how AI stores numbers in memory (similar to image like 4k/1080/720/)

sample_rate = 16000
    -Sets the recording quality.
    -Whisper is trained on 16,000 samples per second, so this is the ideal rate.

print("You: ", end="", flush=True)
    -end="" → don't move to a new line
    -flush=True → display it immediately

audio_data = []
    -Creates an empty list.
    -Stores every audio chunk while you're speaking.

is_speaking = False
    -Boolean variable.
    -Tracks whether the user has started speaking.

silent_chunks = 0
    -Counts silent chunks.
    -Helps determine when you've stopped speaking.

SILENT_LIMIT = 30
    -Maximum silent chunks allowed.
    -When silence reaches 30 chunks, recording stops.

with sd.InputStream(
    -Opens the microphone.
    -Starts receiving live audio.
    -with automatically closes the microphone when finished.

samplerate=sample_rate
    -Uses the sample rate we defined earlier.

channels=1
    -Mono recording.
    -Speech doesn't need stereo.

dtype="float32"
    -Stores audio as 32-bit floating-point numbers.
    -Standard format for Whisper.

data, overflowed = stream.read(1024)
    -Reads 1024 audio samples.
    -data → microphone audio
    -overflowed → whether recording couldn't keep up

volume = np.abs(data).mean()
    -data = Contains audio samples like: -0.02,0.01,-0.99
    -np.abs(data) = Converts negatives to positives.(0.02,0.01,0.99)
    -.mean() = Finds the average volume.(0.027)

if is_speaking and silent_chunks >= SILENT_LIMIT:
    -user already spoke and has now been silent long enough

audio = np.concatenate(audio_data, axis=0)
    -Turns many small chunks into one continuous audio array.
    -Like: Chunk 1,Chunk 2,Chunk 3 = One complete recording


segments,info = model.transcrib("voice.wav")
    -.trnscrib() is a method means "hey AI,listen to thi audio"
    -Calyx record a each voice.wav each time u speak
    -Whisper returns two things the spoken text & the extra info .
    segments is for Spoken text and info is for extra info

text = ""
    -Starts with no text

    
for segments in segments :
    -That segments is a collection of transcription pieces. this loop collect all the pices in segments

text = text.strip()
    -Removes extra spaces at the beginning and end.

if os.path.exists("voice.wav"):
    os.remove("voice.wav")
    -Deletes the temporary recording after transcription to keep your project folder clean.



Microphone
      │
      ▼
InputStream
      │
      ▼
Read small audio chunks
      │
      ▼
Measure volume
      │
      ▼
Voice detected?
      │
      ▼
Store audio
      │
      ▼
2 seconds of silence?
      │
      ▼
Stop recording
      │
      ▼
Save voice.wav
      │
      ▼
Whisper transcribes
      │
      ▼
Combine text segments
      │
      ▼
Return text to brain.py
      │
      ▼
Calyx processes the command
"""