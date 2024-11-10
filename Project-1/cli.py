import argparse

parser = argparse.ArgumentParser(
    prog="Grand Prix Timings Board",
    description="A program that visualizes timecodes from the Grand Prix",
)

parser.add_argument(
    "-filename", help="Path to the timecodes file you want to parse", type=str
)

args = parser.parse_args()


def parse(filepath: str):
    dict = {}
    name = []
    value = []

    with open(file=filepath, mode="r") as file:
        for lines in file:
            strip = lines.strip()
            name.append(strip[:3])
            value.append(strip[3:])

    for key, value in zip(name, value):
        if key not in dict:
            dict[key] = []
        dict[key].append(value)

    return dict


print(parse(args.filename))
