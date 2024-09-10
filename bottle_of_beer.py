# Number of bottles
bottles = 99

# Loop through all the bottles down to 1
while bottles > 0:
    if bottles == 1:
        # Bottle for when 1 is left
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print(f"Take one down, pass it around, no more bottles of beer on the wall.\n")
    else:
        # Bottles for 2 or more
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(
            f"Take one down, pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n"
        )

    # Decrease the number of bottles by 1
    bottles -= 1

# input
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
