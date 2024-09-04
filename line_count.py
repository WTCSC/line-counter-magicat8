def line_count():
	file = open("file.txt", "r")
	lines = file.readlines()
	print(f"{len(lines)}")
