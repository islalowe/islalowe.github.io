# Interval Scheduling

## Problem
Given a set of jobs, find the maximum number that take place compatibly. Each job starts at start time, `s_j` and finishes at finish time, `f_j`. Compatible jobs do not overlap. 

Example intervals:
- A: (0, 7)
- B: (1, 4)
- C: (3, 5)
- D: (3, 8)
- E: (4, 7)
- F: (5, 9)
- G: (6, 10)
- H: (8, 11)

This problem requires finding the maximum subset of compatible jobs. The solution runs in O(nlogn) time.

## Greedy Idea
Consider jobs in chronological order. Take each job provided it's compatible with the ones already taken.
There are multiple options for priorititizing which jobs to take: 
- *Earliest start time:*  Consider jobs in ascending order of start time `s_j`.
- *Earliest finish time:* Consider jobs in ascending order of finish time `f_j`.
- *Shortest interval:* Consider jobs in ascending order of interval length  `f_j` - `s_j`.
- *Fewest conflicts:* For each job, count the number of conflicting jobs `c_j`. Schedule in ascending order of conflicts `c_j`.

The method chosen:
Choosing the earliest finishing interval. This option leaves as much room as possible for future intervals.

## Algorithm
1. Sort intervals by finish time
2. Pick the first interval
3. Repeatedly pick the next interval whose start time is at least the finish time of the last chosen interval

## Pseudocode
```text
Sort jobs by finish times so that f1 ≤ f2 ≤ ... ≤ fn.
IntervalScheduling(jobs):
    A ← ∅
    last_finish ← -∞

    for j = 1 to n:
        if S_j ≥ last_finish:
            add job j to A
            last_finish ← F_j

    return A
```