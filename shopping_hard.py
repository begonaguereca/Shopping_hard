list_names = {}

def show_all_lists():
	print list_names

def show_specific_list(key):
	key = key.lower()
	if key not in list_names: 
		print "Error, that shopping list does not exist"
	else: 
		print sorting_shopping_list(key)


def add_new_list(key):
 	shopping_list = []
 	key = key.lower()

 	if key in list_names:
 		print "Error, this shopping list already exists"
 	else: 
 		list_names[key] = shopping_list

def add_item_list(key, item):
 	key = key.lower()
 	item = item.lower()
 	if key in list_names:
 		shopping_list = list_names[key]
 		if item in shopping_list:
 			print "Error, you are already buying this item"
 		else:
 			shopping_list.append(item)
 			print sorting_shopping_list(key)
 	else: 
 		print "Error, this list does not exist"

def remove_item_list(key, item):
	key = key.lower()
 	item = item.lower()
	if key in list_names:
		shopping_list = list_names[key]
		if item in shopping_list:
			shopping_list.remove(item)
			print sorting_shopping_list(key)
		else:
			print "Error, this item is not in the list"
	else: 
		print "Error, the list does not exist"

def remove_list(key):
	key = key.lower()
	if key in list_names: 
		del list_names[key]
	else: 
		print "Error, this list does not exist"


def sorting_shopping_list(key):
 	key = key.lower()
 	if key in list_names:
 		shopping_list = list_names[key]
 		shopping_list = shopping_list.sort()
 		return shopping_list 
 	else: 
 		print "Error, this list does not exist"

def show_main_menu():
	print "0- Main Menu"
	print "1- Show all lists"
	print "2- Show a specific list"
	print "3- Add a new shopping list"
	print "4- Add an item to a shopping list"
	print "5- Remove an item from a shopping list"
	print "6- Remove a list by nickname"
	print "7- Exit when you are done"
	answer = int(raw_input("Choose from options in main menu "))
	return answer 

# def return_main(): 
# 	answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
# 	if answer2 == 1:
# 		show_main_menu()
# 	else: 
# 		break

def main():
	while True: 
		answer = show_main_menu()

		if answer == 0: 
			show_main_menu()

		elif answer == 1:
			show_all_lists()
			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 
		elif answer ==2: 
			print show_all_lists()
			key = raw_input("What list would you like to see?")
			show_specific_list(key)

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 

		elif answer ==3:
			print show_all_lists()
			key = raw_input("What would you like to call your new shopping list?")
			add_new_list(key)
			print show_all_lists()

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 
				
		elif answer == 4: 
			print show_all_lists()
			key = raw_input("Which list would you like to add an item to?")
			item = raw_input("Which item would you like to add to the shopping list?")
			add_item_list(key, item)

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 
		elif answer == 5: 
			print show_all_lists
			key = raw_input("Which list would you like to remove and item from?")
			item = raw_input("Which item would you like to remove from the shopping list?")
			remove_item_list(key, item)

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 
		elif answer == 6:
			print show_all_lists
			key = raw_input("Which shopping list would you like to remove?")
			remove_list(key)

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 
		elif answer == 7: 
			print "Have a great day! o_0"
			break 
		else: 
			print "Error, please choose a valid menu option"

			answer2 = int(raw_input("what would you like to do? 1- Return to the main menu; 2- Exit your shopping list"))
			if answer2 == 1:
				show_main_menu()
			else: 
				break 


if __name__ == "__main__":
	main()






