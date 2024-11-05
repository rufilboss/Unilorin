import math

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def display_menu():
    print("\n=== Radian <-> Degree Converter ===")
    print("1. Convert Radians to Degrees")
    print("2. Convert Degrees to Radians")
    print("3. Exit")
    print("===================================")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1, 2, or 3): ").strip()

        if choice == '1':
            try:
                radians = float(input("Enter the value in radians: ").strip())
                degrees = radians_to_degrees(radians)
                print(f"{radians} radians is {degrees:.4f} degrees.\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")

        elif choice == '2':
            try:
                degrees = float(input("Enter the value in degrees: ").strip())
                radians = degrees_to_radians(degrees)
                print(f"{degrees} degrees is {radians:.4f} radians.\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")

        elif choice == '3':
            print("Thank you for using this converter developed by ILYAS RUFAI. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
    