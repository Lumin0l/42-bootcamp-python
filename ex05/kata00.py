# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imanol <imanol@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 15:50:16 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/09 19:52:11 by imanol           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Put this at the top of your kata00.py file
kata = (19,42,21)

def main():
	kata_tuple = tuple(kata)
	print(f"The 3 numbers are: {kata_tuple[0]}, {kata_tuple[1]}, {kata_tuple[2]}")

if __name__ == '__main__':
	sys.exit(main())