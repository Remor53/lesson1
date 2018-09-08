def get_summ(first, second, delimetr = '&'):
	return str(first).upper() + str(delimetr) + str(second).upper()
print(get_summ('Learn', 'Python', ' '))