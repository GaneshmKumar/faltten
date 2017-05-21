# Module to flatten a list
def flatten(array, flattened=[]):
	for value in array:
		if(isinstance(value, list)):
			flatten(value, flattened)
		else:
			flattened.append(value)
	return flattened
