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