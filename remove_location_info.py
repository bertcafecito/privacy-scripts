import os
from PIL import Image

input_directory = "photos/input"
output_directory = "photos/output"

def remove_exif_from_images():
    for filename in os.listdir(input_directory):
        print(f"Processing file: {filename}")
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, filename)
            try:
                with Image.open(input_filepath) as img:
                    if "exif" in img.info:
                        data = list(img.getdata())
                        new_img = Image.new(img.mode, img.size)
                        new_img.putdata(data)
                        new_img.save(output_filepath)
                        print(f"Stripped location info from: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    remove_exif_from_images()

if __name__ == "__main__":
    main()