"""
This is an exercise maintained with my mentor Zcho05.
The exercise contains function called create_message() that returns a message about some reminder.

For example:
>>> create_message((2, 4, 6, 7,))
'Мы оповестим вам о предстоящих событиях за 2, 4, 6 и 7 дней'

"""

def create_message(dates, separator=', '):
	'''
	This function construct message from dates:

	>>>create_message((2, 4, 5, 7))
	'Мы оповестим вас о предстоящих событиях за 2, 4, 5 и 7 дней'

	You can even use a tuple with only date. Conjunction "и" ("and") will not be inputed then

	>>>create_message((7,))
	'Мы оповестим вас о предстоящих событиях за 7 дней'

	Also strings and lists is supported:
	>>>create_message((7,))
	'Мы оповестим вас о предстоящих событиях за 7 дней'
	'''


	#check input argument
	if isinstance(dates, str):
		try:
			dates = list(map(int, dates.split()))
		except ValueError:
			raise Exception('Буквы вместо дат, либо неверная запятая')
	if not len(dates):
		raise Exception('Отсутствуют даты')
	for n in dates:
		if not type(n) == int:
			raise Exception('Вместо даты использована буква')

	message = ''
	# choose correct case for ending word
	if str(dates).endswith('1', 0, -1):
		message = ' день'
	elif str(dates).endswith(('2', '3', '4'), 0, -1):
		message = ' дня'
	elif str(dates).endswith(('5', '6', '7', '8', '9', '0'), 0, -1):
		message = ' дней'

	# construct final message
	if len(dates) > 1:
		message = 'Мы оповестим вас о предстоящих событиях за {} и {}'.format(str(dates[:-1])[1:-1], str(dates[-1])) + message
	else:
		message = 'Мы оповестим вас о предстоящих событиях за {}'.format(str(dates)[1:-1]) + message

	# replace comma with an selected separator
	message = message.replace(', ', separator)

	return message

if __name__ == '__main__':
	r = '7, 8, 5, 7, '
	print(create_message(r))
	#
	# import doctest
	# doctest.testmod()
