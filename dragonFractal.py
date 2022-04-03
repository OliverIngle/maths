from turtle import *

# Generate sequence of the fractal
def generate_sequence(initial_sequence, depth):

    if depth <= 1:
        return initial_sequence

    new_sequence = []
    new_sequence.extend(initial_sequence)
    new_sequence.append( not initial_sequence[-1] )


    for step in reversed(initial_sequence):
        new_sequence.append(not step)

    return generate_sequence(new_sequence, depth - 1)

# Plot the fractal
def plotSequence(sequence):
    lineLength = 1
    forward(lineLength)
    for step in sequence:
        if step:
            left(90)
        elif not step:
            right(90)
        forward(lineLength)
    done()

# Find size of the fractal for large depths (approximation at n -> ininity)
def calculate_size(initial_length, depth):
    return 2 ** depth


def main():

    print("\n\n\t\t--- Dragon Fractal ---\n\n")
    depth = int(input("> Enter desired depth: "))
    sequence = generate_sequence([False, False, True], depth)

    color('red')
    bgcolor('black')
    speed(100)
    left(180)
    plotSequence(sequence)

if __name__ == "__main__":
    main()