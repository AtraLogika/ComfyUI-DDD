# ComfyUI-DDD
Generate 3D pictures with AI or convert a 2D photo to 3D
Comfyui-DDD lets you convert 2D images to 3D, or generate 3D images (spatial images) from text.

# Features

- Convert 2D images to 3D images (3D-I2V)
- Generate 3D images with a text prompt (3D-T2V)
- Works with 12 GB VRAM and 32 GB ram
- Does not require any depth estimation model such as Midas, AnyDepth, etc.
- Does not require extra python packages

# Requirements

The current version uses WAN 2.2 as a base model. The WAN 2.2 I2V model is used for 2D to 3D conversion and the WAN 2.2 T2V model is used for 3D image generation.

# Installing

- Place comfyui-ddd.py in your ComfyUI custom_nodes folder
- Download [high lora] and [low lora] and place in your loras folder
  https://huggingface.co/AtraLogika/ComfyUI-DDD/tree/main

# How to convert 2D images to 3D

- Download example workflow (coming soon)

# How to generate 3D images from a text prompt

- Download example workflow (coming soon)
