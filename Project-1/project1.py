first = {}
name = []
value = []


with open(
    file=r"D:\Scripts\uni\lbu-assignment-specs\Project-1\lap_times_1.txt", mode="r"
) as file:
    for lines in file:
        strip = lines.strip()
        name.append(strip[:3])
        value.append(strip[3:])


for key, value in zip(name, value):
    if key not in first:
        first[key] = []
    first[key].append(value)

# print(first)
for key, values in first.items():
    print(f"{key}", len(first[f"{key}"]))
