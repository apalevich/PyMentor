"""
This is an exercise maintained with my mentor Zcho05.
The exercise contains function called create_message() that returns a message about some reminder.

For example:
>>> create_message((2, 4, 6, 7,))
'Мы оповестим вам о предстоящих событиях за 2, 4, 6 и 7 дней'

"""

def create_message(dates, separator=', '):
	#check input argument
<<<<<<< HEAD
	# # TODO convert string to list
	# if isinstance(dates, str):
	# 	try:
	# 		dates = list(map(int, dates.split(',')))
	# 	except ValueError:
	# 		raise Exception('Буквы вместо дат')
	if not len(dates):
		raise Exception('Отсутствуют даты')

	# choose correct case for ending word
	if str(dates).endswith('1', 0, -1):
		message = ' день'
	elif str(dates).endswith(('2', '3', '4'), 0, -1):
		message = ' дня'
	elif str(dates).endswith(('5', '6', '7', '8', '9', '0'), 0, -1):
		message = ' дней'

	# construct final message
	message = 'Мы оповестим вас о предстоящих событиях за {}'.format(str(dates)[1:-1]) + message

	# replace comma with an selected separator
	message = message.replace(', ', separator)
=======
	if isinstance(dates, str):
		try:
			dates = list(map(int, dates.split(',')))
		except ValueError:
			raise Exception('Буквы вместо дат')
	if not len(dates):
		raise Exception('Отсутствуют даты')

	# create final message

	message = ''



	# choose correct case for ending word
	if str(dates).endswith('1', 0, -1):
		message = ' день'
	elif str(dates).endswith(('2', '3', '4'), 0, -1):
		message = ' дня'
	elif str(dates).endswith(('5', '6', '7', '8', '9', '0'), 0, -1):
		message = ' дней'

	message = 'Мы оповестим вас о предстоящих событиях за {}'.format(str(dates)[1:-1]) + message

	# replace comma with an selected separator
	if separator:
		message = message.replace(', ', separator)
>>>>>>> 8eaa9b8d3df24b5b6e3ccd14c0d72c1f4c31d7fb

	return message

if __name__ == '__main__':
<<<<<<< HEAD
	r = '4, 6, 3, 3'
=======
	r = '4, 6, 3, 3,'
>>>>>>> 8eaa9b8d3df24b5b6e3ccd14c0d72c1f4c31d7fb
	print(create_message(r))
	#
	# import doctest
	# doctest.testmod()
