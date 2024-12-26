# Flappy AI

The Flappy Bird, but with AI.

Documentation available in:
- [English](https://github.com/NousadS/flappy-ai/blob/main/README.md)
- [Russian](https://github.com/NousadS/flappy-ai/blob/main/README-ru.md)

# Key combinations

`=` - Disables all key combinations \
`p` - Pause

`h` - Shows the hitboxes:
 - green: hitbox without a collision
 - red: hitbox with a collision

`b` - Shows the best bird menu \
`i` - Shows a bird ID over it \
`s` - Shows a score of the bird above it

`n` - Creates a new generation WITH an inheritance from the last generation \
`r` - Creates a new generation WITHOUT an inheritance from the last generation

`e` - Saves all weights in `./best/{current_datetime}.txt` \
`l` - Loads all weights from the last saving

`ESC` - Exit from the game

# Global parameters

Global parameters are stored in Globals.py in Globals class. \
Near the Globals class there are Colors, Fonts, Sounds and Textures classes, you can change them, but this is not recommended.

### Bird

**bird_initial_count** (100) - how many birds will spawn

**bird_texture_width** (12) - *do not change*
**bird_texture_height** (360) - *do not change*

**frame_speed** (0.1) - how quickly the animation of birds changes
**bird_max_frame** (12) - maximum frame in bird animation
**bird_x** (100) - statical position of the bird by `x`

**bird_speed** (0, -5) - the speed of the bird, `x` should be 0
**bird_speed_limit** (5) - limit the speed of birds
**bird_jump_speed** (-5) - bird jumping speed
**bird_gravity** (0.5) - bird gravity

**bird_jump_delay** (15) - how much will the jump delay be

# Pipe

**pipe_initial_count** (1) - how many pipes will spawn (not recommended to change)

**pipe_texture_width** (2) - *do not change*
**pipe_texture_height** (1) - *do not change*

**pipe_padding** (150) - limit for the padding of a pipe by y
**pipe_gap_clamp** (100, 200) - limit for a gap of pipe

**pipe_spawn** (400) - position when a new pipe spawn
**pipe_speed** (-2, 0) - pipe speed

# Cloud

**cloud_initial_count** (10) - how many clouds will spawn

**cloud_texture_width** (3) - *do not change*
**cloud_texture_height** (3) - *do not change*

**cloud_size_clamp** (0, 2) - limit of random size
**cloud_opacity_clamp** (0, 2) - limit of random opaque

**cloud_speed_clamp** (-1, -1) - limit of random speed

# Intellect

**intellect_skin_clamp** (-30, 30) - random values limit ​​of the skin
**intellect_weights_clamp** (-0.1, 0.1) - random scales limit of intellect
**intellect_rate_clamp** (-0.05, 0.05) - learning rate limit

**intellect_score_increase** (1) - how much does the score increase in the frame
**intellect_learning** (True) - will intelligence learn or not

# Game

**fps** (60) - frame per second

# Interface

![Interface](https://raw.githubusercontent.com/NousadS/flappy-ai/refs/heads/main/readme/interface.png)

1. Bird, over which ID and score will be displayed.
2. Clouds.
3. Pipe (upper and lower).
4. Input layer of AI.
5. AI weights.
6. Output layer of AI.
7. Best score and bird with the best score.