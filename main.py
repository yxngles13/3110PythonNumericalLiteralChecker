#include input file and output file
#merge dectint, octint, hexint into this file

from decint import is_decint
from hexint import is_hexint
from octint import is_octint
from floating import is_floatingpoint

#main function

def main():
    while True:
        print("---------Welcome to Python Numerical Literal Checker:---------")
        print("1. Enter String to Check")
        print("2. Check Test File")
        print("Enter q to quit")
        choice = input("Enter choice: ")

        if choice == 'q':
            print("\nEnd of program.")
            break
        elif choice == '1':
            input_str = input("Enter string to check:")
            if is_decint(input_str) or is_octint(input_str) or is_hexint(input_str) or is_floatingpoint(input_str):
                print("\nAccept")
            else:
                print("\nReject")            
        

if __name__ == "__main__":
    main()
