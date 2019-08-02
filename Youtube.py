from pydub import AudioSegment
import pafy

#url = "https://www.youtube.com/watch?v=uKxyLmbOc0Q"
#video = pafy.new(url)
#bestaudio = video.getbestaudio()
#bestaudio.download()

#wav_audio = AudioSegment.from_file("Renai.webm", format="wav")

#raw_audio = AudioSegment.from_file("Renai.webm", format="raw", frame_rate=44100, channels=2, sample_width=2)

song = AudioSegment.from_file("Renai.webm", "webm")
song.export("Renai.webm", format="mp3")