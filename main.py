import whisper
import os

def main():
    # Define your file path
    audio_file = r"temp\sample_song.mp3"
    
    if not os.path.exists(audio_file):
        print(f"Error: File not found at {audio_file}")
        return

    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print(f"Transcribing '{audio_file}'... (this might take a while)")
    
    try:
        result = model.transcribe(audio_file)
        
        print("\n--- Transcription Result ---")
        print(result["text"])
        
    except Exception as e:
        print(f"An error occurred during transcription: {e}")

if __name__ == "__main__":
    main()