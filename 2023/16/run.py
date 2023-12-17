# %%
from collections import deque

open("input.txt").read()

with open("input.txt") as file:
    data = file.read().splitlines()


len_rows = len(data)
len_cols = len(data[0])


def find(init):
    beams = deque([init])

    visitid = set()

    while True:
        if len(beams) == 0:
            break

        beam = beams.popleft()

        if beam in visitid:
            # print("duplicated")
            continue

        visitid.add(beam)

        beam_direction = beam[0]
        beam_location = beam[1]

        if "R" in beam_direction:
            next_beam_loc = (beam_location[0], beam_location[1] + 1)
        elif "L" in beam_direction:
            next_beam_loc = (beam_location[0], beam_location[1] - 1)
        elif "U" in beam_direction:
            next_beam_loc = (beam_location[0] - 1, beam_location[1])
        elif "D" in beam_direction:
            next_beam_loc = (beam_location[0] + 1, beam_location[1])
        else:
            raise ValueError("Invalid beam direction")

        if next_beam_loc[0] < 0 or next_beam_loc[0] >= len_rows:
            # print("light out")
            continue
        if next_beam_loc[1] < 0 or next_beam_loc[1] >= len_cols:
            # print("light out")
            continue

        value_of_next_beam = data[next_beam_loc[0]][next_beam_loc[1]]
        if value_of_next_beam == ".":
            beams.append((beam_direction, next_beam_loc))

        elif value_of_next_beam == "|" and (
            beam_direction == "R" or beam_direction == "L"
        ):
            beams.append(("D", next_beam_loc))
            beams.append(("U", next_beam_loc))

        elif value_of_next_beam == "|" and (
            beam_direction == "D" or beam_direction == "U"
        ):
            beams.append((beam_direction, next_beam_loc))

        elif value_of_next_beam == "-" and (
            beam_direction == "D" or beam_direction == "U"
        ):
            beams.append(("L", next_beam_loc))
            beams.append(("R", next_beam_loc))

        elif value_of_next_beam == "-" and (
            beam_direction == "L" or beam_direction == "R"
        ):
            beams.append((beam_direction, next_beam_loc))

        elif value_of_next_beam == "\\" and beam_direction == "R":
            beams.append(("D", next_beam_loc))

        elif value_of_next_beam == "\\" and beam_direction == "D":
            beams.append(("R", next_beam_loc))

        elif value_of_next_beam == "\\" and beam_direction == "L":
            beams.append(("U", next_beam_loc))

        elif value_of_next_beam == "\\" and beam_direction == "U":
            beams.append(("L", next_beam_loc))

        elif value_of_next_beam == "/" and beam_direction == "R":
            beams.append(("U", next_beam_loc))

        elif value_of_next_beam == "/" and beam_direction == "D":
            beams.append(("L", next_beam_loc))

        elif value_of_next_beam == "/" and beam_direction == "L":
            beams.append(("D", next_beam_loc))

        elif value_of_next_beam == "/" and beam_direction == "U":
            beams.append(("R", next_beam_loc))
        else:
            raise ValueError("Invalid beam direction")

    locs_visited = {l[1] for l in visitid}

    # print(len(locs_visited) - 1)
    return len(locs_visited) - 1


find(("R", (0, -1)))

# %%
top = []
for i in range(len_rows):
    top.append(find(("R", (i, -1))))
    top.append(find(("L", (i, len_rows + 1))))
    top.append(find(("U", (len_rows, len_rows + 1))))
    top.append(find(("D", (len_rows, -1))))

max(top)

# %%
