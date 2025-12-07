from PIL import Image
import random
import time
from pathlib import Path

EMPTY_COLOR = (128, 128, 128)
TAKEN_COLOR = (255, 255, 255)
WALL_COLOR = (0,0,0)

def is_free(image, x, y):
    try:
        if image.getpixel((x, y)) == EMPTY_COLOR:
            return (x, y)
        else:
            return None
    except IndexError:
        return None

def free_adjacent_rooms(image, x, y):
    return [position for position in [
            is_free(image, x+2, y),
            is_free(image, x-2, y),
            is_free(image, x, y+2),
            is_free(image, x, y-2)
        ] if position is not None]

def generate_maze(largeur, hauteur):
    start_time = time.time()
    # project-root-relative OUTPUT folder
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    maze_image = Image.new("RGB", (largeur, hauteur), WALL_COLOR) #Empty board

    for x in range(int((largeur-1)/2)): #Empty rooms created
        for y in range(int(((hauteur-1)/2))):
            maze_image.putpixel((x*2+1, y*2+1), EMPTY_COLOR)

    start_x = random.randint(0, int((largeur-3)/2))*2+1 #Start room set
    start_y = random.randint(0, int((hauteur-3)/2))*2+1
    maze_image.putpixel((start_x, start_y), TAKEN_COLOR)

    current_x = start_x
    current_y = start_y
    path = []

    while True:
        while len(free_adjacent_rooms(maze_image, current_x, current_y)) == 0:
            if not path:
                # We add an entrance and an exit
                x_start, y_start = random.randint(0, largeur // 2 - 1) * 2 + 1, 0
                x_end, y_end = random.randint(0, largeur // 2 - 1) * 2 + 1, hauteur - 1
                maze_image.putpixel((x_start, y_start), (255, 255, 255))
                maze_image.putpixel((x_end, y_end), (255, 255, 255))

                # save to project OUTPUT directory
                maze_image.save(str(OUTPUT_DIR / "maze.png"))
                print(f"GENERATION DONE IN {time.time() - start_time}")
                return
            current_x, current_y = path.pop()

        next_x, next_y = random.choice(free_adjacent_rooms(maze_image, current_x, current_y))

        maze_image.putpixel((int(current_x - (current_x-next_x) / 2), int(current_y - (current_y-next_y) / 2)), TAKEN_COLOR)
        maze_image.putpixel((next_x, next_y), TAKEN_COLOR)

        path.append((current_x, current_y))

        current_x = next_x
        current_y = next_y
