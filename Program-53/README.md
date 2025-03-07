# File Extension Extractor

Welcome to the **File Extension Extractor** program! This Python script extracts and displays the file extension from a specified file name. It's a useful tool for file management and organization.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Extracts the file extension from a given file name.
- Validates the file name to ensure it has an extension.
- Simple and easy to use.

## How It Works

The program defines a function `get_file_extension` that:
1. Takes a file name as input.
2. Uses `os.path.splitext()` to split the file name into its name and extension.
3. Returns the file extension.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the file name (with extension) when prompted.

### Example

```python
import os

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]

if __name__ == "__main__":
    file_name = input("Enter the file name (with extension): ")

    if os.path.isfile(file_name) or os.path.splitext(file_name)[1]:  # Check if it has an extension
        file_extension = get_file_extension(file_name)
        print(f"The file extension is: '{file_extension}'")
    else:
        print("The specified file name does not have a valid extension.")
```

### Sample Output

```
Enter the file name (with extension): example.txt
The file extension is: '.txt'
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

