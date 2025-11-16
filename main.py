#include input file and output file
#merge dectint, octint, hexint into this file
from decint import is_decint
from hexint import is_hexint
from octint import is_octint
#from decint.py import def is_decint
#from hextint.py import def is_hexint
#from octint.py import def is_octint

#main function

def main():
    print("This is a program that recognizes Decinteger/Octinteger/Hexinteger.")
    print("1. Test your own text.")
    print("2. Batch Test from File")
    print("Enter 1/2 to choose the file.")
    choice = input().strip()

    if choice == "1":
        user_input = input("Enter a string.")
        if is_decint(user_input) or is_hexint(user_input) or is_octint(user_input):
            print("Accept")
        else:
            print("Reject")

    elif choice == "2":
        print("Run text file.")



if __name__ == "__main__":
    main()
