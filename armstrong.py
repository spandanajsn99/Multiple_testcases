def armstrong(i):
	t = i
	s = 0
	while t > 0:
		d = t % 10
		s = s + d*d*d
		t = t // 10
	if s == i:
		print('YES')
	else:
		print('NO')

number = int(input())

armstrong(number)
