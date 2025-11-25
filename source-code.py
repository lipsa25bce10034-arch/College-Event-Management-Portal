# College Event Management Portal 

events = ["Coding Hackathon", "Poster Presentation", "Robotics Workshop"]
participants = []

def show_events():
    print("\n--- Upcoming College Events ---")
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event}")
    print()

def register_student():
    show_events()
    try:
        choice = int(input("Enter event number to join: "))
        if choice < 1 or choice > len(events):
            print("Invalid choice.\n")
            return
    except:
        print("Please enter a number.\n")
        return

    name = input("Enter your name: ")
    roll = input("Enter your roll number: ")

    participants.append({
        "name": name,
        "roll": roll,
        "event": events[choice - 1]
    })

    print("\nRegistration Successful!\n")

def view_participants():
    print("\n--- Participant List ---")
    if len(participants) == 0:
        print("No registrations yet.\n")
        return

    for p in participants:
        print(f"Name: {p['name']}, Roll: {p['roll']}, Event: {p['event']}")
    print()

def main():
    while True:
        print("1. View Events")
        print("2. Register for Event")
        print("3. View Participants")
        print("4. Exit")

        try:
            option = int(input("Enter your choice: "))
        except:
            print("Invalid input.\n")
            continue

        if option == 1:
            show_events()
        elif option == 2:
            register_student()
        elif option == 3:
            view_participants()
        elif option == 4:
            print("Thank you for using the portal!")
            break
        else:
            print("Invalid choice.\n")

main()
