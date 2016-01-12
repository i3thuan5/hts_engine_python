import htsengine
from os.path import join, dirname
model = join(dirname(__file__), 'Taiwanese.htsvoice')
label = [line.rstrip() for line in open(join(dirname(__file__), 'full.lab'))]

s, f, n, a = htsengine.synthesize(model, label)
import wave
wavFile = wave.open('result.wav', 'wb')
wavFile.setsampwidth(s)
wavFile.setframerate(f)
wavFile.setnchannels(n)
wavFile.writeframesraw(a)
wavFile.close()
