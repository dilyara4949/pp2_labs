from ast import Global
import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))
running = True

songs = ['alexander-nakarada-superepic.mp3', 'HinaCC0_011_Fallen_leaves.mp3', 'bensound-jazzyfrenchy.mp3']

pygame.mixer.music.load(songs[0])
def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def play_prev_song():
    global songs
    songs = [songs[2]] + songs[:2]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                play_next_song()
            if event.key == pygame.K_LEFT:
                play_prev_song()
                    
                
            
    screen.fill((255, 255, 255))

    pygame.display.flip()                
            
