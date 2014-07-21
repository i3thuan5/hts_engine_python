import htsengine
model='example/Taiwanese.htsvoice'
label=[line.rstrip() for line in open('example/full.lab')]

s,f,n,a=htsengine.synthesize(model,label)
import wave
wavFile=wave.open('result.wav','wb')
wavFile.setsampwidth(s)
wavFile.setframerate(f)
wavFile.setnchannels(n)
wavFile.writeframesraw(a)
wavFile.close()
