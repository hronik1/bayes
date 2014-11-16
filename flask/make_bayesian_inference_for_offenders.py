def learn_truth_table_for_offenders(filename = 'data/truth_table_for_offenders.json'):
	import codecs
	import json
	from discrete_probability import *

	features = json.loads(codecs.open(filename, 'r', encoding='utf8').read())

	# includes at least one female case
	features.append([1,0,1,1])

	featuresBool = []
	for feature in features:
		featuresBool.append(map(bool,map(int,feature)))

	R, S, N, C = variables = map(Variable, 'RSNC')

	data_header = [R, S, N, C]

	data_assignments = data_to_assignments(data_header, featuresBool)

	P = Table(variables)
	P.learn_from_complete_data(data_assignments)

	return P,R, S, N, C

def make_bayesian_inference_offenders(missing, query):
	P,R, S, N, C = learn_truth_table_for_offenders()

	r = R << query[0]
	s = S << query[1]
	n = N << query[2]
	c = C << query[3]

	if missing == 'n': #offense count
		return P(n|c, s, r)
	elif missing == 'c': #severity
		return P(c|n, s, r)
	elif missing == 'r': #1 if white, 0 if black
		return P(r|n, s, c)
	elif missing == 's': #1 if male, 0 if female
		return P(s|c, n, r)

print make_bayesian_inference_offenders('n', [False,True,True,True])



