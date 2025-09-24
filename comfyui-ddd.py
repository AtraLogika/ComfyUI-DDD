import torch

class Create3DImage:
    output_types = ["crosseyed", "SBS"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "output_type": (cls.output_types,)
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "create_3d_image"
    CATEGORY = "image/processing"
    OUTPUT_IS_LIST = (False,)

    def create_3d_image(self, images, output_type):
        # Check if we have at least 5 images
        if len(images) < 9:
            raise ValueError("At least 9 images are required in the input batch")

       # Extract the 8th and 9th images (0-indexed indices 7 and 8)
        left_eye  = images[5]  # Shape: [height, width, channels]
        right_eye = images[4]  # Shape: [height, width, channels]

        # Convert to CHW format (channels, height, width)
        left_eye_chw  = left_eye.permute(2, 0, 1)  # Shape: [channels, height, width]
        right_eye_chw = right_eye.permute(2, 0, 1)  # Shape: [channels, height, width]

        # Concatenate along width dimension
        if output_type == 'SBS':
            concatenated_chw = torch.cat((left_eye_chw, right_eye_chw), dim=2)  # Shape: [channels, height, width*2]
        else:
            concatenated_chw = torch.cat((right_eye_chw, left_eye_chw), dim=2)  # Shape: [channels, height, width*2]

        # Convert back to ComfyUI's expected format: [batch, height, width, channels]
        concatenated = concatenated_chw.permute(1, 2, 0).unsqueeze(0)  # Shape: [1, height, width*2, channels]

        return (concatenated,)



NODE_CLASS_MAPPINGS = {
    "Create3DImage": Create3DImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Create3DImage": "Create 3D Image [AtraLogika]"
}
