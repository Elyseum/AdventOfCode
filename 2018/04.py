"""Puzzle 04."""

import datetime
import re
from collections import Counter
from itertools import groupby

class ReposeRecord:
    """Repose records of a single day."""

    def __init__(self, line):
        date_str = re.search(r"\[(.+)\].+", line)[1]
        self.date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        self.guard = int(re.search(r".+\#(\d+).+", line)[1]) if '#' in line else None
        self.wakes_up = True if 'wakes up' in line else False
        self.falls_asleep = True if 'falls asleep' in line else False

def read_repose_record(file_name):
    with open(file_name) as file:
        return file.readlines()

def parse_repose_record(lines):
    return [ReposeRecord(line) for line in sorted(lines)]

def get_sleep_minutes_per_guard(sorted_records):
    guard = None
    sleep_start = None
    minutes_per_guard = dict()
    for record in sorted_records:
        if record.guard:
            guard = record.guard
        elif record.falls_asleep:
            sleep_start = record.date
        elif record.wakes_up:
            minuts_asleep = range(sleep_start.minute, record.date.minute)
            minutes_per_guard.setdefault(guard, []).extend(minuts_asleep)
            sleep_start = None
    return minutes_per_guard

REPOSE_RECORDS_LINES_EXAMPLE = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep          ",
    "[1518-11-01 00:25] wakes up              ",
    "[1518-11-01 00:30] falls asleep          ",
    "[1518-11-01 00:55] wakes up              ",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep          ",
    "[1518-11-02 00:50] wakes up              ",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep          ",
    "[1518-11-03 00:29] wakes up              ",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep          ",
    "[1518-11-04 00:46] wakes up              ",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep          ",
    "[1518-11-05 00:55] wakes up              "
]

def puzzle4_1(records):
    sleep_min_per_guard = get_sleep_minutes_per_guard(records).items()
    longest_sleeping = sorted(sleep_min_per_guard, key=lambda x: len(x[1]))[-1]
    guard = longest_sleeping[0]
    print(f"Longest sleeping guard: {guard}")
    minute_times = Counter(longest_sleeping[1]).most_common(1)[0]
    minute = minute_times[0]
    times = minute_times[1]
    print(f"Most frequent minute asleep: {minute}, {times} times")
    return guard * minute

REPOSE_RECORDS_EXAMPLE = parse_repose_record(REPOSE_RECORDS_LINES_EXAMPLE)
print(f"Puzzle 4 (part 1) example: {puzzle4_1(REPOSE_RECORDS_EXAMPLE)}")

REPOSE_RECORDS = parse_repose_record(read_repose_record("04.txt"))
print(f"Puzzle 4 (part 1): {puzzle4_1(REPOSE_RECORDS)}")

def minute_most_asleep(guard_minutes):
    guard = guard_minutes[0]
    minutes = guard_minutes[1]
    minute_most_asleep = Counter(minutes).most_common(1)[0]
    minute = minute_most_asleep[0]
    times_asleep = minute_most_asleep[1]
    return (guard, minute, times_asleep)

def puzzle4_2(records):
    sleep_min_per_guard = get_sleep_minutes_per_guard(records).items()
    min_most_asleep_guard = map(minute_most_asleep, sleep_min_per_guard)
    longest_asleep = sorted(min_most_asleep_guard, key=lambda x: x[2])[-1]
    return longest_asleep[0] * longest_asleep[1]

print(f"Puzzle 4 (part 2) example: {puzzle4_2(REPOSE_RECORDS_EXAMPLE)}")
print(f"Puzzle 4 (part 2): {puzzle4_2(REPOSE_RECORDS)}")