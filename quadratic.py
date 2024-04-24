import math 
def roots(a, b, c):
	x=math.pow(b, 2)-(4*a*c)
	if x<0:
		return "( )"
	raiz=(math.sqrt(x))
	r1=(-b+raiz)/(2*a)
	r2=(-b-raiz)/(2*a)
	if r1==r2:
		return f"({r1})"
	else:
		return f"({r1}, {r2})"


def value_y(a, b, c, x):
	y= a*(math.pow(x, 2))+b*x+c
	return y


def to_string(a, b, c):
	if a and b and c:
		return f"f(x) = {a} * X^2 + {b} * X + {c}"
	elif b and c:
		return f"f(x) = {b} * X + {c}"
	elif a and c:
		return f"f(x) = {a} * X^2 + {c}"
	elif not a and not b and c:
		return f"f(x) = {c}"


def derivation(a, b, c):
	if a and b:
		return f"f'(x) = {2*a} * X + {b}"
	elif not a:
		return f"f'(x) = {b}"
	elif not b:
		return f"f'(x) = {2 * a} * X"
     
	
	elif not a:
		return f"f'(x) = {b}"
	elif not b:
		return f"f'(x) = {2*a} * X"
