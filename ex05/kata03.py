#
#
#
#
#
#

import sys

# Put this at the top of your kata03.py file
kata = "The right format"

def main():
	for i in range(-26, 16):
		if i < 0:
			sys.stdout.write('-')
		else:
			sys.stdout.write(kata[i])

if __name__ == '__main__':
	sys.exit(main())