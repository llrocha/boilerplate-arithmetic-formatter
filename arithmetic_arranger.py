class ArithmeticArranger():
	ERROR_DIGITS = "Error: Numbers must only contain digits."
	ERROR_LENGTH = "Error: Numbers cannot be more than four digits."
	ERROR_OPERATOR = "Error: Operator must be '+' or '-'."
	ERROR_TOO_MANY = "Error: Too many problems."

	def __init__(self, problems):
		self.problems = problems
		self.last_error_message = ''

	def validate_problems(self):
		valid = True
		if(len(self.problems) > 5):
			self.last_error_message = self.ERROR_TOO_MANY
			valid = False

		if(valid):
			for p in self.problems:
				valid = True
				terms = p.split()

				if(not terms[0].isdigit() or not terms[2].isdigit()):
					self.last_error_message = self.ERROR_DIGITS
					valid = False
					break
				if(len(terms[0]) > 4 or len(terms[2]) > 4):
					self.last_error_message = self.ERROR_LENGTH
					valid = False
					break
				if(terms[1] not in ['-', '+']):
					self.last_error_message = self.ERROR_OPERATOR
					valid = False
					break

		return valid

	@property
	def last_error(self):
		return self.last_error_message

	def format_line(self, operand, length, operator=''):
		if(operator):
			format = f'{operator}{{0:>{length-1}}}'
		else:
			format = f'{operator}{{0:>{length}}}'

		return format.format(operand)
	
	def format_problem(self, problem):
		terms = problem.split()
		length = len(terms[0]) + 2
		if(length < (len(terms[2]) + 2)):
			length = len(terms[2]) + 2
		
		lines = []
		lines.append(self.format_line(terms[0], length))
		lines.append(self.format_line(terms[2], length, terms[1]))
		lines.append('-' * length)
		lines.append(self.format_line(eval(problem), length))
	
		return lines

	def transpose(self, matrix):
		return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

	def format(self, resolve=False):
		formatted_problems = []
		for problem in self.problems:
			formatted_problems.append(self.format_problem(problem))
		formatted_problems = self.transpose(formatted_problems)
		result = []
		for i in formatted_problems:
			result.append('    '.join(i))

		if(not resolve):
			result = result[0:len(result)-1]

		return '\n'.join(result)


def arithmetic_arranger(problems, resolve=False):
	aa = ArithmeticArranger(problems)
	if(aa.validate_problems()):
		result = aa.format(resolve)
		return result
	else:
		return aa.last_error
