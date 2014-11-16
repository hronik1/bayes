def learn_truth_table_for_cases(filename = 'data/truth_table_for_cases.json'):
	import codecs
	import json
	from discrete_probability import *

	features = json.loads(codecs.open(filename, 'r', encoding='utf8').read())

	featuresBool = []
	for feature in features:
		featuresBool.append(map(bool,map(int,feature)))

	R, S, W, C, A = variables = map(Variable, 'RSWCA')

	data_header = [R, S, W, C, A]

	data_assignments = data_to_assignments(data_header, featuresBool)

	P = Table(variables)
	P.learn_from_complete_data(data_assignments)

	return P,R, S, W, C, A

def make_bayesian_inference_cases(missing, query):
	P,R, S, W, C, A = learn_truth_table_for_cases()

	r = R << query[0]
	s = S << query[1]
	w = W << query[2]
	c = C << query[3]
	a = A << query[4]

	if missing == 'w':
		return P(w|c, s, r, a)
	elif missing == 'c':
		return P(c|w, s, r, a)
	elif missing == 'r':
		return P(r|w, s, c, a)
	elif missing == 's':
		return P(s|c, w, r, a)
	elif missing == 'a':
		return P(a|c, w, r, s)

print make_bayesian_inference_cases('c', [False,True,True,True,False])

