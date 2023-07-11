import os
from PIL import Image

def change_format(input_dir, picture_format, keep=True):
    # Loop over each file in the directory
    for instance in os.listdir(input_dir):
        if not os.path.isdir(os.path.join(input_dir, instance)):
            print("Yaw maan, that ain´t a directory.... Skipping")
            continue
        else:
            folder = os.path.join(input_dir, instance)
            
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file, dot, file_ending = filename.rpartition(".")
                image_path = os.path.join(folder, filename)
                
                # Open the image
                try:
                    im1 = Image.open(image_path)
                except IOError:
                    print(f"Error: Cannot open {filename}. Skipping...")
                    continue

                # Check if the image is already in the desired format
                if file_ending.lower() in picture_format.lower():
                    print(f"The file {filename} is already in {picture_format} format")
                    continue

                # Convert and save the image
                if file_ending.lower() == "png" and picture_format.lower() in ("jpeg", "jpg", ".jpeg", ".jpg"):
                    file_ending = picture_format
                    im1 = im1.convert('RGB') 
                elif file_ending.lower() in ("jpeg", "jpg", ".jpeg", ".jpg") and picture_format.lower() in (".png", "png"):
                    file_ending = picture_format
                    im1 = im1.convert('RGBA') 

                new_filename = file + "." + file_ending
                new_filepath = os.path.join(folder, new_filename)
                im1.save(new_filepath)

                if not keep:
                    os.remove(image_path) 

                print(f"The image {filename} has been changed to the {file_ending} format.")
            else:
                print(f"{filename} is not an image file. Skipping...")


def resize_images(input_dir, target_size):
    os.makedirs(os.path.join(input_dir, "_resized"), exist_ok=True)  # Create a new directory '_resized' in input_dir, saves to state the output directory
    output_dir = os.path.join(input_dir, "_resized")
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):  # Adjust file extensions as needed
            # Open the image
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            
            # Resize the image
            resized_image = image.resize(target_size)
            
            # Save the resized image

            output_path = os.path.join(output_dir, filename)
            resized_image.save(output_path)
            
            print(f"Resized {filename} to {target_size}")
        print("Image resizing complete!")




# if __name__ == "__main__":
