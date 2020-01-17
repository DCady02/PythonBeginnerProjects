import csv
import re

x = 0

def add():

	first = input('First name: ')
	last = input('Last name: ')
	email = input('Email: ')
	input_phone = input('Phone: ')

	split_phone = list(input_phone)
	phone_list = []
	for x in split_phone:
		if x in '1234567890':
			phone_list.append(x)
	phone = ''.join(phone_list)

	key = first[0] + last[0]
	contact = [key.upper(), first + ' ' + last, email, phone]
	print(contact)

	with open('contacts.csv', 'a', newline='') as contact_file:
		writer = csv.writer(contact_file)
		writer.writerow(contact)


def search(parameter):
	with open('contacts.csv', 'r+') as contact_file:
		
		for row in contact_file:

			parameter_present = False #This variable exists because of printing the row multiple times if 
									  #the parameter existed in multiple items within the row
			for item in row.split(','):
				if parameter.upper() in item.upper():
					parameter_present = True

			if parameter_present is True:
				print(row)

def get_input(user_in):

	if user_in == 'ADD':
		add()

		command = input('>>> ').upper()
		get_input(command)

	elif user_in == 'SEARCH':
		search(input('Search Parameter: '))

		command = input('>>> ').upper()
		get_input(command)

	elif user_in == 'ALL':
		list_all()

		command = input ('>>> ').upper()
		get_input(command)
 
	elif user_in == "EXIT":
		exit()
		
	else:
		print(user_in + ' is not a valid command')

		command = input('>>> ').upper()
		get_input(command)

get_input(input('>>> ').upper())