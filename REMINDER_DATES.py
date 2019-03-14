def create_message(dates, separator=None):

	# create pieces of final message
	message1 = 'Мы оповестим вас о предстоящих событиях за '
	message2 = ''
	message3 = ''

	#fill message2 with days in readable format
	if len(dates) == 0:
		raise Exception('Отсутствуют даты')
	elif len(dates) == 1:
		message2 = str(dates)[1:-1]
	else:
		message2 = str(dates[:-1])[1:-1] + ' и ' + str(dates[-1])

	# replace comma with an selected separator
	if separator:
		message2 = message2.replace(',', separator)

	# choose correct case for ending word
	if message2.endswith('1'):
		message3 = ' день'
	elif message2.endswith(('2', '3', '4')):
		message3 = ' дня'
	elif message2.endswith(('5', '6', '7', '8', '9', '0')):
		message3 = ' дней'

	return message1 + message2 + message3

if __name__ == '__main__':

	print("Examples:")

	REMINDER_DATES = '5, 3, 2, 1'
	print(create_message(REMINDER_DATES))

	REMINDER_DATES = (5, 3, 2, 1, 0,)
	print(create_message(REMINDER_DATES, '/'))

	REMINDER_DATES = (10, 5, 3, 4,)
	print(create_message(REMINDER_DATES, separator=';'))

	REMINDER_DATES = (10, 5, 3, 2, 1, 8)
	print(create_message(REMINDER_DATES))

	REMINDER_DATES = (10, 5, 3, 2, 1, 10)
	print(create_message(REMINDER_DATES))
