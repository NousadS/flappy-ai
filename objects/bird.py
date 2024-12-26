import random

import pygame

from objects.pipe import PipeTop

from .entity import Entity


class Intellect:
    def __init__(self, bird: "Bird", parent: "Intellect" = None):
        # --- Super ---

        self.bird = bird
        self.globals = bird.globals
        self.parent = parent

        # --- Properties ---

        self.score = 0
        self.out = 0

        self.alive = True

        self.neurons = [0, 0, 0]

        # --- Inherence ---

        if self.parent is None:
            self.skin = random.randint(0, self.globals.bird_texture_height - 1)

            self.weights = [random.uniform(*self.globals.intellect_weights_clamp) for _ in range(len(self.neurons))]
        else:
            self.skin = self.parent.skin

            self.weights = self.parent.weights.copy()

            if self.globals.intellect_learning:
                for i in range(len(self.weights)):
                    uniform = random.uniform(*self.globals.intellect_intellect_rate_clamp)

                    self.skin += uniform * 10 * self.bird.height
                    self.weights[i] += uniform

            self.skin = round(self.skin)
            self.skin = max(0, min(self.skin, self.globals.bird_texture_height - 1))

    def think(self):
        self.score += self.globals.intellect_score_increase

        nearest = None

        for pipe in self.bird.pipes:
            if nearest is None or (isinstance(pipe, PipeTop) and pipe.rect.x >= self.globals.bird_x - self.bird.width * 2 and pipe.rect.x < nearest.rect.x):
                nearest = pipe

        if nearest.rect.y + nearest.height + nearest.gap // 2 > self.bird.rect.y > nearest.rect.y + nearest.height:
            self.score += abs(nearest.rect.y + nearest.height + nearest.gap // 2 - self.bird.rect.y)

        if nearest is None:
            self.out = 0
        else:
            screen_width = self.bird.screen.get_width()
            screen_height = self.bird.screen.get_height()

            self.neurons = [
                self.bird.rect.y / screen_height,
                (pipe.rect.x + pipe.height) / screen_width,
                (pipe.rect.x + pipe.height + pipe.gap) / screen_width,
            ]

            self.out = sum([i[0] * i[1] for i in zip(self.neurons, self.weights)])


class Bird(Entity):
    def __init__(self, engine: "Engine", parent: "Intellect" = None):  # type: ignore  # noqa: F821
        super().__init__(engine)

        # --- Properties ---

        self.intellect = Intellect(self, parent)
        self.id = max([bird.id for bird in engine.birds], default=0) + 1

        # --- Drawing ---

        self.texture = self.textures.birds

        self.width = self.texture.get_width() // self.globals.bird_texture_width
        self.height = self.texture.get_height() // self.globals.bird_texture_height

        self.texture = self.texture.subsurface(
            0,
            self.intellect.skin * self.height,
            self.width * self.globals.bird_max_frame,
            self.height,
        )

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.frame = 0

        # --- Movement ---

        self.rect = self.image.get_rect()

        self.speed = pygame.math.Vector2(*self.globals.bird_speed)
        self.jump_speed = self.globals.bird_jump_speed
        self.jump_delay = 0
        self.gravity = self.globals.bird_gravity

    def event(self, event: pygame.event.Event):
        super().event(event)

    def update(self):
        super().update()

        # --- Intellect ---

        self.intellect.think()

        # --- Movement ---

        self.rect.move_ip(self.speed)
        self.rect.x = self.globals.bird_x

        if self.rect.y < 0:
            self.rect.y = 1

        if self.rect.y + self.height >= self.screen.get_height():
            self.rect.y = self.screen.get_height() - self.height

        if self.speed.y < self.globals.bird_speed_limit:
            self.speed.y += self.gravity

        if pygame.sprite.spritecollide(self, self.pipes, False):
            self.intellect.alive = False

            self.sounds.death.play()

            self.kill()

        if self.intellect.out > 0:
            self.jump()

        if self.jump_delay > 0:
            self.jump_delay -= 1

        # --- Drawing ---

        self.frame = (self.frame + self.globals.frame_speed) % (self.globals.bird_max_frame - 1)

        self.image.fill(self.colors.transparent)
        self.image.blit(self.texture, (round(self.frame) * -self.width, 0))

    def jump(self):
        if self.jump_delay <= 0:
            self.speed.y = self.jump_speed

            if len(self.birds) <= 5:
                self.sounds.jump.play()

            self.jump_delay = self.globals.bird_jump_delay
