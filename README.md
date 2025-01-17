# inked

inked is a simple Python package that allows you to add **image** or **text** watermarks to your images. You can position the watermark anywhere on the image using custom or predefined positions.

## Installation

You can install the package using pip:

```bash
pip install inked
```
## Usage

### Command-Line Interface (CLI)
Once Inked is installed, you can use the add-watermark command in your terminal to add watermarks to images.

### Add an Image Watermark
You can add an image watermark to an image using the following command:

```bash
add-watermark input_image.jpg output_image.png watermark_image.png --position bottom-right --opacity 150
```

### Arguments:

- input_image.jpg: Path to the input image.
- output_image.png: Path where the watermarked image will be saved.
- watermark_image.png: Path to the watermark image (can be any image file like PNG).
- --position bottom-right: Position of the watermark on the image.
    -  You can choose from:
   (top-left: Top-left corner of the image.,- center: Center of the image.,- bottom-right: Bottom-right corner of the image.)
    - You can also provide a custom position as a pair of coordinates (e.g., --position 100,200).
- --opacity 150: Opacity of the watermark (range: 0 to 255). Lower values are more transparent.

### Add a Text Watermark
You can add a text watermark to an image with the following command:

```bash
add-watermark input_image.jpg output_image.png "Watermark Text" --position center --watermark_type text --font_size 40 --opacity 200
```
### Arguments:

- "Watermark Text": The text to be used as a watermark.
- --position center: Position of the text watermark on the image.
    - Options include top-left, center, bottom-right, or - custom coordinates (e.g., --position 100,200).
- --watermark_type text: Specifies that the watermark is text, not an image.
- --font_size 40: Font size for the text watermark (default is 30).
- --opacity 200: Opacity of the text watermark (range: 0 to 255). Higher opacity means the text will be more visible.

## Example Usage
### Example 1: Add an Image Watermark to an Image

```bash
add-watermark nature.jpg nature_watermarked.jpg logo.png --position bottom-right --opacity 180
```
Adds logo.png as a watermark in the bottom-right corner of nature.jpg, with an opacity of 180, and saves the result as nature_watermarked.jpg.

### Example 2: Add a Text Watermark with Custom Font Size

```bash

add-watermark beach.jpg beach_watermarked.jpg "Confidential" --position top-left --watermark_type text --font_size 50 --opacity 100
```
Adds the text "Confidential" to the top-left corner of beach.jpg, with a font size of 50 and an opacity of 100, and saves it as beach_watermarked.jpg.

### Example 3: Custom Positioning for an Image Watermark

``` bash

add-watermark landscape.jpg landscape_watermarked.jpg watermark.png --position 100,100 --opacity 128

```

Adds watermark.png to the coordinates (100, 100) on landscape.jpg with opacity 128, and saves it as landscape_watermarked.jpg.

## Programmatic Usage (Python API)
You can also use the package programmatically within a Python script.

### Example: Add an Image Watermark Programmatically

``` python
from inked import add_watermark

input_image = "input_image.jpg"
output_image = "output_image.png"
watermark_image = "watermark_image.png"
position = "bottom-right"
opacity = 150

add_watermark(input_image, output_image, watermark_image, position=position, opacity=opacity)


```

### Example: Add a Text Watermark Programmatically

``` python
from inked import add_watermark

input_image = "input_image.jpg"
output_image = "output_image.png"
watermark_text = "Confidential"
position = "center"
font_size = 40
opacity = 200

add_watermark(input_image, output_image, watermark_data=watermark_text, 
              position=position, watermark_type="text", 
              font_size=font_size, opacity=opacity)

```

## License
This project is licensed under the MIT License.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Please make sure to follow the contribution guidelines and ensure tests are included with your changes.

## Authors
Sumesh.K-  [GitHub](https://github.com/ksumesh21/inked)







