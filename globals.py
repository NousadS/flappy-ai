import pygame


class Textures:
    def __init__(self):
        self.birds = pygame.image.load("./assets/images/birds.png").convert_alpha()
        self.pipes = pygame.image.load("./assets/images/pipes.png").convert_alpha()
        self.clouds = pygame.image.load("./assets/images/clouds.png").convert_alpha()
        self.background = pygame.image.load("./assets/images/background.png").convert_alpha()


class Sounds:
    def __init__(self):
        self.jump = pygame.mixer.Sound("./assets/sounds/jump.wav")
        self.death = pygame.mixer.Sound("./assets/sounds/death.wav")
        self.best = pygame.mixer.Sound("./assets/sounds/best.wav")
        self.pause = pygame.mixer.Sound("./assets/sounds/pause.wav")
        self.saved = pygame.mixer.Sound("./assets/sounds/saved.wav")
        self.generation = pygame.mixer.Sound("./assets/sounds/generation.wav")
        self.test_passed = pygame.mixer.Sound("./assets/sounds/test_passed.wav")

        self.jump.set_volume(0)
        self.death.set_volume(0.1)



class Fonts:
    def __init__(self):
        self.normal = pygame.font.SysFont("Hack", 20, italic=False, bold=False)
        self.italic = pygame.font.SysFont("Hack", 20, italic=True, bold=False)
        self.bold = pygame.font.SysFont("Hack", 20, italic=False, bold=True)
        self.both = pygame.font.SysFont("Hack", 20, italic=True, bold=True)

        self.small_normal = pygame.font.SysFont("Hack", 10, italic=False, bold=False)
        self.small_italic = pygame.font.SysFont("Hack", 10, italic=True, bold=False)
        self.small_bold = pygame.font.SysFont("Hack", 10, italic=False, bold=True)
        self.small_both = pygame.font.SysFont("Hack", 10, italic=True, bold=True)

        self.big_normal = pygame.font.SysFont("Hack", 30, italic=False, bold=False)
        self.big_italic = pygame.font.SysFont("Hack", 30, italic=True, bold=False)
        self.big_bold = pygame.font.SysFont("Hack", 30, italic=False, bold=True)
        self.big_both = pygame.font.SysFont("Hack", 30, italic=True, bold=True)


class Colors:
    def __init__(self):
        self.transparent = (0, 0, 0, 0)
        self.background = (109, 197, 199)

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (105, 106, 106)

        self.red = (174, 50, 50)
        self.green = (106, 190, 48)
        self.blue = (48, 96, 130)

        self.purple = (117, 66, 138)
        self.pink = (215, 123, 186)
        self.yellow = (251, 242, 54)
        self.orange = (223, 113, 38)

        self.brown = (102, 57, 49)
        self.beige = (217, 160, 102)

        self.light_red = (217, 89, 102)
        self.light_green = (153, 229, 80)
        self.light_blue = (91, 110, 225)

        self.light_purple = (160, 104, 182)
        self.light_pink = (233, 185, 218)
        self.light_yellow = (253, 247, 135)
        self.light_orange = (233, 158, 109)

        self.light_brown = (143, 86, 59)
        self.light_beige = (238, 195, 154)

class Globals:
    def __init__(self):
        self.pipes_y_gap = 150

        self.pipe_spawn_gap = 400
        self.cloud_spawn_gap = 400

        self.cloud_speed_clamp = (-1, -1)

        self.pipe_speed = (-2, 0)
        self.bird_speed = (0, -5)

        self.bird_x = 100

        self.bird_jump_speed = -5
        self.bird_gravity = 0.5

        self.bird_texture_width = 12
        self.bird_texture_height = 360

        self.cloud_size_clamp = (0, 2)
        self.cloud_opacity_clamp = (0, 2)

        self.cloud_texture_width = 3
        self.cloud_texture_height = 3

        self.pipe_texture_width = 2
        self.pipe_texture_height = 1

        self.bird_max_frame = 12

        self.learning = True

        self.bird_speed_limit = 5

        self.weights_clamp = (-0.1, 0.1)

        self.skin_clamp = (-30, 30)