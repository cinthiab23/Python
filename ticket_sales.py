# Available seats  20
available_seat = list(range(1, 21))

print("\nAvailable seats:")
print(", ".join(map(str, available_seat)))

while True:
    seat = input("\nEnter the seat number ( or 'o' to finish):")
    if seat == "0":
        # Exit when customer enters 0
        print("Thank you for you purchase")
        break

    if seat in available_seat:
        seat = int(seat)
        available_seat.remove(seat)
        print(f"Seat {seat} has been reserved.")
    else:
        print(f"Seat{seat} is not avilable ")

    print("\nAvailable seats:")
    print(", ".join(map(str, available_seat)))
