# Python file for music
# Allows the ability to implement music into the mystery game
import threading
import winsound

def main_music(music_file):
    try:
        # Using the winsound python library, implements sound into the game
        winsound.PlaySound(music_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    except Exception as e:
        print(f"Error playing music: {e}")

def sound_effect(music_file):
    try:
        # Using the winsound python library, implements sound into the game
        winsound.PlaySound(music_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing music: {e}")
