import itertools

def load_words(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file if len(word.strip()) >= 3)

def valid_word(word, current_side, sides):
    # Check if the word can be formed by moving correctly around the square
    for i in range(1, len(word)):
        if current_side[i] != current_side[i-1]:  # If side changes, it must adhere to adjacency rules
            if not (current_side[i-1], current_side[i]) in sides:
                return False
    return True

def find_solutions(sides, words):
    solutions = []
    side_letters = ''.join(sides.values())
    # Generate all permutations of the side letters
    for perm in itertools.permutations(side_letters):
        current_word = ''
        current_side_sequence = ''
        current_solution = []
        valid = True
        for letter in perm:
            if current_word and sides[letter] != current_side_sequence[-1]:
                if (current_side_sequence[-1], sides[letter]) not in [('top', 'right'), ('right', 'bottom'), ('bottom', 'left'), ('left', 'top'), ('right', 'top'), ('bottom', 'right'), ('left', 'bottom'), ('top', 'left')]:
                    valid = False
                    break
                if current_word in words:
                    current_solution.append(current_word)
                    current_word = ''
            current_word += letter
            current_side_sequence += sides[letter]
        if valid and current_word in words:
            current_solution.append(current_word)
            solutions.append(current_solution)
    # Find the solution with the fewest words that uses all letters exactly once
    return min(solutions, key=len, default=None)

def letter_boxed_solver(top, left, bottom, right, dictionary_file):
    sides = {
        **{letter: 'top' for letter in top},
        **{letter: 'left' for letter in left},
        **{letter: 'bottom' for letter in bottom},
        **{letter: 'right' for letter in right}
    }
    words = load_words(dictionary_file)
    return find_solutions(sides, words)

# Example usage
top = "ABCD"
left = "EFGH"
bottom = "IJKL"
right = "MNOP"
dictionary_file = "eng_words.txt"
solution = letter_boxed_solver(top, left, bottom, right, dictionary_file)
print("Solution:", solution)
