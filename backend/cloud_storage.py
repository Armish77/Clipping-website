import cloudinary
import cloudinary.uploader

# Put your real Cloudinary credentials later
cloudinary.config(
    cloud_name="YOUR_CLOUD_NAME",
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
    secure=True
)

def upload(video_path):
    """
    Uploads video to cloud storage and returns public URL
    """
    result = cloudinary.uploader.upload(
        video_path,
        resource_type="video"
    )
    return result["secure_url"]
