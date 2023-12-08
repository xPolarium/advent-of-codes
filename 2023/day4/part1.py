
answer = 0

with open("input.txt", "r") as file:
	for line in file.readlines():	
		card, winning_numbers = line.split("|")
		
		card_numbers = card.split(":")[1].strip().split()
		winning_numbers = winning_numbers.strip().split()

		matches = 0
		for n in winning_numbers:
			if n in card_numbers:
				matches += 1
		
		if matches:
			answer += 2 ** (matches-1)

print(answer)