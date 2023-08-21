import logging 
import calculadora as calc

logging.basicConfig(filename="test.log", level=logging.INFO) 

def get_sum(v1,v2):
  return calc.sum(v1,v2)

def get_subtract(v1,v2):
  return calc.subtract(v1,v2)

def get_division(v1,v2):
  return calc.divide(v1,v2)

def get_multiplication(v1,v2):
  logging.debug(f"v1: {v1}")
  logging.debug(f"v2: {v2}")
  return calc.multiply(v1,v2)

num_1 = 4
num_2 = 13
num_3 = 0

add_result = get_sum(num_1, num_2)
logging.info(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = get_subtract(num_1, num_2)
logging.info(f"Sub: {num_1} - {num_2} = {sub_result}")

mul_result = get_multiplication(num_1, num_2)
logging.info(f"Mul: {num_1} * {num_2} = {mul_result}")

div_result = get_division(num_1, num_2)
logging.info(f"Div: {num_1} / {num_2} = {div_result}")

div_result = get_division(num_1, num_3)
logging.debug(f"Div: {num_1} / {num_2} = {div_result}")
