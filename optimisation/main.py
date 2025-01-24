import json
from enum import Enum
from typing import List
from datetime import datetime

# TYPES

class WeekDay(Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"

class Activity:
    def __init__(self, week_day: WeekDay, start_hour: int, hour_duration: int, money: float, fun: float):
        self.week_day = week_day
        self.start_hour = start_hour
        self.hour_duration = hour_duration
        self.money = money
        self.fun = fun

    @staticmethod
    def deserialize(data: dict):
        return Activity(
            WeekDay(data["week_day"]),
            data["start_hour"],
            data["hour_duration"],
            data["money"],
            data["fun"]
        )

class Possibilities:
    def __init__(self, activities: List[Activity]):
        self.activities = activities

    @staticmethod
    def deserialize(data: dict):
        activities = [Activity.deserialize(item) for item in data["activities"]]
        return Possibilities(activities)
    
# UTILS

def getIdx(weekDay: WeekDay) -> int:
    if (WeekDay(weekDay) == WeekDay.Mon): return 1
    if (WeekDay(weekDay) == WeekDay.Tue): return 2
    if (WeekDay(weekDay) == WeekDay.Wed): return 3
    if (WeekDay(weekDay) == WeekDay.Thu): return 4
    if (WeekDay(weekDay) == WeekDay.Fri): return 5
    if (WeekDay(weekDay) == WeekDay.Sat): return 6
    if (WeekDay(weekDay) == WeekDay.Sun): return 7

activities = []

def print_activities(activities):
    for activity in activities:
        print('week_day: ' + activity.week_day + ' start_hour: ' + str(activity.start_hour) + ' hour_duration: ' + str(activity.hour_duration) + ' money: ' + str(activity.money) + ' fun: ' + str(activity.fun) + '\n')

def print_fun(activities=activities):
    fun = 0
    for e in activities:
        fun += e.fun
    print('Fun: ' + str(fun))

def print_money(activities=activities):
    money = 0
    for e in activities:
        money += e.money
    print('Money: ' + str(money))

def sortingKey(e: Activity):
    return datetime(2020, 1, getIdx(e.week_day), e.start_hour)

# DATA EXTRACTION

with open('input/small.json', 'r') as file:
    data = json.load(file)

for e in data:
    activity = Activity(e['week_day'], e['start_hour'], e['hour_duration'], e['money'], e['fun'])
    activities.append(activity)    


# ALGO 1
def algo1():
    activities.sort(key=sortingKey)
    print_activities(activities)

    fun_activities = [e for e in activities if e.fun > 0]

    idxToRemove = []
    for i, e in enumerate(fun_activities):
        if i == 0 or i - 1 in idxToRemove:
            continue
        
        previous_activity = fun_activities[i - 1]
        end_time_prev = datetime(2020, 1, getIdx(previous_activity.week_day), previous_activity.start_hour + previous_activity.hour_duration)
        start_time_curr = datetime(2020, 1, getIdx(e.week_day), e.start_hour)

        print(end_time_prev)
        print(start_time_curr)
        
        if end_time_prev < start_time_curr:
            continue
        else:
            if previous_activity.fun < e.fun:
                # fun_activities.remove(previous_activity)
                idxToRemove.append(i - 1)
            else:
                # fun_activities.remove(e)
                idxToRemove.append(i)
    
    fun_activities = [e for i, e in enumerate(fun_activities) if i not in idxToRemove]

    return fun_activities

print_fun()
res = algo1()
print_activities(res)
print_fun(res)
print_money(res)

