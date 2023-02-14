# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/14 11:41:41 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/14 12:13:57 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_user_imput():
	print("""List of available options:
  1: Add a recipe
  2: Delete a recipe
  3: Print a recipe
  4: Print the cookbook
  5: Quit""")
	print('')  
	user_input = input("Please select an option:\n>> ")
	return user_input


def selector(user_input):
	if user_input == 1:
		add_recipe()
	elif user_input == 2:
		delete_recipe()
	elif user_input == 3:
		print_recipe()
	elif user_input == 4:
		print_cookbook()
	elif user_input == 5:
		print("Cookbook closed. Goodbye !")
		exit
	else:
		print("Sorry, this option does not exist.")
		new_input = get_user_imput()
		selector(new_input)
		
		

def main():
	print("Welcome to the Python Cookbook !")
	user_input = get_user_imput()
	print(f"this is the user input: {user_input}")
	selector(user_input)
			
  

if __name__ == '__main__':
	sys.exit(main())