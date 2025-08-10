import warnings
warnings.filterwarnings("ignore")

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load the BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image from a URL
image_url = "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759"
image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")

# Prepare inputs and generate caption
inputs = processor(image, return_tensors="pt")
output = model.generate(**inputs)
caption = processor.decode(output[0], skip_special_tokens=True)

# Output the result
print("\n Generated Caption:", caption)
