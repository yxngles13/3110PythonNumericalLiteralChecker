from decint import is_decint
from hexint import is_hexint
from octint import is_octint
from floating import is_floatingpoint

def check_numbers(s):
    state = ""
    if is_decint(s) or is_octint(s) or is_hexint(s) or is_floatingpoint(s):
        state = "Accept"
    else:
        state = "Reject"
    return state


def main():
    while True:
        print("---------Welcome to Python Numerical Literal Checker---------")
        print("1. Enter String to Check")
        print("2. Check Test File")
        print("Enter q to quit")
        choice = input("Enter choice: ").strip()

        if choice.lower() == 'q':
            print("\nEnd of program.")
            break

        elif choice == '1':
            input_str = input("Enter string to check: ").strip()
            print(check_numbers(input_str))
            

        elif choice == '2':
            input_file = "in_ans.txt"
            output_file = "out.txt"

            with open(input_file, "r") as filein:
                lines = [line.strip() for line in filein if line.strip()]
            
            with open(output_file, "w") as fileout:
                fileout.write("Input                                        Expected                Actual                  Result\n")
                for line in lines:
                    parts = line.split()
                    
                    number = parts[0]
                    expected = parts[1]

                    actual = check_numbers(number)
                    results = "PASS" if actual == expected else "FAIL"

                    fileout.write(f"{number}                                        {expected}                  {actual}            {results}\n")
            
            print("Testing Finished.")
                  

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
