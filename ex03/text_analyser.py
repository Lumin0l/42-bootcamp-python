# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    text_analyser.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/07 11:54:27 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/07 15:23:43 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(user_string):
	characters	= len(user_string)
	upper_case	= 0
	lower_case	= 0
	punctuation	= 0
	spaces		= 0
	
	for index in user_string:
		if index.isupper():
			upper_case += 1
		elif index.islower():
			lower_case += 1
		elif index is ' ':
			spaces += 1
		elif index in string.punctuation:
			punctuation += 1

	print(f"The text contains {characters} character(s):")
	print(f"- {upper_case} upper letter(s)")
	print(f"- {lower_case} lower letter(s)")
	print(f"- {punctuation} punctuation mark(s)")
	print(f"- {spaces} space(s)")
	
def text_filter(user_string):
	try:
		string = str(user_string)
	except ValueError:
		print("AssertionError: argument is not a string")
		return
	text_analyzer(string)	

def main():
	if len(sys.argv) > 2:
		print("Error: Too many arguments. Add a single string.")
		return
	elif len(sys.argv) < 2 or sys.argv[1] == "None" or sys.argv[1] == "none":
		user_string = input("What is the text to analyze?")
		text_filter(user_string)
	else:
		text_filter(sys.argv[1])
		
		
	


if __name__ == '__main__':
	sys.exit(main()) 
	