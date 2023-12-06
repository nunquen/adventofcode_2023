from typing import List

debug = False


def get_best_times(
    time: int,
    distance: int
) -> List[int]:
    best_times = []

    for t in range(time + 1):
        if t == 0:
            continue

        speed = t
        possible_distance = speed * (time - t)
        if possible_distance > distance:
            best_times.append(possible_distance)

    return best_times


def get_the_number(input_data: List) -> int:
    the_number = 1
    for race in input_data:
        best_times = get_best_times(
            time=race["Time"],
            distance=race["Distance"]
            )
        the_number *= len(best_times)

    return the_number
