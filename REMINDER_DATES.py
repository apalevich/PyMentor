#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is an exercise maintained with my mentor Zcho05.
The exercise contains function called create_message() that returns a message about some reminder.

For example:
>>> create_message((2, 4, 6, 7,))
'Мы оповестим вас о предстоящих событиях за 2, 4, 6 и 7 дней'

"""

def create_message(dates, separator=None):
	'''
	This function construct a message from a tuple with dates:

	>>> create_message((2, 4, 5, 7))
	'Мы оповестим вас о предстоящих событиях за 2, 4, 5 и 7 дней'

	You can even use a tuple with only date. Conjunction "и" ("and") will not be inputed then:

	>>> create_message((7,))
	'Мы оповестим вас о предстоящих событиях за 7 дней'

	Also strings and lists are supported:

	>>> create_message('5, 7, 2, 8, ')
	'Мы оповестим вас о предстоящих событиях за 5, 7, 2 и 8 дней'
	>>> create_message([5, 7, 2, 8])
	'Мы оповестим вас о предстоящих событиях за 5, 7, 2 и 8 дней'

	Commas are not required with strings:

	>>> create_message('5 7 2 8')
	'Мы оповестим вас о предстоящих событиях за 5, 7, 2 и 8 дней'

	Don’t worry about non-digit symbols:

	>>> create_message(‘  24, 46, 745, а, рыбки?, 300 xxx    ’)
	‘Мы оповестим вас о предстоящих событиях за 24, 46, 745 и 300 дней’

	You can use optional separator between numbers by adding it as argument:
	>>> create_message('5 7 2 8', '; ')
	'Мы оповестим вас о предстоящих событиях за 5; 7; 2 и 8 дней'

	But beware using create_message with empty input:

	>>> create_message(())
	Traceback (most recent call last):
  		File "reminder_dates.py", line 73, in <module>
    		print(create_message(r))
		File "reminder_dates.py", line 36, in create_message
    		raise Exception('Отсутствуют даты')
	Exception: Отсутствуют даты

	Don't input a letters neither:

	>>> create_message((3, 5, 6, 3, 'a', ))
	Traceback (most recent call last):
	  File "reminder_dates.py", line 101, in <module>
	    print(create_message(r))
	  File "reminder_dates.py", line 77, in create_message
	    raise Exception('Вместо даты использована буква')
	Exception: Вместо даты использована буква
	'''

	#check input argument
	if not dates:
		raise Exception('Отсутствуют даты')
	integers = []

	if isinstance(dates, str):
		temp = ''
		for i in dates:
		    if i.isdigit():
		        temp += i
		    else:
		        temp += ''
		integers = temp.split()
		integers = list(map(int, integers))
	elif isinstance(dates, (list, tuple)):
		for c in dates:
			try:
				integers.append(int(c))
			except ValueError:
				raise Exception('Вместо даты использована буква')

	message = ''
	# choose correct case for ending word
	if str(integers[-1]).endswith('1'):
		message = ' день'
	elif str(integers[-1]).endswith(('2', '3', '4')):
		message = ' дня'
	elif str(integers[-1]).endswith(('5', '6', '7', '8', '9', '0')):
		message = ' дней'

	# construct final message
	if len(integers) > 1:
		message = 'Мы оповестим вас о предстоящих событиях за {} и {}'.format(str(integers[0:-1])[1:-1], str(integers[-1])) + message
	else:
		message = 'Мы оповестим вас о предстоящих событиях за {}'.format(str(integers)[1:-1]) + message

	# replace comma with an selected separator
	if separator:
		message = message.replace(', ', separator)

	return message

if __name__ == '__main__':
	# r = (3, 5, 6, 3, 'a', )
	# print(create_message(r))
	#
	import doctest
	doctest.testmod()
