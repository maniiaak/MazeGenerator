from LOGIC.solve_algorithm import solve

print('''------------------------------------------------
|                MAZE GENERATOR                |
------------------------------------------------''')
w = int(input("WELCOME TO THE MAZE GENERATOR! \nPlease enter the width of the maze (odd number >= 7): "))
h = int(input("Please enter the height of the maze (odd number >= 7): "))

w += 1 - w % 2
h += 1 - h % 2

print("------------------------------------------------")
solve(w, h)
print("Maze generation and solving complete! Check the OUTPUT folder for results.\n------------------------------------------------")