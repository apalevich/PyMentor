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

	Use any big numbers you want to:

	>>> create_message('23 52, 63')
	'Мы оповестим вас о предстоящих событиях за 23, 52 и 63 дня'

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
		for c in range(-1, len(dates)+1):
			if dates[c].isdigit() and dates[c+1].isdigit():
				temp += dates[c]
			elif dates[c].isdigit() and not dates[c+1].isdigit():
				integers.append(temp)
			else:
				temp = ''
		print(integers)
		# integers = list(map(int, integers))
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

	import doctest
	doctest.testmod()
