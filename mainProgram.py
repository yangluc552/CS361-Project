import random
import sys
import time


def get_ascii_title():

    ascii_title = r"""
    ___  ___ _  _    __ __ __  __ __ ______      ___   ___   __  __ __ __  ____ ____  ______  ____ ____ 
    ||\\//|| \\//    || || ||\ || || | || |     //    // \\  ||\ || || || ||    || \\ | || | ||    || \\
    || \/ ||  )/     || || ||\\|| ||   ||      ((    ((   )) ||\\|| \\ // ||==  ||_//   ||   ||==  ||_//
    ||    || //      \\_// || \|| ||   ||       \\__  \\_//  || \||  \V/  ||___ || \\   ||   ||___ || \\

        """
    return ascii_title


def print_ascii_title():
    """Prints the ascii title"""
    print(get_ascii_title())

print_ascii_title()
print("""           CONVERT ANY UNIT TYPE TO ANOTHER! KEEP TRACK OF YOUR CONVERSIONS! NOW GO AND CONVERT!""")

def home_page_instructions():
    print("\nCONTROLS: ")
    print("Type Length(l), Weight(w), Volume(v) for which unit your are trying to convert")
    print("Type About(a) to learn more about this program enter ")
    print("Type Quit(q) to exit the program ")
    print("Type which unit you want to convert to, use the abbreviation of the unit.")
    print("Type in the amount of your unit you have.")
    print("Type 'ENTER' to submit your unit and convert it.\n")



def userResponse():   
    while True:
        home_page_instructions()
        user_unit = input("What would you like to do? [Length(l), Weight(w), Volume(v), About(a), Quit(q)]")

        if user_unit == 'w':
            user_response_W()
        elif user_unit == 'l':
            user_response_L()
        elif user_unit == 'v':
            user_response_V()
        elif user_unit.lower() == user_unit.lower() == 'a':
            print_about()
        elif user_unit.lower() == 'q':
            confirm = input("Are you sure you want to quit? (y/n): ")
            if confirm.lower() == 'y':
                print("Exiting the program. Goodbye!")
                break
            elif confirm.lower() == 'n':
                continue
        else:
            print("Invalid choice! Please choose from 'l', 'w', or 'v'.")
            userResponse()


def user_response_W(): 
    from_unit = input("Enter the unit you have (g, kg, lb, oz): ").lower()
    to_unit = input("Enter the unit you want to convert to (g, kg, lb, oz): ").lower()
    amount = float(input("Enter the amount of you have: "))
    print("\nPlease wait till the conversion is finished\n")
    result = weight_converter(amount, from_unit, to_unit)
    print(f"Got it here is the conversion {amount} {from_unit} is equal to {result} {to_unit} \n")



def weight_converter(amount, from_unit, to_unit):
    # Dictionary containing conversion factors
    conversion_factors = {
        'g': {'g': 1, 'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
        'kg': {'g': 1000, 'kg': 1, 'lb': 2.20462, 'oz': 35.274},
        'lb': {'g': 453.592, 'kg': 0.453592, 'lb': 1, 'oz': 16},
        'oz': {'g': 28.3495, 'kg': 0.0283495, 'lb': 0.0625, 'oz': 1}
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid unit(s)"

    converted_amount = amount * conversion_factors[from_unit][to_unit]
    return converted_amount


def user_response_L(): 
    from_unit = input("Enter the unit you have (m, cm, km, in, ft): ").lower()
    to_unit = input("Enter the unit you want to convert to (m, cm, km, in, ft): ").lower()
    amount = float(input("Enter the amount: "))
    print("\nPlease wait till the conversion is finished\n")
    result = length_converter(amount, from_unit, to_unit)
    print(f"Got it here is the conversion {amount} {from_unit} is equal to {result} {to_unit} \n")


def length_converter(amount, from_unit, to_unit):
    # Dictionary containing conversion factors
    conversion_factors = {
        'm': {'m': 1, 'cm': 100, 'km': 0.001, 'in': 39.3701, 'ft': 3.28084},
        'cm': {'m': 0.01, 'cm': 1, 'km': 0.00001, 'in': 0.393701, 'ft': 0.0328084},
        'km': {'m': 1000, 'cm': 100000, 'km': 1, 'in': 39370.1, 'ft': 3280.84},
        'in': {'m': 0.0254, 'cm': 2.54, 'km': 0.0000254, 'in': 1, 'ft': 0.0833333},
        'ft': {'m': 0.3048, 'cm': 30.48, 'km': 0.0003048, 'in': 12, 'ft': 1}
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid unit(s)"

    converted_amount = amount * conversion_factors[from_unit][to_unit]
    return converted_amount


def user_response_V(): 
    from_unit = input("Enter the unit you have (m^3, cm^3, liter, gallon, pint): ").lower()
    to_unit = input("Enter the unit you want to convert to (m^3, cm^3, liter, gallon, pint: ").lower()
    amount = float(input("Enter the amount: "))
    print("\nPlease wait till the conversion is finished\n")
    result = volume_converter(amount, from_unit, to_unit)
    print(f"Got it, here is the conversion: {amount} {from_unit} is equal to {result} {to_unit} \n")


def volume_converter(amount, from_unit, to_unit):
    # Dictionary containing conversion factors
    conversion_factors = {
        'm^3': {'m^3': 1, 'cm^3': 1000000, 'liter': 1000, 'gallon': 264.172, 'pint': 2113.38},
        'cm^3': {'m^3': 0.000001, 'cm^3': 1, 'liter': 0.001, 'gallon': 0.000264172, 'pint': 0.00211338},
        'liter': {'m^3': 0.001, 'cm^3': 1000, 'liter': 1, 'gallon': 0.264172, 'pint': 2.11338},
        'gallon': {'m^3': 0.00378541, 'cm^3': 3785.41, 'liter': 3.78541, 'gallon': 1, 'pint': 8},
        'pint': {'m^3': 0.000473176, 'cm^3': 473.176, 'liter': 0.473176, 'gallon': 0.125, 'pint': 1}
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid unit(s)"
        

    converted_amount = amount * conversion_factors[from_unit][to_unit]
    return converted_amount


def print_about():
    print("""\nWhen I created this program I wanted to create a simple and easy way to get basic conversions that will help users.
I wanted to make sure that all the information would be in one place so that way you wouldn't have to switch around to find 
what kind of measurement you wanted. By having all kinds of measurements available a user can just use this application to 
get what they want.

I hope you enjoy the program! 
""")

userResponse()
