hotel = {
  '1': {
    '185': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""
              PPPPPPPPPP    Y       Y   TTTTTTTTTTT   H         H    OOOOOOOOO     N        N
              P         P    Y     Y         T        H         H   O         O    NN       N
              P         P     Y   Y          T        H         H   O         O    N  N     N
              P         P      Y Y           T        H         H   O         O    N   N    N
              PPPPPPPPPP        Y            T        HHHHHHHHHHH   O         O    N    N   N
              P                 Y            T        H         H   O         O    N     N  N
              P                 Y            T        H         H   O         O    N      N N
              P                 Y            T        H         H   O         O    N       NN
              P                 Y            T        H         H    OOOOOOOOO     N        N
              """)
    print("""
                       H         H    OOOOOOOOO   TTTTTTTTTTT  EEEEEEEEEEE   L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       HHHHHHHHHHH   O         O      T        EEEEEEE       L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H    OOOOOOOOO       T        EEEEEEEEEEE   LLLLLLLLLLL
              """)    
    check = int(input("\n\n______PYTHON___HOTEL______\n\nWhat would you like to do?\n0)Exit program\n1)Check-in\n2)Check-out\n3)Display guest list\n4)Check room occupany\n8)Clear\n> "))

    if check == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ncheck-in")
        room = int(input("Enter your room number: ")) #room has to start as integer for the greater than logic
        if 100 <= room <= 199:
            floor = "1"
        elif 200 <= room <= 299:
            floor = "2"
        elif 300 <= room <= 399:
            floor = "3"
        room = str(room) #changing room back to a string to get from dict
        if room in hotel[floor]:
            print("room unavailable")
            pass
        else:
            guests = []
            print("When finished hit enter or type stop")
            while True:
                guest = input("Enter guest name: ")
                hotel[floor][room] = guests
                if guest == "stop" or guest == "":
                    break
                else:
                    guests.append(guest)
                    pass
            x = ', '.join(guests)
            print(f"You have checked {x} into room {room}")

    elif check == 2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ncheck-out")
        room = int(input("Enter your room number: ")) #room has to start as integer for the greater than logic
        if 100 <= room <= 199:
            floor = "1"
        elif 200 <= room <= 299:
            floor = "2"
        elif 300 <= room <= 399:
            floor = "3"
        room = str(room) #changing room back to a string to get from dict
        if room not in hotel[floor]:
            print("Room not occupied")
            pass
        else: 
            hotel[floor].pop(room)
            print("\n*********************************************")
            print(f"  Room {room} has been checked-out.")
            print("  Thank you for your visit at Python Hotel")
            print("*********************************************")
    
    elif check == 0:
        print("Goodbye")
        break
    elif check == 3:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCurrent Guest List\n==================")
        for floor, rooms in hotel.items():
            for room, occupants in rooms.items():
                print(f"{', '.join(occupants)}")
    elif check == 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOccupied Rooms")
        for floor, rooms in hotel.items():
            print(f"\nFloor {floor}")
            for room, occupants in rooms.items():
                print(f"{room}")
    elif check == 8:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("""
              PPPPPPPPPP    Y       Y   TTTTTTTTTTT   H         H    OOOOOOOOO     N        N
              P         P    Y     Y         T        H         H   O         O    NN       N
              P         P     Y   Y          T        H         H   O         O    N  N     N
              P         P      Y Y           T        H         H   O         O    N   N    N
              PPPPPPPPPP        Y            T        HHHHHHHHHHH   O         O    N    N   N
              P                 Y            T        H         H   O         O    N     N  N
              P                 Y            T        H         H   O         O    N      N N
              P                 Y            T        H         H   O         O    N       NN
              P                 Y            T        H         H    OOOOOOOOO     N        N
              """)
        print("""
                       H         H    OOOOOOOOO   TTTTTTTTTTT  EEEEEEEEEEE   L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       HHHHHHHHHHH   O         O      T        EEEEEEE       L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H   O         O      T        E             L
                       H         H    OOOOOOOOO       T        EEEEEEEEEEE   LLLLLLLLLLL
              """)
    elif check == 9:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for floor, rooms in hotel.items():
            print(f"\nFloor {floor}")
            for room, occupants in rooms.items():
                print(f"Room {room}: {', '.join(occupants)}")