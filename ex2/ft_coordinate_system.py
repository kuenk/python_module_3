import sys
import math


def cal_distance(start, data):
    """Calculate the distance between start and input"""
    result = math.sqrt((data[0] - start[0])**2 +
                       (data[1] - start[1])**2 +
                       (data[2] - start[2])**2)
    return (result)


def check_input(input_data):
    """Check input parse the input and return the error"""
    is_string = False
    if not input_data:
        raise IndexError("The input is empty. "
                         "Please write 3 number cordinates")
    if len(input_data) == 1 and "," in input_data[0]:
        is_string = True
        input_data = input_data[0].split(",")
    elif len(input_data) != 3:
        raise ValueError("Please, put 3 cordinates. "
                         "No more or less")

    temp_list = [0] * 3
    for i in range(3):
        try:
            val = int(input_data[i])
            if val < 0:
                raise ValueError("Please write 3 "
                                 "positive numbers")
            temp_list[i] = val
        except ValueError as e:
            if "positive" in str(e):
                raise e
            print(f"Parsing invalid coordinates: {input_data}")
            raise ValueError(f"Error parsing coordinates: invalid literal "
                             f"for int() with base 10: {input_data[i]}")
    return (tuple(temp_list), is_string)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    try:
        data, is_string = check_input(sys.argv[1:])
        if is_string:
            print(f"Parsing coordinates: {sys.argv[1:]}")
            print(f"Parsed position: {data}")
        else:
            print(f"Position created: {data}")

        start = (0, 0, 0)
        result = cal_distance(start, data)

        print(f"Distance between {start} and {data}: {result}")
        x, y, z = data
        print("Unpacking demostration:")
        print(f"Player at x={x}, y={y}, z={z}")
    except (IndexError, ValueError) as e:
        print(f"{e}")
