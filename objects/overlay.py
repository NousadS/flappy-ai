import pathlib

import pendulum
import pygame
import pygame.locals

from .entity import Entity


class Overlay(Entity):
    def __init__(self, engine: "Engine"):  # type: ignore  # noqa: F821
        super().__init__(engine)

        # --- Properties ---

        self.show_hit_boxes = False
        self.show_best = True
        self.show_ids = False
        self.show_scores = False

        self.blocked = False
        self.block_blink = 0

        # --- Drawing ---

        self.image = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        # --- Movement ---

        self.rect = self.image.get_rect()

    def event(self, event: pygame.event.Event):
        super().event(event)

        if event.type == pygame.locals.QUIT:
            self.engine.stop()

        if event.type == pygame.locals.KEYDOWN:
            if self.blocked:
                if event.key == pygame.locals.K_EQUALS:
                    self.blocked = False
            else:
                if event.key == pygame.locals.K_EQUALS:
                    self.blocked = True

                if event.key == pygame.locals.K_h:
                    self.show_hit_boxes = not self.show_hit_boxes

                if event.key == pygame.locals.K_b:
                    self.show_best = not self.show_best

                if event.key == pygame.locals.K_i:
                    self.show_ids = not self.show_ids

                if event.key == pygame.locals.K_s:
                    self.show_scores = not self.show_scores

                if event.key == pygame.locals.K_ESCAPE:
                    self.engine.stop()

                if event.key == pygame.locals.K_r:
                    self.engine.best = None
                    self.engine.run()

                if event.key == pygame.locals.K_n:
                    self.engine.run()

                if event.key == pygame.locals.K_p:
                    self.sounds.pause.play()

                    self.engine.pause()

                if event.key == pygame.locals.K_e:
                    with pathlib.Path(f"./best/{pendulum.now().format("YYYY-MM-DD HH.mm")}.txt").open("w") as file:
                        file.write(f"{self.best.weights[0]}\n")
                        file.write(f"{self.best.weights[1]}\n")
                        file.write(f"{self.best.weights[2]}\n")

                    self.sounds.saved.play()

                if event.key == pygame.locals.K_l:
                    with list(pathlib.Path("./best").iterdir())[-1].open("r") as file:
                        self.engine.best.weights = [float(line.strip()) for line in file.readlines()]

                    self.engine.run()

    def update(self):
        super().update()

        # --- Movement ---

        # Nothing here :)

        # --- Drawing ---

        self.image.fill(self.colors.transparent)

        if self.show_best:
            best_render = self.fonts.bold.render(f"Best Score: {self.best.score}", True, self.colors.white)

            id_render = self.fonts.small_both.render(f"ID: {self.best.bird.id}", True, self.colors.white)

            weight_1_render = self.fonts.small_bold.render(f"{self.best.weights[0]:+.2f}", True, self.colors.black, self.colors.white)
            weight_2_render = self.fonts.small_bold.render(f"{self.best.weights[1]:+.2f}", True, self.colors.black, self.colors.white)
            weight_3_render = self.fonts.small_bold.render(f"{self.best.weights[2]:+.2f}", True, self.colors.black, self.colors.white)

            neuron_1_render = self.fonts.small_bold.render(f"{self.best.neurons[0]:+.2f}", True, self.colors.white)
            neuron_2_render = self.fonts.small_bold.render(f"{self.best.neurons[1]:+.2f}", True, self.colors.white)
            neuron_3_render = self.fonts.small_bold.render(f"{self.best.neurons[2]:+.2f}", True, self.colors.white)

            out_render = self.fonts.small_bold.render(f"{self.best.out * 100:+.2f} ÷ 100", True, self.colors.white)

            pygame.draw.rect(self.image, (*self.colors.black, 128), (self.rect.width - 300, 0, 300, 200), border_bottom_left_radius=20)

            self.image.blit(best_render, (self.rect.width - 290, 10))

            self.image.blit(self.best.bird.image, (self.rect.width - 10 - self.best.bird.rect.width, 10))
            self.image.blit(id_render, (self.rect.width - 10 - id_render.get_width(), 10 + self.best.bird.height))

            pygame.draw.line(self.image, self.colors.white, (self.rect.width - 250, 60), (self.rect.width - 100, 110), max(1, min(10, round(abs(self.best.weights[0] * 100)) // 2)))
            pygame.draw.line(self.image, self.colors.white, (self.rect.width - 250, 110), (self.rect.width - 100, 110), max(1, min(10, round(abs(self.best.weights[1] * 100)) // 2)))
            pygame.draw.line(self.image, self.colors.white, (self.rect.width - 250, 160), (self.rect.width - 100, 110), max(1, min(10, round(abs(self.best.weights[2] * 100)) // 2)))

            pygame.draw.circle(self.image, self.colors.yellow, (self.rect.width - 250, 60), 7)
            pygame.draw.circle(self.image, self.colors.yellow, (self.rect.width - 250, 110), 7)
            pygame.draw.circle(self.image, self.colors.yellow, (self.rect.width - 250, 160), 7)

            pygame.draw.circle(self.image, self.colors.yellow, (self.rect.width - 100, 110), 7)

            self.image.blit(weight_1_render, (self.rect.width - 100 - abs(250 - 100) // 2 - weight_1_render.get_width() // 2, 60 + 25 - weight_1_render.get_height() // 2))
            self.image.blit(weight_2_render, (self.rect.width - 100 - abs(250 - 100) // 2 - weight_2_render.get_width() // 2, 60 + 50 - weight_2_render.get_height() // 2))
            self.image.blit(weight_3_render, (self.rect.width - 100 - abs(250 - 100) // 2 - weight_3_render.get_width() // 2, 60 + 75 - weight_3_render.get_height() // 2))

            self.image.blit(neuron_1_render, (self.rect.width - 260 - neuron_1_render.get_width(), 60 - neuron_1_render.get_height() // 2))
            self.image.blit(neuron_2_render, (self.rect.width - 260 - neuron_2_render.get_width(), 110 - neuron_2_render.get_height() // 2))
            self.image.blit(neuron_3_render, (self.rect.width - 260 - neuron_3_render.get_width(), 160 - neuron_3_render.get_height() // 2))

            self.image.blit(out_render, (self.rect.width - 90, 110 - out_render.get_height() // 2))

        if self.show_ids or self.show_scores:
            for bird in self.birds:
                id_render = self.fonts.small_both.render(f"ID: {bird.id}", True, self.colors.blue)
                score_render = self.fonts.small_both.render(f"Score: {bird.intellect.score}", True, self.colors.blue)

                if self.show_ids and self.show_scores:
                    self.image.blit(id_render, (bird.rect.center[0] - id_render.get_width() // 2, bird.rect.y - 20))
                    self.image.blit(score_render, (bird.rect.center[0] - score_render.get_width() // 2, bird.rect.y - 10))
                elif self.show_ids:
                    self.image.blit(id_render, (bird.rect.center[0] - id_render.get_width() // 2, bird.rect.y - 10))
                elif self.show_scores:
                    self.image.blit(score_render, (bird.rect.center[0] - score_render.get_width() // 2, bird.rect.y - 10))

        if self.show_hit_boxes:
            for object in [*self.birds, *self.pipes]:
                pygame.draw.rect(self.image, self.colors.red, object.rect, 2)

            for object in [*self.clouds, self.background, self.overlay]:
                pygame.draw.rect(self.image, self.colors.green, object.rect, 2)

        if self.blocked:
            self.block_blink = (self.block_blink + 1) % 50

            color = self.colors.red if self.block_blink < 25 else self.colors.light_red

            blocked_render = self.fonts.big_bold.render("BLOCKED", True, color)

            self.image.blit(blocked_render, (self.rect.width // 2 - blocked_render.get_width() // 2, self.rect.height // 2 - blocked_render.get_height() // 2))