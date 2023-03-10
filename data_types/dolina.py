steps = "UDDDUDUU"
path = 8

sea_level = 0
valleys = 0

for step in steps:
    if step == "U":
        sea_level = sea_level + 1
        if sea_level == 0:
            valleys = sea_level + 1
    elif step == "D":
        sea_level = sea_level - 1

print(f"Result: {valleys} count!")
