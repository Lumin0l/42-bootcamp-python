# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/07 15:37:38 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/07 16:00:37 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def operations(num_1, num_2):
	

def main():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("You only need to type 2 numbers.")
	else:
		try:
			num_1 = int(sys.argv[1])
		except ValueError:
			print("First number is not an integer")
			return
		try:
			num_1 = int(sys.argv[2])
		except ValueError:
			print("Second number is not an integer")
			return
		operations(sys.argv[1], sys.argv[2])
		

if __name__ == '__main__':
	sys.exit.(main())