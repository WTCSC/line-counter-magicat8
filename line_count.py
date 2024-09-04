def line_count():
	file = open("file.txt", "r")
	lines = file.readlines()
	output = len(lines)
	return output
