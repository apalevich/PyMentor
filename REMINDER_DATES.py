REMINDER_DATES = (5, 3, 2, 1, 0,)

def message():
	return 'Мы оповестим вас о предстоящих событиях за {}, {}, {}, {} и {} дней'.format(REMINDER_DATES[0], REMINDER_DATES[1], REMINDER_DATES[2],REMINDER_DATES[3],REMINDER_DATES[4])


if __name__ == '__main__':
	print(message())
