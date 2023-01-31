# numbers = [4,6,2,7,1]
# numbers.sort()
# print(numbers)

# names = ["Charlos","Ray","Alex","Kelly"]
# print(names)
# print(sorted(names))
# print(sorted(names,key = len))



# def get_event_date(event):
#     return event.date

# def current_users(events):
#     events.sort(key=get_event_date) # sorting by get_event_date value
#     machines = {}
#     for event in events: #iterate through list of  events
#         if event.machine not in machines: #check if the machine in the dictionary, if not add a empty set as the value
#             machines[event.machine] = set() #
#         if event.type == "login": #if type
#             machines[event.machine].add(event.user)
#         elif event.type == "logout":
#             machines[event.machine].remove(event.user)
#     return machines

# def generate_report(machines):
#     for machine, users in machines.items():
#         if len(users) > 0: #ensure that we don't print any machines where nobody is currently logged in
#             user_list = ", ".join(users)
#             print("{}: {}".format(machine,user_list))

# class Event:
#     def __init__(self,event_date,event_type,machine_name,user):
#         self.date = event_date
#         self.type = event_type
#         self.machine = machine_name
#         self.user = user
# events = [
#     Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
#     Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
#     Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
#     Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
#     Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
#     Event('2020-01-24 11:24:35', 'login', 'mailserver.local', 'chris')
# ]
# users = current_users(events)
# print(users)
# generate_report(users)

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
        if machines[event.machine]:
                machines[event.machine].remove(event.user)
        else:
                print(f"User {event.user} is not logged in")
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),# 
]

users = current_users(events)
print(users)
generate_report(users)


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            if machines[event.machine]:
                machines[event.machine].remove(event.user)
            else:
                print(f"User {event.user} is not logged in")
    return machines

def generate_report(machines):
    print("{:<20s} | {:>10s}".format("Machine", "Usernames"))
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{:<20s} | {:>10s}".format(machine, user_list))

class Event:
    def __init__(self,event_date,event_type,machine_name,user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
users = current_users(events)
print(users)
generate_report(users)

