def CREATE_MESSAGE(dates):
	message = 'Мы оповестим вас о предстоящих событиях за {} и {} дней'.format(str(dates[0:-1])[1:-1], str(dates[-1]))
	return message

if __name__ == '__main__':
	print("Examples:")

	REMINDER_DATES = (5, 3, 2, 1, 0,)
	print(CREATE_MESSAGE(REMINDER_DATES))

	REMINDER_DATES = (10, 5, 3, 2, 1, 0,)
	print(CREATE_MESSAGE(REMINDER_DATES))
