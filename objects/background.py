import pygame
import pygame.locals

from .entity import Entity


class Background(Entity):
    def __init__(self, engine: "Engine"):  # type: ignore  # noqa: F821
        super().__init__(engine)

        # --- Properties ---

        # Nothing here :)

        # --- Drawing ---

        self.image = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        # --- Movement ---

        self.rect = self.image.get_rect()

    def event(self, event: pygame.event.Event):
        super().event(event)

    def update(self):
        super().update()

        # --- Movement ---

        # Nothing here :)

        # --- Drawing ---

        self.image.fill(self.colors.background)
        self.image.blit(self.textures.background, (0, self.rect.height - 234))
