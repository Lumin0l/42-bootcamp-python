# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 15:50:16 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/09 15:54:55 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Put this at the top of your kata00.py file
kata = (19,42,21)

def print_kata(kata):
	print(f"The 3 numbers are: {kata[0]}, {kata[1]}, {kata[2]}")

def main():
	print_kata(kata)

if __name__ == '__main__':
	sys.exit(main())