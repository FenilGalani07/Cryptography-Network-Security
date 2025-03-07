# Image Resolution Finder

Welcome to the **Image Resolution Finder** program! This Python script retrieves and displays the resolution (size) of a specified image file. It's a useful tool for image processing and analysis.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

## Features

- Retrieves the resolution (width and height) of an image.
- Handles various image formats (JPEG, PNG, etc.).
- Simple and easy to use.

## How It Works

The program defines a function `get_image_resolution` that:
1. Takes the path to an image file as input.
2. Uses the `PIL` (Pillow) library to open the image.
3. Retrieves the size of the image, which is returned as a tuple (width, height).

## Usage

1. Clone the repository or download the script.
2. Install the Pillow library if you haven't already:
   ```bash
   pip install Pillow
   ```
3. Run the script using Python 3.x.
4. Enter the path to the image file when prompted.

### Example

```python
from PIL import Image

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.size

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    try:
        width, height = get_image_resolution(image_path)
        print(f"The resolution of the image is: {width} x {height}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Sample Output

```
Enter the path to the image file: example.jpg
The resolution of the image is: 1920 x 1080
```

## Requirements

- Python 3.x
- Pillow library (install using `pip install Pillow`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Fenil Galani
[GitHub Profile](https://github.com/FenilGalani07/Cryptography-Network-Security_2.git)

