"""
This module provides functionality to add watermarks (either text or image) to images.
Functions:
    get_predefined_position(image_size: tuple[int, int], watermark_size: tuple[int, int],
    position: str) -> tuple[int, int]: add_watermark(input_image_path: str,
    output_image_path: str, watermark_data: str, position: Union[str,
    tuple[int, int]] = "bottom-right", watermark_type: str = "image",
    font_size: int = 30, opacity: int = 128) -> None:main() -> None:
    Parses command-line arguments and calls the add_watermark function with the parsed arguments.
"""
import argparse
from typing import Union, Tuple
from PIL import Image, ImageDraw, ImageFont

def get_predefined_position(image_size: Tuple[int, int], watermark_size: Tuple[int, int],
                            position: str) -> Tuple[int, int]:
    """
    Calculates the position of the watermark based on predefined positions.
    
    :param image_size: Tuple (width, height) of the image.
    :param watermark_size: Tuple (width, height) of the watermark.
    :param position: Predefined position string ('top-left', 'center', 'bottom-right').
    :return: (x, y) tuple for the watermark position.
    """
    image_width, image_height = image_size
    watermark_width, watermark_height = watermark_size
    if position == "center":
        return (image_width - watermark_width) // 2, (image_height - watermark_height) // 2
    if position == "bottom-right":
        return image_width - watermark_width - 10, image_height - watermark_height - 10
    if position == "top-left":
        return 10, 10
    raise ValueError("Invalid predefined position. Use 'center', 'bottom-right', or 'top-left'.")

def add_watermark(
    input_image_path: str,
    output_image_path: str,
    watermark_data: str,
    position: Union[str, Tuple[int, int]] = "bottom-right",
    watermark_type: str = "image",
    font_size: int = 30,
    opacity: int = 128
) -> None:
    """
    Adds a watermark (image or text) to an image at a custom or predefined position.

    :param input_image_path: Path to the input image.
    :param output_image_path: Path to save the output image with watermark.
    :param watermark_data: Path to the watermark image or the text for watermarking.
    :param position: Position for the watermark ('top-left', 'center', 'bottom-right'
      or custom (x, y)).
    :param watermark_type: Type of watermark ('image' or 'text').
    :param font_size: Font size for text watermark.
    :param opacity: Opacity of the watermark (0 to 255).
    """
    try:
        # Open the image
        image = Image.open(input_image_path).convert("RGBA")

        if watermark_type == 'image':
            image = add_image_watermark(image, watermark_data, position, opacity)
        elif watermark_type == 'text':
            image = add_text_watermark(image, watermark_data, position, font_size, opacity)
        else:
            raise ValueError("Invalid watermark type. Use 'image' or 'text'.")

        # Save the final image with watermark
        image.save(output_image_path, "PNG")
        print(f"Watermarked image saved to {output_image_path}")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")

def add_image_watermark(image: Image.Image, watermark_data: str,
                        position: Union[str, Tuple[int, int]], opacity: int) -> Image.Image:
    """
    Adds an image watermark to the given image.

    :param image: The original image.
    :param watermark_data: Path to the watermark image.
    :param position: Position for the watermark ('top-left', 'center',
                                                'bottom-right' or custom (x, y)).
    :param opacity: Opacity of the watermark (0 to 255).
    :return: Image with the watermark.
    """
    image_width, _ = image.size
    watermark = Image.open(watermark_data).convert("RGBA")
    watermark_width, watermark_height = watermark.size

    # If position is a string, use predefined logic
    if isinstance(position, str):
        position = get_predefined_position(image.size, watermark.size, position)

    # Resize watermark if needed (optional, based on original image size)
    scale_factor = 0.1  # Resize watermark to 10% of image width (adjust if needed)
    new_width = int(image_width * scale_factor)
    new_height = int(watermark_height * (new_width / watermark_width))
    watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Apply opacity to watermark
    watermark_with_opacity = watermark.copy()
    watermark_with_opacity.putalpha(opacity)

    # Paste watermark onto the image
    image.paste(watermark_with_opacity, position, watermark_with_opacity)
    return image

def add_text_watermark(image: Image.Image, watermark_data: str,
                        position: Union[str, tuple[int, int]],
                        font_size: int, opacity: int) -> Image.Image:
    """
    Adds a text watermark to the given image.

    :param image: The original image.
    :param watermark_data: The text for watermarking.
    :param position: Position for the watermark
     ('top-left', 'center', 'bottom-right' or custom (x, y)).
    :param font_size: Font size for text watermark.
    :param opacity: Opacity of the watermark (0 to 255).
    :return: Image with the watermark.
    """
    watermark_text = watermark_data
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size using textbbox
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # If position is a string, use predefined logic
    if isinstance(position, str):
        position = get_predefined_position(image.size, (text_width, text_height), position)

    # Apply opacity to text
    watermark_overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark_overlay)
    watermark_draw.text(position, watermark_text, font=font, fill=(255, 255, 255, opacity))

    # Combine image with text watermark
    return Image.alpha_composite(image, watermark_overlay)

def main():
    """
    Main function to add a watermark (text or image) to an image.
    This function sets up the argument parser to handle command-line arguments
    and calls the add_watermark function with the parsed arguments.
    Command-line arguments:
    - input_image (str): Path to the input image.
    - output_image (str): Path to save the output image with the watermark.
    - watermark_data (str): Path to the watermark image or the text for watermarking.
    - --position (str, optional): Position of the watermark. Choices are "top-left", 
    "center", "bottom-right".
        Default is "bottom-right".
    - --watermark_type (str, optional): Type of watermark. Choices are "image" or "text".
      Default is "image".
    - --font_size (int, optional): Font size for text watermark. Default is 30.
    - --opacity (int, optional): Opacity for the watermark. Range is 0 to 255.
      Default is 128.
    """

    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Add a watermark (text or image) to an image.")
    # Define command-line arguments
    parser.add_argument("input_image", help="Path to the input image.")
    parser.add_argument("output_image",
                         help="Path to save the output image with the watermark.")
    parser.add_argument("watermark_data",
                        help="Path to the watermark image or the text for watermarking.")
    parser.add_argument("--position", default="bottom-right",
                         choices=["top-left", "center", "bottom-right"],
                        help="Position of the watermark (default: bottom-right).")
    parser.add_argument("--watermark_type", default="image", choices=["image", "text"],
                        help="Type of watermark: 'image' or 'text' (default: image).")
    parser.add_argument("--font_size", type=int, default=30,
                        help="Font size for text watermark (default: 30).")
    parser.add_argument("--opacity", type=int, default=128, choices=range(0, 256),
                        help="Opacity for the watermark (default: 128).")
    # Parse the arguments
    args = parser.parse_args()
    # Call the add_watermark function with the parsed arguments
    add_watermark(
        input_image_path=args.input_image,
        output_image_path=args.output_image,
        watermark_data=args.watermark_data,
        position=args.position,
        watermark_type=args.watermark_type,
        font_size=args.font_size,
        opacity=args.opacity
    )

if __name__ == "__main__":
    main()
