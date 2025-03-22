import time
import random
from gtts import gTTS
import playsound
from sklearn.feature_extraction.text import CountVectorizer

# 1. Before Sleep – Setup Dream Recall Mode
def generate_sound_cue(memory_challenge):
    """Generate a sound cue for the memory challenge."""
    sound_text = f"Tonight, you will remember: {memory_challenge}"
    tts = gTTS(text=sound_text, lang='en')
    tts.save("sound_cue.mp3")
    print("Sound cue generated. Playing now...")
    playsound.playsound("sound_cue.mp3")

def start_sleep_tracking():
    """Simulate sleep tracking (can integrate with wearable APIs)."""
    print("Sleep tracking started...")
    time.sleep(5)  # Simulate sleep tracking for 5 seconds

# 2. During Sleep – AI-Triggered Memory Training
def detect_rem_sleep():
    """Simulate REM sleep detection (can integrate with EEG or wearable APIs)."""
    print("Detecting REM sleep...")
    time.sleep(3)  # Simulate REM sleep detection
    return True

def play_memory_cue():
    """Play a memory cue during REM sleep."""
    cues = ["Remember the number 7", "Think of a red apple", "Recall the word 'ocean'"]
    cue = random.choice(cues)
    print(f"Playing memory cue: {cue}")
    # Integrate with sound playback (e.g., playsound or PyAudio)

# 3. After Waking Up – Memory Game & Dream Journal
def record_dream():
    """Record the user's dream."""
    dream = input("What do you remember from your dream? ")
    return dream

def analyze_dream(dream):
    """Analyze dream patterns using basic NLP."""
    vectorizer = CountVectorizer().fit([dream])
    vectors = vectorizer.transform([dream])
    print(f"Dream analyzed. Keywords: {vectorizer.get_feature_names_out()}")

def memory_game():
    """Simple memory game based on the dream."""
    print("Let's play a memory game!")
    sequence = random.sample(range(1, 10), 3)  # Generate a random sequence
    print("Memorize this sequence:", sequence)
    time.sleep(5)  # Give the user time to memorize
    user_input = input("Enter the sequence (e.g., 1 2 3): ")
    user_sequence = list(map(int, user_input.split()))
    if user_sequence == sequence:
        print("Correct! Great memory!")
    else:
        print(f"Oops! The correct sequence was {sequence}.")

# Main Program
if __name__ == "__main__":
    # Before Sleep
    memory_challenge = input("Enter your memory challenge (e.g., a number, object, or event): ")
    generate_sound_cue(memory_challenge)
    start_sleep_tracking()

    # During Sleep
    if detect_rem_sleep():
        play_memory_cue()

    # After Waking Up
    dream = record_dream()
    analyze_dream(dream)
    memory_game()
