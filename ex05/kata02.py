#
#
#
#
#
#

import sys
import datetime

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

# The format codes are standard directives for mentioning in which format you want to represent datetime. 
# For example, the %d-%m-%Y %H:%M:%S codes convert date to dd-mm-yyyy hh:mm:ss format.

""" def main():
    kata_string = str(kata)
    print_time = datetime.datetime.strptime(kata_string, '%Y, %m, %d, %H, %M').strftime('%Y/%m/%d %H:%M')
    print(f"{print_time}") """

def main():
    kata_string = str(kata)

    print(type(kata_string))
    print(kata_string)
    #esta preguntar
    print(f"0{kata[1]}/{kata[2]}/{kata[0]} {kata[3]}:{kata[4]}")

if __name__ == '__main__':
    sys.exit(main())