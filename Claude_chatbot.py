import assemblyai as aai

#add your AssemblyAI API key here
aai.settings.api_key = "508454de6b514afa8dfee40f4e24c84b"

# Import your local audio file or a URL to an audio file
audio_file = "https://assembly.ai/wildfires.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)