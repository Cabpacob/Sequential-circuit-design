from pyeda.inter import exprvar


def is_access_allowed(input_bits):
	variables = list(map(exprvar, "abcd"))

	a, b, c, d = variables

	f = ~b & (a | c | d) 

	values = dict(zip(variables, input_bits))

	return bool(f.restrict(values))


print(is_access_allowed(input()))
