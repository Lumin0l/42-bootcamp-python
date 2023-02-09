# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imanol <imanol@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 15:55:21 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/09 19:53:37 by imanol           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main ():
    #No se ni lo que me pide, en principio no lo puedo hacer tuple.
    print(f"Python was created by {kata['Python']}")
    print(f"Ruby was created by {kata['Ruby']}")
    print(f"PHP was created by {kata['PHP']}")

if __name__ == '__main__':
    sys.exit(main())

