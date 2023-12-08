import re

answer = 0

m = {
	"one": '1',
	"two": '2',
	"three": '3', 
	"four": '4', 
	"five": '5', 
	"six": '6', 
	"seven": '7', 
	"eight": '8', 
	"nine": '9'
}

with open('input.txt', 'r') as file:
	for line in file.readlines():

		s = line.strip()
		digits = []

		while s:
			if s[0].isdigit():
				digits.append(s[0])
				s = s[1:]
				continue
			
			for code in m:
				if s.startswith(code):
					digits.append(m[code])
					s = s[1:]
					break
			else:
				s = s[1:]
			
		res = int(digits[0] + digits[-1])
		answer += res

print(answer)