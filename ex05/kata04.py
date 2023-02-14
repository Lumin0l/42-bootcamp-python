#
#
#
#
#
#
#

import sys

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04

def main():
	kata_p3_exp = "{:.2e}".format(kata[3])
	kata_p4_exp = "{:.2e}".format(kata[4])

	print(f"module_0{kata[0]}, ex_0{kata[1]} :  {kata[2]:.2f}, {kata_p3_exp}, {kata_p4_exp}")

if __name__ == '__main__':
	sys.exit(main())