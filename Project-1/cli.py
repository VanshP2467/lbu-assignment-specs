import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(
    prog="Grand Prix Timings Board",
    description="A program that visualizes timecodes from the Grand Prix",
)

parser.add_argument(
    "-filename", help="Path to the timecodes file you want to parse", type=str
)

args = parser.parse_args()


def parse(filepath: str):
    lap_times = {}
    name = []
    value = []
    race = ""

    # open file and fill the variables via python slicing
    with open(file=filepath, mode="r") as file:
        for index, lines in enumerate(file):
            strip = lines.strip()
            if index == 0:
                race = lines
            else:
                name.append(strip[:3])
                value.append(strip[3:])

    value = list(map(float, value))

    for key, value in zip(name, value):
        if key not in lap_times:
            lap_times[key] = []
        lap_times[key].append(value)

    return lap_times


myfile = parse(args.filename)

tabulate = print(tabulate(myfile, headers="keys", tablefmt="grid", numalign="left"))
