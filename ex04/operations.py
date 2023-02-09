# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/07 15:37:38 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/09 15:40:39 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

def operations(num_1, num_2):
	print(f"Sum: {num_1+num_2}")
	print(f"Difference: {num_1-num_2}")
	print(f"Product: {num_1*num_2}")
	if num_2 == 0:
		print("Quotient: ERROR (division by zero)")
		print("Remainder: ERROR ((modulo by zero)")
	else:
		print(f"Quotient: {num_1/num_2}")
		print(f"Remainder: {num_1%num_2}")

def main():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("You need to type exactly 2 numbers.")
	else:
		try:
			num_1 = int(sys.argv[1])
		except ValueError:
			print("Only integers")
			return
		try:
			num_2 = int(sys.argv[2])
		except ValueError:
			print("Only integers")
			return
		operations(num_1, num_2)
		

if __name__ == '__main__':
	sys.exit(main())