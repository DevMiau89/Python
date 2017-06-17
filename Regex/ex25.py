#36. Write a python program to convert camel case string to snake case string.
import re

def camelCaseToSnake(s):
    #pattern = re.sub('(.)([A-Z][a-z]+)', r'\1\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()



if __name__ == "__main__":
    print camelCaseToSnake('snakesOnPlane andCrat ohoOoo')

def test_1():
    assert camelCaseToSnake('PythonExercises') == 'python_exercises'
    
   