from collections import deque

def menu(ax, bx, px, errors):
	print "Galois Field Calculator"
	print "\nInput: "
	string = raw_input("A(x): ").split()
	for value in string:
		try: 
			int(value)
		except ValueError:
			errors.append("Coefficents of A(x) must be an integer.")
			break
		else: 
			ax.append(int(value))
	string = raw_input("B(x): ").split()
	for value in string: 
		try: 
			int(value)
		except ValueError:
			errors.append("Coefficents of B(x) must be an integer.")
			break
		else: 
			bx.append(int(value))	
	string = raw_input("P(x): ").split()
	for value in string: 
		try: 
			int(value)
		except ValueError:
			errors.append("Coefficents of P(x) must be an integer.")
			break
		else: 
			px.append(int(value))
	try:
		chosen = input("\nPick among the following operations:\n1. A(x) + B(x)\n2. A(x) - B(x)\n3. A(x) x B(x)\n4. A(x) / B(x)\nOperation: ")
	except:
		errors.append("Operation must only be either 1, 2, 3, or 4.")
	else:
		if chosen < 1 or chosen > 4:
			errors.append("Operation must only be either 1, 2, 3, or 4.")
		return chosen

def printing(array, print_type):
	marker = 0
	if print_type == 2:
		for power in range(len(array)):
				if array[power][0] == 1:
					if marker == 0:
						if array[power][1] == 0:
							print str(array[power][0]),
						elif array[power][1] == 1:
							print "x",
						else:
							print "x^" + str(array[power][1]),
						marker = 1
					else:
						if array[power][1] == 0:
							print "+ " + str(array[power][0]),
						elif array[power][1] == 1:
							print "+ " + "x",
						else:
							print "+ " + "x^" + str(array[power][1]),

				elif array[power][0] != 0:
					if marker == 0:
						if array[power][1] == 0:
							print str(array[power][0]),
						elif array[power][1] == 1:
							print str(array[power][0]) + "x",
						else:
							print str(array[power][0]) + "x^" + str(array[power][1]),
						marker = 1
					else:
						if array[power][1] == 0:
							print "+ " + str(array[power][0]),
						elif array[power][1] == 1:
							print "+ " + str(array[power][0]) + "x",
						else:
							print "+ " + str(array[power][0]) + "x^" + str(array[power][1]),

	else:	
		for power in range(len(array)):
			if print_type == 0:
				if array[power] == 1:
					if marker == 0:
						if (len(array)-power-1) == 0:
							print str(array[power]),
						elif (len(array)-power-1) == 1:
							print "x",
						else:
							print "x^" + str(len(array)-power-1),
						marker = 1
					else:
						if (len(array)-power-1) == 0:
							print "+ " + str(array[power]),
						elif (len(array)-power-1) == 1:
							print "+ " + "x",
						else:
							print "+ " + "x^" + str(len(array)-power-1),	

				elif array[power] != 0:
					if marker == 0:
						if (len(array)-power-1) == 0:
							print str(array[power]),
						elif (len(array)-power-1) == 1:
							print str(array[power]) + "x",
						else:
							print str(array[power]) + "x^" + str(len(array)-power-1),
						marker = 1
					else:
						if (len(array)-power-1) == 0:
							print "+ " + str(array[power]),
						elif (len(array)-power-1) == 1:
							print "+ " + str(array[power]) + "x",
						else:
							print "+ " + str(array[power]) + "x^" + str(len(array)-power-1),
						
			elif print_type == 1:	
				if marker == 0:
					if (len(array)-power-1) == 0:
						print str(array[power]),
					elif (len(array)-power-1) == 1:
						print str(array[power]) + "x",
					else:
						print str(array[power]) + "x^" + str(len(array)-power-1),
					marker = 1
				else:
					if (len(array)-power-1) == 0:
						print "+ " + str(array[power]),
					elif (len(array)-power-1) == 1:
						print "+ " + str(array[power]) + "x",
					else:
						print "+ " + str(array[power]) + "x^" + str(len(array)-power-1),
					
def mod2(array):
	for index in range(len(array)):
		array[index] = array[index]%2


def addition(ax, bx, add_type, result, for_div):
	size = 0
	if len(ax) == len(bx): 
		size = len(ax)
	elif len(ax) > len(bx):
		size = len(ax)
		for count in range(len(ax)-len(bx)): 
			bx.insert(0,0)
	elif len(ax) < len(bx):
		size = len(bx)
		for count in range(len(bx)-len(ax)):
			ax.insert(0,0)

	if for_div == 0:
		if add_type == 1: print "A(x) + B(x) = (",
		if add_type == 2: print "A(x) - B(x) = (",
		printing(ax, 0)
		if add_type == 1: print ") + (",
		if add_type == 2: print ") - (",
		printing(bx, 0)
		print ")"
		print "\nComputation:"
		print "A(x) = ",
		printing(ax, 1)
		if add_type == 1: print "\n+"
		if add_type == 2: print "\n-"
		print "B(x) = ",
		printing(bx, 1)
		print "\nis equal to"

	if len(ax) >= len(bx):
		for index in range(len(ax)):
			result.append((ax[index] + bx[index]))
	else:
		for index in range(len(bx)):
			result.append((ax[index] + bx[index]))

	if for_div == 0:
		if add_type == 1: print "A(x) + B(x) = (",
		if add_type == 2: print "A(x) - B(x) = (",
		printing(result, 0)
		print ") mod 2"

	mod2(result)

	if for_div == 0:
		if add_type == 1: print "A(x) + B(x) = ",
		if add_type == 2: print "A(x) - B(x) = ",
		printing(result, 0)	

	return result

