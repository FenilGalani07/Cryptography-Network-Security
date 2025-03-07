# Dictionary Merger

Welcome to the **Dictionary Merger** program! This Python script merges two dictionaries into one. If there are duplicate keys, the values from the second dictionary will overwrite those from the first.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Merges two dictionaries into one.
- Handles duplicate keys by overwriting values from the first dictionary with those from the second.
- Simple and easy to use.

## How It Works

The program defines a function `merge_dictionaries` that:
1. Takes two dictionaries as input.
2. Creates a copy of the first dictionary.
3. Uses the `update()` method to add the second dictionary to the copy.
4. Returns the merged dictionary.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Modify the example dictionaries in the script as needed.

### Example

```python
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'd': 4}

    merged_dict = merge_dictionaries(dict1, dict2)
    print("Merged Dictionary:", merged_dict)
```

### Sample Output

```
Merged Dictionary: {'a': 1, 'b': 3, 'c': 3, 'd': 4}
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

