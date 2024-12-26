import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, engine: "Engine", *args, **kwargs):  # type: ignore  # noqa: F821
        super().__init__(*args, **kwargs)

        self.engine = engine

        self.parameters()

    def update(self):
        self.parameters()

    def event(self, event: pygame.event.Event): ...

    def parameters(self):
        self.screen = self.engine.screen

        self.textures = self.engine.textures
        self.sounds = self.engine.sounds
        self.fonts = self.engine.fonts
        self.colors = self.engine.colors
        self.globals = self.engine.globals

        if hasattr(self.engine, "background"):
            self.background = self.engine.background

        if hasattr(self.engine, "overlay"):
            self.overlay = self.engine.overlay

        if hasattr(self.engine, "birds"):
            self.birds = self.engine.birds

        if hasattr(self.engine, "pipes"):
            self.pipes = self.engine.pipes

        if hasattr(self.engine, "clouds"):
            self.clouds = self.engine.clouds

        self.best = self.engine.best