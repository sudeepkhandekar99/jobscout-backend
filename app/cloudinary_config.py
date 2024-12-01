import os
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_URL_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_URL_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_URL_API_SECRET"),
)

def upload_image_to_cloudinary(file, folder: str):
    """
    Uploads an image to Cloudinary.
    Args:
        file: The file object to upload.
        folder: The folder name in Cloudinary.
    Returns:
        The URL of the uploaded image.
    """
    response = cloudinary.uploader.upload(file.file, folder=folder)
    return response["secure_url"]
