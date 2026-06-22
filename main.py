import speech_recognition as sr
from pydub import AudioSegment
import io

def main():
    recognizer = sr.Recognizer()
    audio_file_path = r"temp\sample_song.mp3"

    try:
        # 1. Load the audio file
        print("Loading and converting audio...")
        sound = AudioSegment.from_mp3(audio_file_path)
        
        # 2. Force conversion to 16kHz, mono (required for best API compatibility)
        sound = sound.set_frame_rate(16000).set_channels(1)
        
        # 3. Export to an in-memory buffer
        wav_io = io.BytesIO()
        sound.export(wav_io, format="wav")
        wav_io.seek(0)

        # 4. Process the audio
        with sr.AudioFile(wav_io) as source:
            print("Processing audio file (this may take a moment)...")
            audio_data = recognizer.record(source)

        # 5. Recognize
        print("Transcribing...")
        audio_text = recognizer.recognize_google(audio_data)
        print("\n--- Transcription ---")
        print(audio_text)

    except FileNotFoundError:
        print(f"Error: The file at {audio_file_path} was not found.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()