if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Grand Prix Timings Board",
        description="A program that visualizes timecodes from the Grand Prix",
    )

    parser.add_argument(
        "-filename",
        help="Path to the timecodes file you want to parse",
        type=str,
        nargs="?",
    )

    args = parser.parse_args()

    if args.filename is None:
        print("Please specify a file")
        parser.print_help()
        exit(-1)

race_name = ""


def parse(filepath: str):
    lap_times = {}
    name = []
    value = []

    # open file and fill the variables via python slicing
    try:
        open(file=filepath, mode="r")
        print("Reading file")

    except FileNotFoundError:
        print("File not found. Please check the path and try again")
        exit()

    with open(file=filepath, mode="r") as file:
        for index, lines in enumerate(file):
            strip = lines.strip()
            if index == 0:
                race_name = lines
            else:
                name.append(strip[:3])
                value.append(strip[3:])

        value = list(map(float, value))

        for key, value in zip(name, value):
            if key not in lap_times:
                lap_times[key] = []
            lap_times[key].append(value)

        return lap_times


# myfile = parse(R"D:\Scripts\uni\lbu-assignment-specs\Project-1\lap_times_1.txt")
myfile = parse(args.filename)
# tabulate = print(tabulate(myfile, headers="keys", tablefmt="grid", numalign="left"))


sorted_values = []
for keys, values in myfile.items():
    sorted_values = values.sort()
    print(f"Fastest lap time for {keys} is {values[0]}")
