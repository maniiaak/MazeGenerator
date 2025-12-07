# LabyrinthGenerator

A small Python project that generates mazes and their solutions, and saves the results as images in the `OUTPUT/` folder.

##  Features

- Procedural maze generation with configurable width and height (odd numbers, >= 7).
- Automatic solving of the generated maze and a visual solution overlay.
- Outputs PNG images to the `OUTPUT/` directory.

##  Screenshots

Generated maze:

![Generated maze](OUTPUT/maze.png)

Solved maze (solution overlaid):

![Solved maze](OUTPUT/maze_solution.png)

> If these images are missing, run the generator first (see Quick start below).

##  Quick start

1. Make sure you're in the project root (the repository top-level).
2. Run the program with Python 3.10+:

```bash
python3 main.py
```

3. When prompted, enter the width and height of the maze. The program will coerce values to the nearest odd number >= 7.
4. Check the `OUTPUT/` folder for `maze.png` and `maze_solution.png`.

##  Notes & Troubleshooting

- Run the script from the repository root to ensure relative paths resolve correctly. Running from another directory can cause FileNotFoundError when the program tries to read/write files in `OUTPUT/`.
- If you see a FileNotFoundError mentioning `OUTPUT/maze.png` or similar, re-run `main.py` to generate the files. Also make sure the `OUTPUT/` directory exists and is writable.

##  Project layout (important files)

- `main.py` — CLI entry point (asks for width/height and runs generator/solver).
- `LOGIC/` — maze generation and solve logic.
- `OUTPUT/` — generated PNG images (e.g. `maze.png`, `maze_solution.png`).
- `LICENSE` — project license.

## Contributing

Contributions are welcome. Open an issue or a pull request with a clear description of the change.

## License

This project is licensed under the terms in `LICENSE`.
