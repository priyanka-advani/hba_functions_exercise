"""
This is Part 4 of the Hackbright Prep functions exercise 
 """


def calculate_tip(bill_amt, tip_percentage):
    """Given the bill amount and tip percentage, calculates the tip."""

    # ENTER YOUR CODE HERE

    tip_amt = bill_amt * tip_percentage
    return tip_amt


def calculate_total(bill_amt, tip_amt):
    """Given the tip amount and the bill amount, calculates the total bill."""

    # ENTER YOUR CODE HERE

    total = bill_amt + tip_amt
    return total


def split_bill(total, number_of_people):
    """Given the bill total and the number of people, calculates the total per person."""

    # ENTER YOUR CODE HERE

    total_per_person = total / number_of_people
    return total_per_person


def total_per_person():
    """Gets user input for bill amount, tip %, and # of people. Returns total per person.

    This function should:
    1. Get user input for the bill amount, tip percentage, and # of people
    2. Calculate the tip amount and save it to a variable.
    3. Using the tip amount calculated above, find the total bill amount.
    4. Using the total found above, calculate the total per person. 
    """

    # ENTER YOUR CODE HERE
    
    bill_amt = int(raw_input("Enter bill amount: "))
    tip_percentage = float(raw_input("Enter tip percentage: "))
    number_of_people = int(raw_input("Enter number of people: "))

    tip_amt = calculate_tip(bill_amt, tip_percentage)
    total = calculate_total(bill_amt, tip_amt)
    per_person = split_bill(total, number_of_people)

    return per_person


##############################################################################
# Don't touch the code below, this will allow us to run the total_per_person function when we
# run our python file in the terminal using `python bill-calculator.py`

if __name__ == "__main__":
    print total_per_person()