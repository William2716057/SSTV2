import os
from PIL import Image
from pysstv.color import Robot36
import numpy as np

def encode_image_to_sstv(image_path, output_path):
    # Load image
    image = Image.open(image_path)
    
    # Convert to RSB
    image = image.convert("RGB")
    
    # Create instance of  SSTV encoder with the Robot36 mode
    samples_per_sec = 11025  # Common sample rate
    bits = 16  # Common bit depth
    
    sstv = Robot36(image, samples_per_sec, bits)
    
    # Encode image to SSTV, save it to a WAV file
    with open(output_path, "wb") as f:
        sstv.write_wav(f)
    
    print(f"SSTV signal saved to {output_path}")

if __name__ == "__main__":
    # Set input and output paths
    input_image = "sample.jpg"
    output_wav = "output_sstv.wav"
    
    # Encode image to SSTV
    encode_image_to_sstv(input_image, output_wav)