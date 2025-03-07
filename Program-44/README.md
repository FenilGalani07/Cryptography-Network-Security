# Unique Permutations Generator

Welcome to the **Unique Permutations Generator**! This Python script generates all unique permutations of a given string. It's a useful tool for combinatorial problems, word games, and exploring different arrangements of characters.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Generates all unique permutations of a given string.
- Handles duplicate characters efficiently.
- Displays permutations in a sorted order for easy viewing.

## How It Works

The program uses the `itertools.permutations` function to generate all possible arrangements of the input string. It then converts these permutations into a set to ensure uniqueness and returns the result. The unique permutations are then printed in sorted order.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the desired string when prompted.

### Example

```python
import itertools

def compute_permutations(input_string):
    permutations = itertools.permutations(input_string)
    unique_permutations = set([''.join(p) for p in permutations])
    return unique_permutations

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = compute_permutations(user_input)
    print(f"All unique permutations of '{user_input}':")
    for perm in sorted(result):
        print(perm)
```

### Sample Output

```
Enter a string: abc
All unique permutations of 'abc':
abc
acb
bac
bca
cab
cba
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

