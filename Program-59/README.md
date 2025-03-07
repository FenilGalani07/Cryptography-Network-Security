# Vowel Counter

Welcome to the **Vowel Counter** program! This Python script counts the number of occurrences of each vowel (a, e, i, o, u) in a given string. It is case-insensitive and provides a simple utility for text analysis.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Counts the occurrences of each vowel in a string.
- Case-insensitive counting.
- Simple and easy to use.

## How It Works

The program defines a function `count_vowels` that:
1. Initializes a dictionary to hold the count of each vowel.
2. Converts the input string to lowercase to ensure case-insensitivity.
3. Iterates through each character in the string and increments the count for each vowel found.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the string when prompted.

### Example

```python
def count_vowels(input_string):
    vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    input_string = input_string.lower()

    for char in input_string:
        if char in vowels_count:
            vowels_count[char] += 1

    return vowels_count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vowel_counts = count_vowels(user_input)

    print("Vowel counts:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")
```

### Sample Output

```
Enter a string: Hello World!
Vowel counts:
a: 0
e: 1
i: 0
o: 2
u: 0
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

