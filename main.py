import pygame

from globals import Colors, Fonts, Globals, Sounds, Textures
from objects import Background, Bird, Cloud, Overlay, PipeTop
from objects.bird import Intellect


class Engine:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Flappy AI")

        # --- Properties ---

        self.colors = Colors()
        self.fonts = Fonts()
        self.globals = Globals()
        self.sounds = Sounds()
        self.textures = Textures()

        self.best = None

        # --- Objects ---

        self.background = Background(self)
        self.overlay = Overlay(self)
        
        self.clouds = pygame.sprite.Group()

        for _ in range(10):
            self.clouds.add(Cloud(self))

    def run(self):
        # --- Objects ---

        self.birds = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()

        for _ in range(1):
            self.birds.add(Bird(self, self.best))

        self.best = None

        for _ in range(1):
            self.pipes.add(PipeTop(self))

        # --- Running ---

        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False

        self.sounds.generation.play()

        while self.running:
            objects = pygame.sprite.Group()
            objects.add(self.background)  # THIS
            objects.add(self.clouds)  # IS
            objects.add(self.pipes)  # FIXED
            objects.add(self.birds)  # ORDER
            objects.add(self.overlay)  #

            for event in pygame.event.get():
                for object in objects:
                    object.event(event)

            if not self.paused:
                if len(self.birds) == 0:
                    self.run()

                if self.best and not self.best.alive:
                    self.best = None

                for bird in self.birds:
                    if not self.best or (bird.intellect.alive and bird.intellect.score >= self.best.score):
                        self.best = bird.intellect

                objects.update()

            self.screen.fill((0, 0, 0))

            objects.draw(self.screen)

            pygame.display.update()

            self.clock.tick(60)

    def pause(self):
        self.paused = not self.paused

    def stop(self):
        self.running = False


Engine().run()
