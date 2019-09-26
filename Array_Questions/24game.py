# given an array of 4 integers each between 1-9,
# in a fixed order. try to add, subtract, multiply or divide these numbers in a way to add up to 24. 
# You can use parenteses to section off the number. 
import itertools

def solve(numbers,goal=24, expr = []):
    if expr == []:
        expr = [str(n) for n in numbers]
    if len(numbers) == 1:
        if numbers[0] == goal:
            return number[0]
        else:
            return False
    if len(numbers) == 2:
        answers,answer_exps = combinetwo(numbers[0],number[1])
        for i, answer in enumerate(answers):
            if answer == goal:
                return convert_expr_to_string(expr[0],expr[1],answer_exps[i])
        return False
    pairs = set(itertools.combinations(numbers,2))
    for pair in pairs:
        possible_values, possible_expr = combinetwo(*pair)
        for counter, value in enumerate(possible_values):
            expression = possible_expr[counter]
            a_index = numbers.index(pair[0])
            b_index = numbers.index(pair[1])
            if a_index == b_index:
                b_index = numbers.index(pair[1],a_index+1)
            