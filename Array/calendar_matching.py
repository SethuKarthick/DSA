calendar1 = [
  ["9:00", "10:30"],
  ["12:00", "13:00"],
  ["16:00", "18:00"]
]
dailyBounds1 = ["9:00", "20:00"]

calendar2 = [
  ["10:00", "11:30"],
  ["12:30", "14:30"],
  ["14:30", "15:00"],
  ["16:00", "17:00"]
]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30

def calendar_matching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updated_calendar_one = update_calendar(calendar1, dailyBounds1)
    updated_calendar_two = update_calendar(calendar2, dailyBounds2)
    merged_calendar = merge_calendars(updated_calendar_one, updated_calendar_two)
    flattened_calendar = flatten_calendar(merged_calendar)
    res = get_free_timings(flattened_calendar, meetingDuration)
    return res

def update_calendar(calendar, dailyBounds):
    updated_calendar = [["0:00", dailyBounds[0]]] + calendar + [[dailyBounds[1], "23:59"]]
    return [[time_to_minutes(start), time_to_minutes(end)] for start, end in updated_calendar]

def merge_calendars(calendar1, calendar2):
    merged_calendar = calendar1 + calendar2
    merged_calendar.sort(key=lambda x : x[0])
    return merged_calendar

def flatten_calendar(calendar):
    flattened_calendar = [calendar[0][:]]

    for i in range(1, len(calendar)):
        prev = flattened_calendar[-1]
        current = calendar[i]

        if current[0] <= prev[1]:
            prev[1] = max(current[1], prev[1])
        else:
            flattened_calendar.append(current[:])
    return flattened_calendar

def get_free_timings(flattened_calendar, meetingDuration):
    result = []

    for i in range(1, len(flattened_calendar)):
        start = flattened_calendar[i-1][1]
        end = flattened_calendar[i][0]

        if end - start >= meetingDuration:
            result.append([minutes_to_time(start), minutes_to_time(end)])

    return result

def time_to_minutes(time_str):
    hr, minutes = map(int,time_str.split(":"))
    return hr*60 + minutes

def minutes_to_time(minutes):
    hr = minutes // 60
    m = minutes % 60
    return f"{hr}:{str(m).zfill(2)}"


res = calendar_matching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
print(res)
