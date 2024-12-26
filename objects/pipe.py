import random

import pygame

from .entity import Entity


class PipeTop(Entity):
    def __init__(self, engine: "Engine"):  # type: ignore  # noqa: F821
        super().__init__(engine)

        self.pipes.add(self)

        # --- Properties ---

        self.gap = random.randint(*self.globals.pipe_gap_clamp)
        self.spawned = False

        # --- Drawing ---

        self.texture = self.textures.pipes.copy()

        self.width = self.texture.get_width() // self.globals.pipe_texture_width
        self.height = self.texture.get_height() // self.globals.pipe_texture_height

        self.texture = self.texture.subsurface(0, 0, self.width, self.height)

        self.image = pygame.Surface(
            (self.width, self.height * 2 + self.gap), pygame.SRCALPHA
        )

        # --- Movement ---

        self.rect = self.texture.get_rect()
        self.rect.x = self.screen.get_width()
        self.rect.y = (
            random.randint(
                self.globals.pipe_padding,
                self.screen.get_height() - self.globals.pipe_padding,
            )
            - self.height
        )

        self.speed = pygame.math.Vector2(*self.globals.pipe_speed)

        PipeBottom(self.engine, self)

    def event(self, event: pygame.event.Event): ...

    def update(self):
        super().update()

        # --- Movement ---

        self.rect.move_ip(self.speed)

        if self.rect.x + self.width <= 0:
            self.kill()

        if self.rect.x <= self.globals.pipe_spawn and not self.spawned:
            PipeTop(self.engine)

            self.spawned = True

        # --- Drawing ---

        self.image.fill(self.colors.transparent)
        self.image.blit(self.texture, (0, 0))


class PipeBottom(Entity):
    def __init__(self, engine: "Engine", top: PipeTop):  # type: ignore  # noqa: F821
        super().__init__(engine)

        self.pipes.add(self)

        # --- Properties ---

        self.top = top
        self.gap = top.gap
        self.speed = top.speed
        self.spawned = top.spawned

        # --- Drawing ---

        self.texture = self.textures.pipes.copy()

        self.width = self.texture.get_width() // self.globals.pipe_texture_width
        self.height = self.texture.get_height() // self.globals.pipe_texture_height

        self.texture = self.texture.subsurface(self.width, 0, self.width, self.height)

        self.image = pygame.Surface(
            (self.width, self.height * 2 + self.top.gap), pygame.SRCALPHA
        )

        # --- Movement ---

        self.rect = self.top.rect.copy()
        self.rect.y += self.height + self.top.gap

    def event(self, event: pygame.event.Event):
        super().event(event)

    def update(self):
        super().update()

        # --- Properties ---

        self.gap = self.top.gap
        self.speed = self.top.speed
        self.spawned = self.top.spawned

        # --- Movement ---

        self.rect = self.top.rect.copy()
        self.rect.y += self.top.height + self.top.gap

        # --- Drawing ---

        self.image.fill(self.colors.transparent)
        self.image.blit(self.texture, (0, 0))
