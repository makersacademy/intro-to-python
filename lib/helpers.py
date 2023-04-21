# Just some friendly helper functions.
# Probably you want to be in the materials, not here.
# To start, go to 000_START_HERE.py

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

def these_are_the_same(a, b):
    if a == b:
        print(f"[TRUE]  {a} == {b}")
    else:
        print(f"[FALSE] {a} != {b}")

def show_us_the_output_of(a):
    print(f"{a}")

count_correct = 0
def check_that_these_are_equal(a, b):
    global count_correct
    print(f"EXPECTED: {b}")
    print(f"ACTUAL:   {a}")

    if a == b:
        count_correct = count_correct + 1
        print(f"{GREEN}That's correct! ({count_correct} checks right so far){NC}\n")
    else:
        print(f"{RED}That's not correct. Stopping execution here...{NC}")
        exit()
