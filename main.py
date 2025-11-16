#include input file and output file
#merge dectint, octint, hexint into this file

from decint import is_decint
from hexint import is_hexint
from octint import is_octint

#main function

def main():
    print("Enter 1/2")
    print("1. Enter String to Check")
    print("2. Check Test File")

    choice = input("Enter choice: ")

    if choice == '1':
        input_str = input("Enter string to check:")
        if is_decint(input_str) or is_octint(input_str) or is_hexint(input_str):
            print("Accept")
        else:
            print("Reject")

if "__name__" == "__main__":
    main()
