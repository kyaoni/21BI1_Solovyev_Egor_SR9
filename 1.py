try:
	n=int(input('Введите целое десятичное число '))
except ValueError:
	print('Ошибка ввода')
else:
	def function():
		x=abs(n)
		c=0
		while x>0:
			x//=10
			c+=1
		last=abs(n)%10
		if last%2!=0:
			print('Ошибка, последняя цифра нечётная')
		else:
			p=10**(c-1)
			first=abs(n)//p
			if first%2!=0:
				print('Ошибка, первая цифра нечётная')
			else:
				m=abs(n)-(first*p)-last
				f=(last*p)+first+m
				if n>0:
					print(f)
				else:
					print(-f)
	function()