


def get_summ(num_one, num_two):
	try:
		return int(num_one) + int(num_two)
	except ValueError:
		print("Упс, не верно переданное значение")

chislo1 = input('Введите число 1: ')
chislo2 = input('Введите число 2: ')

get_summ(chislo1, chislo2)
