def read_household_data():
	out = dict()
	with open('../data/fetched_housing_data.csv', 'r') as data:
		for line in data:
			left, middle, right = line.partition(',')
			out[left] = right.strip('\n')
	return out