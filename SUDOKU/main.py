# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#import PyQt6.QtWidgets
from numpy import array
from math import floor


def print_sudoku(complete):
    print(complete)


def check(index, set_temp):

    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    x = set_temp[index[0], :]
    y = set_temp[:, index[1]]

    # Get numbers in a quadrant
    quad_x = floor(index[0]/3)
    quad_y = floor(index[1]/3)
    quad = []
    for j in range(quad_x*3, quad_x*3+3):
        for k in range(quad_y * 3, quad_y * 3 + 3):
            quad.append(set_temp[j, k])

    # Remove similar numbers on possible
    for i in quad:
        if i in possible:
            possible.remove(i)
    for i in x:
        if i in possible:
            possible.remove(i)
    for i in y:
        if i in possible:
            possible.remove(i)

    return possible


def sudoku(set_prime):
    # Convert to Array
    set_sol = array(set_prime)
    i, j = 0, 0
    saves = [[0, 0, 0]]
    while i < len(set_prime):
        while j < len(set_prime):
            if set_sol[i, j] == 0:
                # Append Address with blanks
                saves.append([i, j, 0])
                status = True
                while status:
                    possible = check((i, j), set_sol)
                    # IF NO POSSIBLE MATCHES, Means had previous mistake
                    if not possible:
                        # Remove current address (i,j). Need last latest address
                        saves.pop(-1)

                        # Address of last match
                        i, j = saves[-1][0], saves[-1][1]
                        # Next possible() of last match
                        saves[-1][-1] += 1
                        # Set again to blank the last match. Previously guessed
                        set_sol[i, j] = 0
                        # Check possible again
                        possible = check((i, j), set_sol)

                    # IF - Not tried all possible answers yet. ELSE - Next previous blank
                    if len(possible) > saves[-1][-1]:
                        set_sol[i, j] = possible[saves[-1][-1]]
                        status = False
                    else:
                        saves.pop(-1)
                        saves[-1][-1] += 1
                        i, j = saves[-1][0], saves[-1][1]
                        set_sol[i, j] = 0

            j += 1
        j = 0
        i += 1

    return set_sol


if __name__ == '__main__':
    sample = (
        (0, 5, 2, 0, 0, 6, 0, 0, 0),
        (1, 6, 0, 9, 0, 0, 0, 0, 4),
        (0, 4, 9, 8, 0, 3, 6, 2, 0),

        (4, 0, 0, 0, 0, 0, 8, 0, 0),
        (0, 8, 3, 2, 0, 1, 5, 9, 0),
        (0, 0, 1, 0, 0, 0, 0, 0, 2),

        (0, 9, 7, 3, 0, 5, 2, 4, 0),
        (2, 0, 0, 0, 0, 9, 0, 5, 6),
        (0, 0, 0, 1, 0, 0, 9, 7, 0),
        )

    solution = sudoku(sample)
    #print_sudoku(array(sample))
    print_sudoku(solution)
