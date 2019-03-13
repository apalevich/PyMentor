def CREATE_MESSAGE(dates, separator=None):

	# inject dates into example sentence
	message = 'Мы оповестим вас о предстоящих событиях за {} и {}'.format(str(dates[0:-1])[1:-1], str(dates[-1]))

	# replace comma with an selected separator
	if separator:
		message = message.replace(',', separator)

	# choose correct case for ending word
	if message.endswith('1'):
		message += ' день'
	elif message.endswith(('2', '3', '4')):
		message += ' дня'
	elif message.endswith(('5', '6', '7', '8', '9', '0')):
		message += ' дней'

	return message

if __name__ == '__main__':

	print("Examples:")

	REMINDER_DATES = (5, 3, 2, 1, 0,)
	print(CREATE_MESSAGE(REMINDER_DATES))

	REMINDER_DATES = (10, 5, 3, 4,)
	print(CREATE_MESSAGE(REMINDER_DATES, ';'))

	REMINDER_DATES = (10, 5, 3, 2, 1, 8)
	print(CREATE_MESSAGE(REMINDER_DATES, separator='/'))

	REMINDER_DATES = (10, 5, 3, 2, 1, 10)
	print(CREATE_MESSAGE(REMINDER_DATES, ' и'))
