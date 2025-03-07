# File Creation and Modification Date Retriever

Welcome to the **File Creation and Modification Date Retriever** program! This Python script retrieves and displays the creation and modification dates of a specified file. It's a useful tool for file management and auditing.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Retrieves the creation and modification dates of a specified file.
- Displays dates in a human-readable format.
- Validates the file path before attempting to retrieve dates.

## How It Works

The program defines a function `get_file_dates` that:
1. Takes a file path as input.
2. Uses `os.path.getctime()` to get the creation time and `os.path.getmtime()` to get the modification time.
3. Converts the timestamps to a human-readable format using `datetime.fromtimestamp()`.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the full path of the file when prompted.

### Example

```python
import os
from datetime import datetime

def get_file_dates(file_path):
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    creation_time = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    modification_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
    return creation_time, modification_time

if __name__ == "__main__":
    file_path = input("Enter the full path of the file: ")

    if os.path.isfile(file_path):
        creation_date, modification_date = get_file_dates(file_path)
        print(f"Creation Date: {creation_date}")
        print(f"Modification Date: {modification_date}")
    else:
        print("The specified path is not a valid file.")
```

### Sample Output

```
Enter the full path of the file: /path/to/your/file.txt
Creation Date: 2023-01-15 10:30:45
Modification Date: 2023-02-20 14:15:30
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)
