"""Day ten of advent of code 2023 https://adventofcode.com/2023 """

# %%
import matplotlib.pyplot as plt

data = open("input.txt", encoding="utf-8").read().splitlines()

# legal pip connections
legal_pipe_connections = {}
north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)
# | is a vertical pipe connecting north and south.
legal_pipe_connections["|"] = [north, south]
# - is a horizontal pipe connecting east and west.
legal_pipe_connections["-"] = [east, west]
# L is a 90-degree bend connecting north and east.
legal_pipe_connections["L"] = [north, east]
# J is a 90-degree bend connecting north and west.
legal_pipe_connections["J"] = [north, west]
# 7 is a 90-degree bend connecting south and west.
legal_pipe_connections["7"] = [south, west]
# F is a 90-degree bend connecting south and east.
legal_pipe_connections["F"] = [south, east]

# row_column_index_of_s = [
#     (i, j) for i, r in enumerate(data) for j, c in enumerate(r) if c == "S"
# ]
# r, c = row_column_index_of_s[0]
# print(r, c)

r, c = 76, 109  # hardcoded and manually found
START = (r, c)


def explore(p, pipe):
    r, c = pipe
    current_pipe = data[r][c]
    options = legal_pipe_connections[current_pipe]

    nr = r + options[0][0]
    nc = c + options[0][1]
    if p[0] == nr and p[1] == nc:
        nr = r + options[1][0]
        nc = c + options[1][1]

    return (nr, nc)


pipes_to_explore = [(r, c)]
been = [(-1, -1)]
for i in range(100000):
    current_pipe = pipes_to_explore.pop(0)
    # print(current_pipe, data[current_pipe[0]][current_pipe[1]])
    res = explore(been[-1], current_pipe)
    pipes_to_explore.append(res)
    been.append(current_pipe)

    if i != 0 and current_pipe == START:
        break

been.pop(0)

assert (i // 2) == 6697


# %%
def is_point_inside_knot(point, knot):
    """The function is commonly referred to as a "Ray Casting" algorithm
    or sometimes a "Winding Number" algorithm. to figure out if the point is within a polygon/knot/loop
    https://stackoverflow.com/questions/217578/how-can-i-determine-whether-a-2d-point-is-within-a-polygon
    """
    x, y = point
    crossings = 0
    for i in range(len(knot)):
        x1, y1 = knot[i]
        x2, y2 = knot[(i + 1) % len(knot)]

        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        if y == y1 or y == y2:
            y = y + 0.1

        if y1 == y2 or y < y1 or y > y2:
            continue

        if x > max(x1, x2):
            continue

        if x1 != x2:
            xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
        elif x <= x1:
            crossings += 1
            continue

        if x1 == x2 or x <= xinters:
            crossings += 1

    return crossings % 2 != 0


# all the tiles I have visited can be looked at as a knot
knot = been

# Check again using the improved method
inside_points = []
for x in range(len(data)):
    for y in range(len(data[0])):
        if is_point_inside_knot((x, y), knot):
            inside_points.append((x, y))

inside_points = set(inside_points) - set(been)

assert len(inside_points) == 423
print("task2:", inside_points)
# %% Visulized knot
# Visualize the knot and the points inside it
knot_x, knot_y = zip(*knot)

# # Visualize the knot and inside points
inside_x_improved, inside_y_improved = (
    zip(*inside_points) if inside_points else ([], [])
)

plt.figure(figsize=(8, 8))
plt.plot(knot_x, knot_y, marker="o", color="blue", label="Knot")
plt.scatter(
    inside_x_improved, inside_y_improved, color="green", label="Improved Inside Points"
)
plt.legend()
plt.grid(True)
plt.show()
