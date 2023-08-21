import itertools
def solve_cryptarithm(puzzle):
    words = puzzle.replace('+', ' ').replace('=', ' ').split()
    result_word = words[-1]
    words = words[:-1]
    letters = set(''.join(words + [result_word]))
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        digit_map = dict(zip(letters, perm))
        numbers = [int(''.join(str(digit_map[c]) for c in word)) for word in words]
        result = int(''.join(str(digit_map[c]) for c in result_word))
        if sum(numbers) == result:
            return digit_map
    return None
puzzle = 'SEND + MORE = MONEY'
solution = solve_cryptarithm(puzzle)
if solution:
    for letter, digit in solution.items():
        print(f'{letter}: {digit}')
else:
    print('No solution found.')
