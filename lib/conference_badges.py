def badge_maker(name):
    message = f"Hello, my name is {name}."
    return message

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges

def assign_rooms(names):
    assignments = []
    room_number = 1
    for name in names:
        assignment = f"Hello, {name}! You'll be assigned to room {room_number}!"
        assignments.append(assignment)
        room_number += 1
    return assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)
