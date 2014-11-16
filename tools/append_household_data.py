from read_household_data import read_household_data

def append_household_data(in_file="../data/incidents_upload_quid.csv", out_file="../data/incidents_upload_quid_new.csv"):
	household_data = read_household_data()
	with open(in_file, 'r') as orig:
		with open(out_file, 'w') as new:
			for line in orig:
				split_line = line.split(',')
				data = household_data.get(split_line[3], ',,,,,')
				new_line = line.rstrip('\n')
				for element in data.split(','):
					new_line += ',' + element.strip()
				new.write(new_line+'\n')
