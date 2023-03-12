from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model(r"/Users/david/repos/github/DavidPeterWatson/home-automation/src/vosk/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

done = False

while not done:
    data = stream.read(1024)
    if recognizer.AcceptWaveform(data):
        resultString = recognizer.Result()
        result = json.loads(resultString)
        print(result)
        if result['text'] == "exit":
            print("Closing")
            done = True