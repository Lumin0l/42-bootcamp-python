# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    old_even_zero.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 11:37:45 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/03 13:30:34 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def whatis(num):
	if num == 0:
		return ("I'm Zero.")
	elif (num % 2) == 0:
		return ("I'm Even.")
	else:
		return ("I'm Odd.")


def main():
	if len(sys.argv) == 2:
		try:
			num = int(sys.argv[1])
		except ValueError:
			print("AssertionError: argument is not an integer")
			return
		print(whatis(num))
		return
	elif len(sys.argv) > 2:
		print("AssertionError: more than one argument provided")
		return
	
		
if __name__ == '__main__':
	main()