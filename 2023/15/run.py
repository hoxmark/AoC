# Import necessary libraries

with open("input.txt") as file:
    steps = file.read().strip().split(",")


def string_hash(s):
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256
    return value


boxes = [[] for _ in range(256)]

part1_result = 0

for step in steps:
    part1_result += string_hash(step)

    if "-" in step:
        label = step[:-1]
        boxes[string_hash(label)] = [
            item for item in boxes[string_hash(label)] if item[0] != label
        ]
    else:
        label, level_str = step.split("=")
        level = int(level_str)
        target_box = boxes[string_hash(label)]
        replaced = False

        for item in target_box:
            if item[0] == label:
                item[1] = level
                replaced = True
        if not replaced:
            target_box.append([label, level])

print("Task 1 Result:", part1_result)

part2_result = 0
for box_index, box in enumerate(boxes):
    for item_index, (label, level) in enumerate(box):
        part2_result += (box_index + 1) * (item_index + 1) * level

print("Task 2 Result:", part2_result)
