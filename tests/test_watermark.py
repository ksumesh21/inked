"""
Unit tests for the watermark functionality in the inked package.
This module contains test cases for the add_watermark function, which is responsible for
adding image and text watermarks to images. The tests ensure that the function correctly
applies the specified watermarks and saves the output images.
Classes:
    TestWatermark: A test case class for testing the add_watermark function.
Usage:
    Run this module with a test runner to execute the unit tests.

"""
import os
import unittest
from inked.watermark import add_watermark

class TestWatermark(unittest.TestCase):
    """
    Test suite for the watermark functionality.
    This class contains unit tests for the `add_watermark` function, which is responsible for adding
    both image and text watermarks to images. The tests verify that the function correctly processes
    the input images and generates the expected output images with the specified watermarks.
    Methods:
        test_add_image_watermark: Tests the addition of an image watermark to an input image.
        test_add_text_watermark: Tests the addition of a text watermark to an input image.
    """
    def test_add_image_watermark(self):
        """
        Test the add_watermark function by adding an image watermark to an input image.
        This test verifies that the add_watermark function correctly adds an image watermark
        to the specified input image and saves the result to the output image path. It also
        checks that the output file is created successfully.
        Steps:
        1. Define the paths for the input image, output image, and watermark image.
        2. Call the add_watermark function with the specified parameters.
        3. Assert that the output image file is created.
        Raises:
            AssertionError: If the output image file is not created.
        """

        input_image_path = "tests/input_image.webp"
        output_image_path = "tests/output_image_with_image_watermark.jpg"
        watermark_image_path = "tests/watermark.webp"
        # Call add_watermark function
        add_watermark(input_image_path, output_image_path,
                       watermark_image_path, position="center", watermark_type="image")
        # Ensure the output file is created
        self.assertTrue(os.path.exists(output_image_path))
    def test_add_text_watermark(self):
        """
        Test the add_watermark function by adding a text watermark to an image.
        This test verifies that the add_watermark function correctly adds a text watermark
        to the specified input image and saves the output image with the watermark applied.
        It checks if the output image file exists after the function is executed.
        Args:
            self: The instance of the test case.
        Raises:
            AssertionError: If the output image file does not exist.
        """

        input_image_path = "tests/input_image.webp"
        output_image_path = "tests/output_image_with_text_watermark.jpg"
        watermark_text = "Sample Watermark"
        add_watermark(input_image_path, output_image_path,
                      watermark_text, position="bottom-right", watermark_type="text",
                        font_size=30, opacity=128)
        self.assertTrue(os.path.exists(output_image_path))

if __name__ == "__main__":
    unittest.main()
