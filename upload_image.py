import os
from PIL import Image

def upload_image():
    while True:
        file_path = input("Enter the path to your image file: ")

        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    print(f"Successfully uploaded {file_path}")
                    return file_path  
                
            except IOError:
                print("The file is not a valid image. Please try again.")
        else:
            print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    upload_image()
