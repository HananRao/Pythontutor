import sys
import random

try:
    reps = int(sys.argv[1])
except IndexError:
    print('Number of repetitions must be provided on the command line')
    sys.exit(1)
except ValueError:
    print('Repetitions must be a pure number')
    sys.exit(1)

# Check if (a*b)**3 == a**3 * b**3
successes = 0
for _ in range(reps):
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    if (a * b) ** 3 == a ** 3 * b ** 3:
        successes += 1

success_rate = successes / reps * 100

print('(a*b)**3 and a**3*b**3 \n'
      f'{successes} successes and {reps - successes} failures. \n'
      f'Success rate = {success_rate:.2f}%')

# Check if a/b == 1 / (a/b)
successes = 0
for _ in range(reps):
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    if a / b == 1 / (b / a):
        successes += 1

success_rate = successes / reps * 100

print('\na/b and 1/(a/b) \n'
      f'{successes} successes and {reps - successes} failures. \n'
      f'Success rate = {success_rate:.2f}%')

"""
Sample run:
python math_identities_failures.py 100000
(a*b)**3 and a**b*b**3
33796 successes and 66204 failures.
Success rate = 33.80%

a/b and 1/(a/b)
72936 successes and 27064 failures.
Success rate = 72.94%
"""
