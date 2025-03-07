# File Name Extractor

Welcome to the **File Name Extractor** program! This Python script retrieves and displays the file name from a specified file path. It's a useful tool for file management and navigation.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Extracts the file name from a given file path.
- Validates the file path before attempting to retrieve the file name.
- Simple and easy to use.

## How It Works

The program defines a function `get_file_name` that:
1. Takes a file path as input.
2. Uses `os.path.basename()` to extract the file name from the provided path.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the full path of the file when prompted.

### Example

```python
import os

def get_file_name(file_path):
    return os.path.basename(file_path)

if __name__ == "__main__":
    file_path = input("Enter the full path of the file: ")

    if os.path.isfile(file_path):
        file_name = get_file_name(file_path)
        print(f"The file name is: {file_name}")
    else:
        print("The specified path is not a valid file.")
```

### Sample Output

```
Enter the full path of the file: /path/to/your/file.txt
The file name is: file.txt
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

