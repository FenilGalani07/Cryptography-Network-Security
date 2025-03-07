# Current Working Directory Path Retriever

Welcome to the **Current Working Directory Path Retriever** program! This Python script retrieves and displays the full path of the current working directory. It's a useful tool for file management and navigation in your projects.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Retrieves the full path of the current working directory.
- Simple and easy to use.
- Useful for file management tasks.

## How It Works

The program uses the `os` module to access the operating system's functionality. The `os.getcwd()` function is called to get the current working directory, which is then printed to the console.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.

### Example

```python
import os

def get_current_working_directory():
    return os.getcwd()

if __name__ == "__main__":
    current_directory = get_current_working_directory()
    print(f"The full path of the current working directory is: {current_directory}")
```

### Sample Output

```
The full path of the current working directory is: D:\Cryptography-Network-Security_2\Cryptography-Network-Security_2
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)