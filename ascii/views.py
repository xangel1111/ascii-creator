import requests
from io import BytesIO
from django.shortcuts import render
from asciiartist import asciiartist, display_edges
from PIL import Image

Image.CUBIC = Image.BICUBIC

def ascii_show(req):
  art = None

  if (req.method == "POST"):
    url = req.POST.get('image-url')
    image_file = req.FILES.get('image')

    if url and image_file:
       raise ValueError("choose only one")
    
    if url:
      response = requests.get(url)
      img = Image.open(BytesIO(response.content))  

    if image_file:
      if image_file and hasattr(image_file, 'read'):
          img = Image.open(image_file)
      else:
          raise ValueError("Not a valid image.")
      
    art, e1dges = asciiartist(
          img, # The image!
          100,  # Number of lines of the output ascii art
          noise_reduction=2,  # Level of noise reduction (optional)
          line_weight=1,      # Weight of the lines to draw (optional)
          text_ratio=2.2      # Height/width ratio of each character (optional)
      )
    print(art)
    
  return render(req, "ascii/index.html", {'ascii': art})