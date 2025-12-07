from LOGIC.maze import generate_maze
import shutil
from PIL import Image
import random
import time
from pathlib import Path

PATH_COLOR = (255, 255, 255)
EXPLORED_COLOR = (150, 150, 150)
WALL_COLOR = (0,0,0)

SIZE = [251, 251]

def draw_path(image, path):
    for knot in path:
        image.putpixel(knot, (255, 0, 0))

def knot_start(image):
    for pix in range(SIZE[0]):
        if image.getpixel((pix, 0)) == PATH_COLOR:
            return pix
        
def is_explored(image, x, y):
    try:
        if image.getpixel((x, y)) == PATH_COLOR:
            return (x, y)
        else:
            return None
    except IndexError:
        return None

def path_options(image, x, y):
    return [position for position in [
            is_explored(image, x+1, y),
            is_explored(image, x-1, y),
            is_explored(image, x, y+1),
            is_explored(image, x, y-1)
        ] if position is not None]

def deep_explore(image, pos_start, h):
    print("Solving maze...", end="\r")
    start_time = time.time()
    current_x, current_y = pos_start
    path = [pos_start]
    # paths relative to project root (two levels up from this file: project/LOGIC/..)
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
    SOLUTION_PATH = OUTPUT_DIR / "maze_solution.png"

    while True:
        while len(path_options(image, current_x, current_y)) == 0:
            if current_y == h-1:
                path.append((current_x, current_y))
                draw_path(image, path)
                OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
                image.save(str(SOLUTION_PATH))

                print(f"SOLVING DONE IN {time.time() - start_time}")
                return
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            image.save(str(SOLUTION_PATH))
            current_x, current_y = path.pop()

        next_x, next_y = random.choice(path_options(image, current_x, current_y))
        image.putpixel((next_x, next_y), EXPLORED_COLOR)
        path.append((current_x, current_y))

        current_x = next_x
        current_y = next_y

def solve(w, h):
    # Use project-root-relative OUTPUT directory
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
    maze_PATH = OUTPUT_DIR / "maze.png"
    SOLUTION_PATH = OUTPUT_DIR / "maze_solution.png"

    # generate the maze image first
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generate_maze(w, h)

    # ensure the generated maze exists, then copy to solution file
    if not maze_PATH.exists():
        raise FileNotFoundError(f"maze image not found at {maze_PATH}")

    shutil.copy(str(maze_PATH), str(SOLUTION_PATH))
    maze = Image.open(str(SOLUTION_PATH))
    deep_explore(maze, (knot_start(maze), 0), h)
