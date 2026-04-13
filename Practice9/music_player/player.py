import pygame

class MusicPlayer:
    def __init__(self):
        self.tracks = [
            "C:/Users/Roar/Documents/GitHub/PP2/Practice9/music_player/music/track1.wav",
            "C:/Users/Roar/Documents/GitHub/PP2/Practice9/music_player/music/track2.wav"
        ]
        self.index = 0

    def play(self):
        pygame.mixer.music.load(self.tracks[self.index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def current_track(self):
        return self.tracks[self.index]