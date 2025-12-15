#Mohammad Amin
#SCSJ2500448

def user_profile():
    print("\n==Please enter your details==")
    name = input("Your name? : ")
    age = int(input("Your age? : "))
    membership_type = input("Enter your membership type : ")
    
    if age < 12:
        print("Not eligible for membership")
    elif 12 <= age <= 60:
        print("Standard Membership Granted")
    else:
        print("Senior membership granted")

def booking_session():
    print("\n==Enter your booking time==") 
    time = int(input("Your time? : ")) 
    session = input("Your session : ") #use alphabets A,B,C etc... 
    
    print(f"You have booked session {session} successfully!")

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. User Profile")
        print("2. Booking Session")
        print("3. Exit System")
        print("=================")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            user_profile()
        elif choice == 2:
            booking_session()
        elif choice == 3:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()

