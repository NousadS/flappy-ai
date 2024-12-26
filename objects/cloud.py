import random

import pygame

from .entity import Entity


class Cloud(Entity):
    def __init__(self, engine: "Engine"):  # type: ignore  # noqa: F821
        super().__init__(engine)

        self.clouds.add(self)

        # --- Properties ---

        self.size = random.randint(*self.globals.cloud_size_clamp)
        self.opacity = random.randint(*self.globals.cloud_opacity_clamp)

        # --- Drawing ---

        self.texture = self.textures.clouds.copy()

        self.width = self.texture.get_width() // self.globals.cloud_texture_width
        self.height = self.texture.get_height() // self.globals.cloud_texture_height

        self.texture = self.texture.subsurface(self.size * self.width, self.opacity * self.height, self.width, self.height)

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # --- Movement ---

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width())
        self.rect.y = random.randint(0, self.screen.get_height())

        self.speed = pygame.math.Vector2(random.uniform(*self.globals.cloud_speed_clamp), 0)

    def event(self, event: pygame.event.Event):
        super().event(event)

    def update(self):
        super().update()

        # --- Movement ---

        self.rect.move_ip(self.speed)

        if self.rect.x + self.width <= 0:
            self.rect.x = self.screen.get_width()

        # --- Drawing ---

        self.image.fill(self.colors.transparent)

        self.image.blit(self.texture, (0, 0))
