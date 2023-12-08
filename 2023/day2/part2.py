

answer = 0

def map_to_cube_count(x):
	cubes = x.split(", ")

	pulls = {}
	for cube in cubes:
		count, color = cube.split()

		pulls[color] = int(count)
	
	return pulls

with open("input.txt", "r") as f:
	for i, line in enumerate(f.readlines()):
		game, pulls = line.strip().split(": ")
		pulls = pulls.split("; ")

		pulls = list(map(map_to_cube_count, pulls))

		
		colors = {
			'red': -1,
			'green': -1,
			'blue': -1,
		}

		for pull in pulls:
			for color, amount in pull.items():
				if amount > colors[color]:
					colors[color] = amount
		
		prod = colors['red'] * colors['green'] * colors['blue']
		
		answer += prod
		

print(answer)