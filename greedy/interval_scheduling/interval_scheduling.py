from typing import List, Tuple

Interval = Tuple[string, int, int]

"""
This function returns a maximum subset of compatible jobs/time intervals. Compatible jobs do not overlap in time. 
"""
def interval_scheduling(intervals: List[Interval]) -> List[Interval]:
    # step 1: sort by finish time
    sorted_intervals = intervals.sort(intervals, key=lambda interval: interval[2])

    # keeping track
    count_intervals = 0
    end_intervals = 0
    selected_set: List[Interval] = []

    # step 2: traverse the list of intervals
    for interval in intervals:
      # the interval starting times are >= the previous interval ending times
      if (end <= interval[1]):
        end = interval[2]
        # count the interval
        count += 1
        # take the interval
        selected_set.append(interval)


def main() -> None:
    intervals = [("A", 0, 7), ("B", 1, 4), ("C", 3, 5), ("D", 3, 8), ("E", 4, 7), ("F", 5, 9), ("G", 6, 10), ("H", 8, 11)]

    print("Original intervals: ")
    print(intervals, "\n")

    result = interval_scheduling(intervals)

    print("Selected compatible intervals:")
    print(result, "\n")

    print("\nNumber selected:")
    print(len(result, "\n"))


if __name__ == "__main__":
    main()
