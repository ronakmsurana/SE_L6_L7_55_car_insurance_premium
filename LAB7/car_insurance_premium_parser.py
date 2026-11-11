def normalize_registration(plate):
    """
    Removes spaces and dashes from a registration number and upper-cases it.
    Assumes plate is a non-empty string.
    """
    plate = plate.strip().upper()
    for ch in [' ', '-', '.']:
        plate = plate.replace(ch, '')
    return plate

def total_claim_amount(text):
    """
    Adds up claim amounts separated by semicolons.
    Assumes every amount is a whole number.
    """
    return sum(int(amount) for amount in text.split(';'))

def driver_age(dob, current_year=2026):
    """
    Works out the driver's age from a DD/MM/YYYY date of birth.
    Assumes dob always has three parts separated by '/'.
    """
    return current_year - int(dob.split('/')[2])

def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    print("Driver age in 2026:", driver_age(value))

if __name__ == "__main__":
    main()
