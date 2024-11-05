def main():
    flowers = []
    # user input for list of flower
    print("Enter flower names one by one. Type 'done' when finished. ")
    while True:
        flower = input("Enter a flower name and type 'done' to finish: ")
        if flower.lower() == 'done':
            break
        elif flower:
            flowers.append(flower)

    # sort the list
    flowers.sort()
    print("\nSored list of flowers: ")
    for i, flower in enumerate(flowers, start=1):
        print(f"{i}. {flower}")

    # search flowers in the list
    search_flower = input("\nEnter a flower name to search for: ")
    if search_flower in flowers:
        print(f"{search_flower} is in the list. ")
    else:
        print(f"{search_flower} was not found in the list.")

    # specifi flower by number
    while True:
        try:
            flower_number = int(
                input("\nEnter the number of a flower to view:   "))
            if 1 <= flower_number <= len(flowers):
                print(f"The flower at  position {flower_number} is : {
                      flowers[flower_number - 1]}")
                break
            else:
                print("Number out of range. Please try again")
        except ValueError:
            print("Invalid input. Please enter a number. ")
        except IndexError:
            print("Index out of range. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


main()
