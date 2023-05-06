import os
import sys
from PIL import Image

def resize_image(input_image_path, output_image_path, new_width, new_height):
    with Image.open(input_image_path) as img:
        width, height = img.size
        aspect_ratio = float(width) / float(height)
        
        if new_width and not new_height:
            new_height = int(new_width / aspect_ratio)
        elif new_height and not new_width:
            new_width = int(new_height * aspect_ratio)
        elif not new_width and not new_height:
            raise ValueError("You must provide at least one dimension (width or height)")

        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(output_image_path)

def process_images(source_directory, target_directory, new_width=None, new_height=None):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_image_path = os.path.join(source_directory, filename)
            output_image_path = os.path.join(target_directory, filename)
            resize_image(input_image_path, output_image_path, new_width, new_height)

def main():
    if len(sys.argv) < 4:
        print("Usage: python bulk_image_resizer.py <source_directory> <target_directory> <new_width> [<new_height>]")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    new_width = int(sys.argv[3])
    new_height = int(sys.argv[4]) if len(sys.argv) >= 5 else None

    process_images(source_directory, target_directory, new_width, new_height)


if __name__ == "__main__":
    main()
