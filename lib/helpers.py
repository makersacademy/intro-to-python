# Just some friendly helper functions.
# Probably you want to be in the materials, not here.
# To start, go to 000_START_HERE.py

def these_are_the_same(a, b):
    if a == b:
        print(f"[TRUE]  {a} == {b}")
    else:
        print(f"[FALSE] {a} != {b}")

def show_us_the_output_of(a):
    print(f"{a}")

def check_that_these_are_equal(a, b):
    print(f"EXPECTED: {b}")
    print(f"ACTUAL:   {a}")

    if a == b:
        print("That's correct!")
    else:
        print("That's not correct. Stopping execution here...")
        exit()
