# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ide-la-i <ide-la-i@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/14 11:41:41 by ide-la-i          #+#    #+#              #
#    Updated: 2023/02/16 09:16:26 by ide-la-i         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {'sandwich': {'ingredients': 'ham, bread, cheese and tomatoes', 'type': 'lunch', 'time': '10'},
		'cake': {'ingredients': 'flour, sugar and eggs', 'type': 'dessert', 'time': '60'},
		'salad': {'ingredients': 'avocado, arugula, tomatoes and spinach', 'type': 'lunch', 'time': '15'}}

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

def print_recipe():
	recipe_choice = input("Please enter a recipe name to get its details:\n")
	for key in cookbook:
		if key == recipe_choice:
			print(key)
			return 1
	print("No recipe found for that item. Check spelling and try again, or add it yourself if missing.")
	
	
def print_cookbook():
	print(cookbook)
	exit

def selector(user_input):
	if user_input == '1':
		add_recipe()
	elif user_input == '2':
		delete_recipe()
	elif user_input == '3':
		print_recipe()
	elif user_input == '4':
		print_cookbook()
	elif user_input == '5':
		print("Cookbook closed. Goodbye !")
		exit
	else:
		print("Sorry, this option does not exist.")
		new_input = get_user_imput()
		selector(new_input)
		
		

def main():
	print("Welcome to the Python Cookbook !")
	user_input = get_user_imput()
	selector(user_input)
			
  

if __name__ == '__main__':
	sys.exit(main())