def multiply(ax, bx, px, result, for_div):
	if for_div == 0:
		print "A(x) x B(x) = ((",
		printing(ax, 0)
		print ") x (",
		printing(bx, 0)
		print ")) mod P(x)"
		print "\nComputation:"
		print "A(x) = ",
		printing(ax, 1)
		print "\nx"
		print "B(x) = ",
		printing(bx, 1)
		print "\nis equal to"
		print "A(x) x B(x) = ((",
		printing(ax, 1)
		print ") x (",
		printing(bx, 1)
		print ")) mod P(x)"

	for index1 in range(len(ax)):
		for index2 in range(len(bx)):
			if not((ax[index1] == 0) or (bx[index2] == 0)):
				result.append((ax[index1] * bx[index2], (len(ax)-index1-1) + (len(bx)-index2-1)))

	result = sorted(result, key=lambda x: x[1], reverse = True)

	if len(result) > 1:
		size = len(result) - 1
		temp = result[0]
		result.remove(temp)

		while (size >= 0):
			if result[0][1] == temp[1]:
				temp = (result[0][0] + temp[0], temp[1])
			else:
				result.append(temp)
				temp = result[0]
			if size != 0: result.remove(result[0])
			size = size - 1

		size = len(result) - 1

		while (size >= 0):
			if (result[size][0] % 2) == 0:
				result.remove(result[size])
			size = size - 1
		
	if for_div == 0:		
		print "A(x) x B(x) = (",
		printing(result, 2)
		print ") mod P(x)"

	comparison = len(px)-1
	mod_px_marker = 0
	px_temp = deque(px)
	px_temp[0] = 0

	while (mod_px_marker == 0):
		mod_px_marker = 1
		size = len(result) - 1
		while (size >= 0):
			movement = result[size][1] - comparison
			if movement >= 0:
				mod_px_marker = 0
				px_temp.rotate(-movement)
				for index2 in range(len(px_temp)):
					if px_temp[index2] != 0:
						result.append((result[size][0],len(px_temp)-index2-1))
				px_temp.rotate(movement)
				result.remove(result[size])
			size = size - 1

	result = sorted(result, key=lambda x: x[1], reverse = True)
	size = len(result) - 1
	temp = result[0]
	result.remove(temp)

	while (size >= 0):
		if len(result) == 0:
			result.append(temp)
			break
		if result[0][1] == temp[1]:
			temp = (result[0][0] + temp[0], temp[1])
		else:
			result.append(temp)
			temp = result[0]
		if size != 0: result.remove(result[0])
		size = size - 1

	result_temp = [0] * ((len(ax)-1) + (len(bx)-1) + 1)

	for index in result:
		result_temp[index[1]] = index[0] 

	result = result_temp

	result.reverse()

	if for_div == 0:
		print "A(x) x B(x) = (",
		printing(result, 0)
		print ") mod 2"
	mod2(result)

	if for_div == 0:
		print "A(x) x B(x) = ",
		printing(result, 0)

	return result

def divide(ax, bx, px, result):
	R = deque(bx)
	S = deque(px)

	if len(R) > len(S):
		for count in range(len(R)-len(S)): 
			S.appendleft(0)
	elif len(R) < len(S):
		for count in range(len(S)-len(R)):
			R.appendleft(0)

	U = deque([1])
	V = deque([0])
	delta = 0
	print "\nR(x) | S(x) | U(x) | V(x) | delta"
	printing(R, 0)
	print " | ",
	printing(S, 0)
	print " | ",
	printing(U, 0)
	print " | 0 | - "

	while (True):
		size_S = 0
		size_R = 0

		for index1 in range(len(S)):
			if S[index1] != 0:
				size_S = len(S)-index1-1
				break
		for index2 in range(len(R)):
			if R[index2] != 0:
				size_R = len(R)-index2-1
				break
		
		if size_R == 0: break

		delta = size_S - size_R

		if delta < 0:
			temp1 = S
			S = R
			R = temp1

			temp2 = V
			V = U
			U = temp2

			delta = -delta

		R.rotate(-delta)
		result = []
		S = deque(addition(list(S), list(R), 1, result, 1))
		R = deque(R)
		R.rotate(delta)

		U_x = deque([0] * (delta+1))
		U_x[0] = 1
		result = []
		U_x = multiply(list(U_x), list(U), px, result, 1)

		result = []
		V = deque(addition(list(V), list(U_x), 1, result, 1))
		
		printing(R,0)
		print " | ",
		printing(S,0)
		print " | ",
		printing(U,0)
		print " | ",
		printing(V,0)
		print " | ",
		print str(delta),
		print ""

	print ""
	result = []
	result = multiply(ax, list(U), px, result, 0)
	
ax = []
bx = []
px = []
result = []
operation = 0
errors = []

operation = menu(ax, bx, px, errors)

for error in errors: print error
if errors == []:
	print "\nOutput:"
	print "A(x) = ",
	printing(ax, 0)
	print "\nB(x) = ",
	printing(bx, 0)
	print ""
	if operation == 1 or operation == 2:
		result = addition(ax, bx, operation, result, 0)

	elif operation == 3:
		result = multiply(ax, bx, px, result, 0)

	elif operation == 4:
		divide(ax, bx, px, result)









