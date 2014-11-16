def dedupe_addresses(in_addresses='../data/addresses.txt', out_addresses='../data/out_addresses.txt'):
	deduped = set()
	with open(in_addresses, 'r') as addresses:
		for address in addresses:
			deduped.add(address)

	with open(out_addresses, 'w') as out:
		for address in deduped:
			out.write(address)