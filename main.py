#include input file and output file
#merge dectint, octint, hexint into this file

#from decint.py import def is_decint
#from hextint.py import def is_hexint
#from octint.py import def is_octint

#main function

def main():

#open input file

#(input file testcases is in format: 1234 accept)
#read first string on line (test case)
#check if the string is hexint or octint (check string for 0x/0o prefix)
    #if hextint, call is_hexint function
    #if octint, call is_octint function
    #if neither, call is_decint function

#based on if the functions give true=accept, false=reject
#write to output file the same input (1234 accept) and append actual result (accept/reject)
        #should look like (1234 accept accept)

#if both expected and actual results are accept or both are reject, add "PASS" to end of line
        #should look like (1234 accept accept PASS)
        #else add "FAIL" to end of line


