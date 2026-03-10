from typing import List, Tuple

Interval = Tuple[str, int, int]

"""
This function returns a maximum subset of compatible jobs/time intervals. Compatible jobs do not overlap in time. 
"""
def interval_scheduling(intervals: List[Interval]) -> List[Interval]:
    # step 1: sort by finish time
    intervals.sort(key=lambda interval: interval[2])
    sorted_intervals = intervals

    # keeping track
    interval_count = 0
    end_interval = 0
    selected_set: List[Interval] = []

    # step 2: traverse the list of intervals
    for interval in sorted_intervals:
      # the interval starting times are >= the previous interval ending times
      if (end_interval <= interval[1]):
        end_interval = interval[2]
        # count the interval
        interval_count += 1
        # take the interval
        selected_set.append(interval)
    return selected_set


def main() -> None:
    intervals = [("A", 0, 7), ("B", 1, 4), ("C", 3, 5), ("D", 3, 8), ("E", 4, 7), ("F", 5, 9), ("G", 6, 10), ("H", 8, 11)]

    print("Original intervals: ")
    print(intervals, "\n")

    result = interval_scheduling(intervals)

    print("Selected compatible intervals:")
    print(result)

    print("\nNumber selected:")
    print(len(result), "\n")


if __name__ == "__main__":
    main()
