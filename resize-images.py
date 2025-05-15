from PIL import Image
import os
import shutil  # Import the shutil module for copying files


def resize_image(image_path, output_dir="resized_images", max_size=4000):
    """
    Resizes an image so that its longest side is at most max_size pixels.
    Always copies the image to the output directory.

    Args:
        image_path (str): The path to the input image file.
        output_dir (str, optional): The directory to save the (potentially resized) image.
                                     Defaults to "resized_images".
        max_size (int, optional): The maximum length of the longest side
                                   in pixels. Defaults to 4000.
    """
    try:
        img = Image.open(image_path)
        width, height = img.size
        resized = False

        if width > height:
            if width > max_size:
                new_width = max_size
                new_height = int(height * (new_width / width))
                resized_img = img.resize((new_width, new_height))
                print(
                    f"Resized {image_path} from {width}x{height} to {new_width}x{new_height}"
                )
                save_image(resized_img, image_path, output_dir, suffix="_resized")
                resized = True
        else:
            if height > max_size:
                new_height = max_size
                new_width = int(width * (new_height / height))
                resized_img = img.resize((new_width, new_height))
                print(
                    f"Resized {image_path} from {width}x{height} to {new_width}x{new_height}"
                )
                save_image(resized_img, image_path, output_dir, suffix="_resized")
                resized = True

        if not resized:
            copy_original_image(image_path, output_dir)

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred processing {image_path}: {e}")


def save_image(image, original_path, output_dir, suffix=""):
    """
    Saves the image to the specified output directory.

    Args:
        image (PIL.Image.Image): The image object to save.
        original_path (str): The original path of the image (for naming).
        output_dir (str): The directory to save the image.
        suffix (str, optional): The suffix to add to the filename. Defaults to "".
    """
    os.makedirs(output_dir, exist_ok=True)
    base, ext = os.path.splitext(os.path.basename(original_path))
    output_path = os.path.join(output_dir, f"{base}{suffix}{ext}")
    try:
        image.save(output_path)
        print(f"Saved image to {output_path}")
    except Exception as e:
        print(f"Error saving {output_path}: {e}")


def copy_original_image(image_path, output_dir):
    """
    Copies the original image to the output directory.

    Args:
        image_path (str): The path to the original image file.
        output_dir (str): The directory to copy the image to.
    """
    os.makedirs(output_dir, exist_ok=True)
    try:
        destination_path = os.path.join(output_dir, os.path.basename(image_path))
        shutil.copy2(image_path, destination_path)  # copy2 preserves metadata
        print(f"Copied {os.path.basename(image_path)} to {output_dir}")
    except Exception as e:
        print(f"Error copying {image_path}: {e}")


def process_directory(input_dir, output_dir="resized_images", max_size=4000):
    """
    Processes all image files in a given directory.

    Args:
        input_dir (str): The path to the directory containing images.
        output_dir (str, optional): The directory to save (potentially resized) images.
                                     Defaults to "resized_images".
        max_size (int, optional): The maximum length of the longest side.
                                   Defaults to 4000.
    """
    for filename in os.listdir(input_dir):
        if is_image_file(filename):
            image_path = os.path.join(input_dir, filename)
            resize_image(image_path, output_dir, max_size)


def is_image_file(filename):
    """
    Checks if a filename has a common image file extension.

    Args:
        filename (str): The name of the file.

    Returns:
        bool: True if the filename suggests an image file, False otherwise.
    """
    extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    return any(filename.lower().endswith(ext) for ext in extensions)


if __name__ == "__main__":
    print("Image Resizing and Copying Script")
    print("---------------------------------")

    mode = input(
        "Do you want to process a single image (s) or a directory of images (d)? (s/d): "
    ).lower()

    if mode == "s":
        image_path = input("Enter the path to the image file: ")
        output_dir = (
            input("Enter the output directory (leave blank for 'resized_images'): ")
            or "resized_images"
        )
        try:
            max_size_input = input(
                f"Enter the maximum size for the longest side (default: 4000): "
            )
            max_size = int(max_size_input) if max_size_input else 4000
            resize_image(image_path, output_dir, max_size)
        except ValueError:
            print("Invalid input for maximum size. Using default value of 4000.")
            resize_image(image_path, output_dir)
    elif mode == "d":
        input_dir = input("Enter the path to the directory containing images: ")
        output_dir = (
            input("Enter the output directory (leave blank for 'resized_images'): ")
            or "resized_images"
        )
        try:
            max_size_input = input(
                f"Enter the maximum size for the longest side (default: 4000): "
            )
            max_size = int(max_size_input) if max_size_input else 4000
            process_directory(input_dir, output_dir, max_size)
        except ValueError:
            print("Invalid input for maximum size. Using default value of 4000.")
            process_directory(input_dir, output_dir)
    else:
        print(
            "Invalid mode selected. Please enter 's' for single image or 'd' for directory."
        )
