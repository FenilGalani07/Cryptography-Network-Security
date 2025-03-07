# Alphabetical Word Sorter

Welcome to the **Alphabetical Word Sorter** program! This Python script sorts the words in a given string in alphabetical order. It's a simple utility for text processing and organization.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Sorts words in a string in alphabetical order.
- Handles case sensitivity by default (uppercase letters will precede lowercase).
- Simple and easy to use.

## How It Works

The program defines a function `sort_words` that:
1. Splits the input string into words using the `split()` method.
2. Sorts the list of words using the `sort()` method.
3. Returns the sorted list of words.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the string when prompted.

### Example

```python
def sort_words(input_string):
    words = input_string.split()
    words.sort()
    return words

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    sorted_words = sort_words(user_input)

    print("Sorted words in alphabetical order:")
    print(", ".join(sorted_words))
```

### Sample Output

```
Enter a string: banana apple orange grape
Sorted words in alphabetical order:
apple, banana, grape, orange
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

