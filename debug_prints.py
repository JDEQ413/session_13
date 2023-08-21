import calculadora as calc

def get_sum(v1,v2):
  return calc.sum(v1,v2)

def get_subtract(v1,v2):
  return calc.subtract(v1,v2)

def get_division(v1,v2):
  return calc.divide(v1,v2)

def get_multiplication(v1,v2):
  return calc.multiply(v1,v2)

num_1 = 20
num_2 = 10

add_result = get_sum(num_1, num_2)
print(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = get_subtract(num_1, num_2)
print(f"Sub: {num_1} - {num_2} = {sub_result}")

mul_result = get_multiplication(num_1, num_2)
print(f"Mul: {num_1} * {num_2} = {mul_result}")

div_result = get_division(num_1, num_2)
print(f"Div: {num_1} / {num_2} = {div_result}")
