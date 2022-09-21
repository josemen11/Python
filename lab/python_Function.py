from datetime import timedelta, datetime
def rocket_parts():
    print("payload, propellant, structure")
    
rocket_parts()    


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))
total_days = days_to_complete(238855, 75)
print(round(total_days))      




def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

def variable_length(*args):
    print(args)

variable_length("one", "two")    


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
print(sequence_time(4, 14, 18))    