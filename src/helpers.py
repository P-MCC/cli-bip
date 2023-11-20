import os
import cv2

def getImageList(path):
    """
    Get a list of all image files in the specified directory.
    """
    try:
        image_list = [file for file in os.listdir(path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif'))]
        return image_list
    except OSError as e:
        print(f"Error accessing directory {path}: {e}")
        return []

def getImage(imgName):
    """
    Read and return the specified image file using OpenCV.
    """
    try:
        img = cv2.imread(imgName)
        if img is None:
            raise FileNotFoundError(f"Image not found: {imgName}")
        return img
    except Exception as e:
        print(f"Error loading image {imgName}: {e}")
        return None

def writeImage(imgName, img, path):
    """
    Write the image data to a file with the specified name in the specified directory using OpenCV.
    """
    try:
        cv2.imwrite(os.path.join(path, imgName), img)
        print(f"Image {imgName} saved successfully.")
    except Exception as e:
        print(f"Error saving image {imgName}: {e}")