
MAX = {
	'red': 12,
	'green': 13,
	'blue': 14,
}

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

		flag = True
		for pull in pulls:
			for color, amount in pull.items():
				if MAX[color] < amount:
					flag = False
					continue
		
		if flag:
			answer += i + 1

print(answer)