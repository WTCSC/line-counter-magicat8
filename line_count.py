def line_count():
	# Opens file in read mode
	file = open("file.txt", "r")
	# Reads each line in the file
	lines = file.readlines()
	# Gets number of line
	output = len(lines)
	# Returns output
	return output
