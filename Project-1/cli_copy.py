from rich.console import Console
from rich.table import Table
from rich import box
from rich import print as rprint

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
    parser.add_argument(
        "-sort",
        help="Create sorted tables (disabled by default)",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()

    if args.filename is None:
        print("Please specify a file")
        parser.print_help()
        exit(-1)


def parse(filepath: str):
    lap_times = {}
    name = []
    value = []
    global race_name
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


myfile = parse(args.filename)


console = Console()

table = Table(title=f"{race_name}", box=box.DOUBLE_EDGE)

for keys, value in myfile.items():
    table.add_column(f"{keys}")


max_rows = max(len(value) for value in myfile.values())


for i in range(max_rows):
    row = []  # new list with string values so that rich can render it
    for key, values in myfile.items():
        # highlighting the fastest and slowest laps
        if args.sort is True:
            values = sorted(values)
        maxx = max(values)
        minn = min(values)
        avg = sum(values) / len(values)

        if values[i] == maxx if i < len(values) else None:
            row.append(f"[bold red]{str(values[i]) if i < len(values) else ""}")

        elif values[i] == minn if i < len(values) else None:
            row.append(f"[bold green]{str(values[i]) if i < len(values) else ""}")

        elif i == len(values):  # if you reach the end of list, append the avg value
            row.append(f"AVG:[bold uu]{avg:.3f}")

        else:
            row.append(str(values[i]) if i < len(values) else "")

    table.add_row(*row)


console.print(table)


def find_fastest(input: dict):
    lowest_key, lowest_value = min(input.items(), key=lambda item: min(item[1]))

    rprint(
        f"The fastest driver is [bold green]{lowest_key}[/bold green] with the time [bold green]{lowest_value[0]}"
    )


find_fastest(myfile)
