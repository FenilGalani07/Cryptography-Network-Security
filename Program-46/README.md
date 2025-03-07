# Anagram Checker

Welcome to the **Anagram Checker** program! This Python script checks if two strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Checks if two strings are anagrams.
- Ignores spaces and is case-insensitive.
- Simple and easy to use.

## How It Works

The program defines a function `are_anagrams` that:
1. Removes spaces and converts both strings to lowercase.
2. Sorts the characters of both strings.
3. Compares the sorted versions of the strings to determine if they are anagrams.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the two strings when prompted.

### Example

```python
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if are_anagrams(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')
```

### Sample Output

```
Enter the first string: listen
Enter the second string: silent
"listen" and "silent" are anagrams.
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)
