# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rev_alpha.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 10:06:20 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/03 11:31:33 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def rev_and_swapcase(s):
	str = s[::-1]
	return str.swapcase()
	
	
def main():
	if sys.argv > 1:
		arg = ' '.join(sys.argv[1:])
		to_print = rev_and_swapcase(arg)
	print(to_print)

if __name__ == '__main__':
	main()
