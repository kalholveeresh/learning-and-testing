import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Get all voices
voices = engine.getProperty('voices')

# Set voice (0 = male, 1 = female usually)
engine.setProperty('voice', voices[1].id)

# Set speech rate (default ~200)
engine.setProperty('rate', 160)

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

text = """
Hello Veeresh,
This is an advanced text to speech example using Python.
You can control voice, speed, and volume.
"""

# Speak
engine.say(text)

# Save audio to file
engine.save_to_file(text, 'output_audio.mp3')

engine.runAndWait()
