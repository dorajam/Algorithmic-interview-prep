# backtrack algorithms
obstacles = [(0,1), (2,2)]
r = 2
c = 2


def find_path(r,c):
	if r==0 and c==0:
		return [(r,c)]
	for d in possible_dirs(r,c):
		solution = find_path(d[0], d[1])
		if solution:
			return solution + [(r,c)]
	return None


def possible_dirs(r,c):
	directions = []
	if r>0 and (r-1,c) not in obstacles:
		directions.append((r-1,c))
	if c>0 and (r,c-1) not in obstacles:
		directions.append((r,c-1))
	return directions

print find_path(r,c)