from manim import *
import random
from PIL import Image, ImageFilter
import numpy as np

class AES_CTR_128_algorithm(Scene):
    def construct(self):
        # Add a title to the scene and display it for 2 seconds
        title = Text('AES - CTR Encryption Process').scale(1)
        self.add(title)
        self.wait(2)
        # Fade out the title by shifting it downward and scaling it up
        self.play(FadeOut(title, shift=DOWN * 2, scale=3))
       
        # Introduce the first paragraph and display it
        first_paragraph = Text('We would like to encrypt an image')
        self.play(FadeIn(first_paragraph, shift=DOWN, scale=0.66))
        self.wait(1)
        # Shift the first paragraph upward to make space
        self.play(first_paragraph.animate.shift(UP * 3))
       
        # Step 1: Load the image using ImageMobject and position it at the center
        image_path = "C:/Users/User/source/repos/images/Lena.png"
        lena = ImageMobject(image_path)
        lena.scale(0.2).move_to(ORIGIN)  # Scale and center the image
        self.play(FadeIn(lena, shift=UP, scale=0.66))

        # Fade out the first paragraph by shifting it upward and scaling it up
        self.play(FadeOut(first_paragraph, shift=UP, scale=2))
       
        # Load the image using PIL for processing
        lena_image_pil = Image.open("C:/Users/User/source/repos/images/Lena.png")

        # Apply Gaussian blur to the image with a radius of 15
        blurred_lena_image = lena_image_pil.filter(ImageFilter.GaussianBlur(radius=15))

        # Save the blurred image as a temporary file
        blurred_lena_image.save("C:/Users/User/source/repos/images/blurred_lena.png")

        # Load and display the blurred image in Manim
        blurred_lena_mobject = ImageMobject("C:/Users/User/source/repos/images/blurred_lena.png")

        # Scale the original image and animate it scaling up
        self.play(lena.animate.scale(2.2), run_time=2)
        # Scale the blurred image and fade it into the scene
        blurred_lena_mobject = blurred_lena_mobject.scale(0.45)
        self.play(FadeIn(blurred_lena_mobject))
        # Fade out the original image
        self.play(FadeOut(lena))
     
        # Get the width and height of the blurred image in scene units
        image_width = blurred_lena_mobject.get_width()
        image_height = blurred_lena_mobject.get_height()

        # Define the number of horizontal and vertical lines for the grid
        num_horizontal_lines = 50
        num_vertical_lines = 50

        # Create a list to store all grid lines
        grid_lines = []

        # Create horizontal grid lines across the image
        for i in range(num_horizontal_lines + 1):  # Include the last line at the bottom
            y = image_height * (i / num_horizontal_lines) - (image_height / 2)
            horizontal_line = Line(
                start=[-image_width / 2, y, 0],
                end=[image_width / 2, y, 0],
                color=WHITE,
                stroke_width=1
            )
            grid_lines.append(horizontal_line)

        # Create vertical grid lines across the image
        for j in range(num_vertical_lines + 1):  # Include the last line on the right
            x = image_width * (j / num_vertical_lines) - (image_width / 2)
            vertical_line = Line(
                start=[x, -image_height / 2, 0],
                end=[x, image_height / 2, 0],
                color=WHITE,
                stroke_width=1
            )
            grid_lines.append(vertical_line)

        # Group all grid lines into a VGroup for easier manipulation
        grid_group = VGroup(*grid_lines)

        # Introduce the second paragraph and display the grid
        second_paragraph = Text('Let\'s divide the image into pixels')
        self.play(FadeIn(second_paragraph, shift=DOWN, scale=0.66))
        self.wait(1)
        # Fade out the second paragraph by shifting it upward and scaling it up
        self.play(FadeOut(second_paragraph, shift=UP, scale=2))
        
        # Define each line of the paragraph separately for better alignment
        line1 = Text(
            'Each pixel in an RGB image is assigned',
            font_size=30,
        )
        line2 = Text(
            'a value between 0 and 255 for each of the red, green, and blue channels,',
            font_size=30,
        )
        line3 = Text(
            'which together describe the color.',
            font_size=30,
        )

        # Group the lines vertically with spacing and center them
        paragraph_group = VGroup(line1, line2, line3).arrange(
            DOWN,  # Arrange lines vertically
            center=True,  # Center the group horizontally
            buff=0.5  # Space between lines
        )

        # Animate the paragraph group fading in from below with scaling
        self.play(FadeIn(paragraph_group, shift=DOWN, scale=0.5))
        self.wait(3)
        # Fade out the paragraph group by shifting it upward and scaling it up
        self.play(FadeOut(paragraph_group, shift=UP, scale=2))
        # Fade in the grid over the blurred image
        self.play(FadeIn(grid_group))
        self.wait(1)
        # Animate scaling up the blurred image and grid together over 6 seconds
        self.play(blurred_lena_mobject.animate.scale(10), grid_group.animate.scale(10), run_time=6)

        # Add a dot and RGB text to display pixel values
        dot = Dot(point=ORIGIN, color=WHITE, radius=0.2)  # Initial dot at the center
        rgb_text = Text("(Red, Green, Blue)", font_size=24).next_to(dot, RIGHT)  # Text next to the dot

        # Fade in the dot and RGB text
        self.play(FadeIn(dot), FadeIn(rgb_text))

        # Define points on the image to sample pixel values
        points = [
            [-5, -3, 0],  # Top-left
            [-4, 2, 0],
            [1, -3, 0],
            [-4, -2, 0]   # Center-right
        ]

        # Get image position and dimensions in scene units
        image_position = blurred_lena_mobject.get_center()
        image_width = blurred_lena_mobject.get_width()
        image_height = blurred_lena_mobject.get_height()

        # Iterate through each point to display corresponding RGB values
        for point in points:
            # Extract Manim coordinates
            x_manim = point[0]
            y_manim = point[1]

            # Convert Manim coordinates to pixel coordinates
            pixel_x = int(((x_manim - image_position[0]) / image_width + 0.5) * lena_image_pil.width)
            pixel_y = int(((image_position[1] - y_manim) / image_height + 0.5) * lena_image_pil.height)

            # Retrieve the RGB value from the image at the calculated pixel coordinates
            rgb = lena_image_pil.getpixel((pixel_x, pixel_y))
            rgb_str = f"({rgb[0]}, {rgb[1]}, {rgb[2]})"

            # Animate the dot moving to the current point
            self.play(dot.animate.move_to(point), run_time=2)
            # Update the RGB text with the new values
            self.play(rgb_text.animate.become(Text(rgb_str, font_size=24).next_to(dot, RIGHT)))
            self.wait(1)

        # Fade out the dot and RGB text by shifting them upward and scaling them up
        self.play(FadeOut(dot), FadeOut(rgb_text), shift=UP, scale=2)
        # Animate scaling down the blurred image and grid together over 4 seconds
        self.play(blurred_lena_mobject.animate.scale(0.05), grid_group.animate.scale(0.05), run_time=4)
        self.wait(1)

        # Create separate Text objects for each line explaining bits per pixel
        line1 = Text(
            'Each RGB pixel value (0-255) represents 8 bits per color channel,',
            font_size=24
        )
        line2 = Text(
            'totaling 24 bits per pixel.',
            font_size=24
        )

        # Group the lines vertically with spacing and center them
        paragraph_4_group = VGroup(line1, line2).arrange(
            DOWN,           # Arrange lines vertically
            buff=0.2,        # Spacing between lines
            center=True      # Center the group horizontally
        )

        # Position the group at the top edge of the screen
        paragraph_4_group.to_edge(UP)

        # Scale the text slightly for better fit
        paragraph_4_group.scale(1.1)

        # Animate the paragraph group fading in from below with scaling
        self.play(FadeIn(paragraph_4_group, shift=DOWN, scale=2))
        self.wait(1)
        # Fade out the paragraph group by shifting it upward
        self.play(FadeOut(paragraph_4_group))

        # Draw a white rectangle around the blurred image
        image_frame = SurroundingRectangle(blurred_lena_mobject, color=WHITE, buff=0.1)
        self.play(Create(image_frame), run_time=2)

        # Create a bit string representation and position it over the image
        bits_string = Text("011010110010110101011001000101010100010101110101010111010111", font_size=36)
        bits_string.move_to(blurred_lena_mobject.get_center())  # Center the bit string over the image

        # Transform the rectangle into the bit string, fade out the image and grid
        self.play(ReplacementTransform(image_frame, bits_string), FadeOut(blurred_lena_mobject), FadeOut(grid_group), run_time=2)
        
        # Display a plaintext explanation at the top of the screen
        plaintext_text = Text("This bit string becomes the plaintext to encrypt", font_size=34, color=WHITE)
        plaintext_text.to_edge(UP)
        self.play(FadeIn(plaintext_text))
        self.wait(1)
        # Fade out the plaintext explanation
        self.play(FadeOut(plaintext_text))

        # Define points for the custom right-pointing arrow polygon
        arrow_shape = Polygon(
            [-3, 0.5, 0],  # Top-left
            [0, 0.5, 0],   # Top-right before arrowhead
            [0, 1.0, 0],   # Top-right arrowhead
            [3, 0, 0],     # Arrow point (middle)
            [0, -1.0, 0],  # Bottom-right arrowhead
            [0, -0.5, 0],  # Bottom-right before arrowhead
            [-3, -0.5, 0], # Bottom-left
        ).set_color(WHITE)
       
        # Shift and scale the arrow shape to position it on the left side
        arrow_shape.shift(LEFT * 4.5)
        arrow_shape = arrow_shape.scale(0.4)

        # Create text to put inside the arrow
        binary_text = Text("0101110010100", color=WHITE).scale(0.4)
       
        # Position the text inside the arrow
        binary_text.move_to(arrow_shape.get_center())
       
        # Create the plaintext label and position it above the arrow
        plaintext_label = Text("Plaintext", color=WHITE).scale(0.8)
        plaintext_label.next_to(arrow_shape, UP, buff=0.1)

        # Create the Rijndael Encryptor text and surrounding box
        encryptor_text = Text("Rijndael Encryptor", color=WHITE).scale(1)
        encryptor_box = SurroundingRectangle(encryptor_text, color=WHITE, buff=0.5, fill_color=GRAY, fill_opacity=0.75)

        # Position the encryptor box to the right of the arrow with a slight left shift for alignment
        encryptor_box.next_to(arrow_shape, RIGHT, buff=1)
        encryptor_box.shift(LEFT * 0.5)
        encryptor_text.move_to(encryptor_box.get_center())
        
        # Define points for the custom downward arrow polygon
        arrow_shape_rot_key = Polygon(
            [-0.5, 2, 0],  # Top-left
            [0.5, 2, 0],   # Top-right
            [0.5, 0, 0],   # Bottom-right before arrowhead
            [1.0, 0, 0],   # Right side of arrowhead
            [0, -1, 0],    # Arrow tip (bottom center)
            [-1.0, 0, 0],  # Left side of arrowhead
            [-0.5, 0, 0],  # Bottom-left before arrowhead
        ).set_color(WHITE)

        # Scale and position the downward arrow above the encryptor box
        arrow_shape_rot_key = arrow_shape_rot_key.scale(0.5)
        arrow_shape_rot_key.move_to(encryptor_box, UP)
        arrow_shape_rot_key.shift(UP * 1.8)

        # Create text to put inside the downward arrow (binary string) and rotate it vertically
        binary_text_rot = Text("01010101", color=WHITE).scale(0.4).rotate(PI / 2)
        # Position the binary text inside the downward arrow
        binary_text_rot.move_to(arrow_shape_rot_key.get_center())

        # Create the "Cipher Key" label and position it above the downward arrow
        cipher_key_text = Text("Cipher Key", color=WHITE).scale(0.8)
        cipher_key_text.next_to(arrow_shape_rot_key, UP, buff=0.3)

        # Define points for the second custom downward arrow polygon (counter)
        arrow_shape_rot_counter = Polygon(
            [3, 0.5, 0],    # Top-right
            [0, 0.5, 0],    # Top-left before arrowhead
            [0, 1.0, 0],    # Top-left arrowhead
            [-3, 0, 0],     # Arrow point (middle)
            [0, -1.0, 0],   # Bottom-left arrowhead
            [0, -0.5, 0],   # Bottom-left before arrowhead
            [3, -0.5, 0],   # Bottom-right
        ).set_color(WHITE)

        # Scale and position the second downward arrow to the right side
        arrow_shape_rot_counter = arrow_shape_rot_counter.scale(0.4)
        arrow_shape_rot_counter.shift(RIGHT * 5.5)

        # Create text to put inside the second downward arrow (binary string)
        binary_text_rot_counter = Text("11101010111001", color=WHITE).scale(0.4)
        # Position the binary text inside the second downward arrow
        binary_text_rot_counter.move_to(arrow_shape_rot_counter.get_center())

        # Create the "Counter" label and position it above the second downward arrow
        cunter_text = Text("Counter", color=WHITE).scale(0.8)
        cunter_text.next_to(arrow_shape_rot_counter, UP, buff=0.3)
       
        # Create and position the "AES-CTR mode" text below all elements
        aes_ctr_text = Text("AES-CTR mode", color=WHITE).scale(2)
        aes_ctr_text.shift(DOWN * 2)

        # Animate the creation of the arrows, labels, and encryptor box
        self.play(
            ReplacementTransform(bits_string, arrow_shape),
            FadeIn(plaintext_label),
            FadeIn(binary_text),
            FadeIn(encryptor_text),
            FadeIn(arrow_shape_rot_key),
            FadeIn(encryptor_box),
            FadeIn(cipher_key_text),
            FadeIn(binary_text_rot),
            FadeIn(binary_text_rot_counter),
            FadeIn(cunter_text),
            FadeIn(arrow_shape_rot_counter),
            FadeIn(aes_ctr_text),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.AES_CTR_128_encryption_process()



    def AES_CTR_128_encryption_process(self):
        encryption_process = Text('We will go through the AES-CTR 128 encryption algorithm').scale(0.7)
        self.play(FadeIn(encryption_process, shift=UP, scale=0.66))
        self.wait(1)
        self.play(FadeOut(encryption_process, shift=UP, scale=2))

        # Define the hexadecimal and binary values for two rows (8 cells per row)
        hex_row_top = ["32", "43", "f6", "a8", "88", "5a", "30", "8d"]
        binary_row_top = ["0011 0010", "0100 0011", "1111 0110", "1010 1000", 
                          "1000 1000", "0101 1010", "0011 0000", "1000 1101"]

        hex_row_bottom = ["31", "31", "98", "a2", "e0", "37", "07", "34"]
        binary_row_bottom = ["0011 0001", "0011 0001", "1001 1000", "1010 0010", 
                             "1110 0000", "0011 0111", "0000 0111", "0011 0100"]

        # Create two tables, one for the top row and one for the bottom row
        table_top = Table(
            [binary_row_top, hex_row_top],
            include_outer_lines=True,
        )

        table_bottom = Table(
            [binary_row_bottom, hex_row_bottom],
            include_outer_lines=True,
        )

        # Scale the tables down to fit smaller text
        table_top.scale(0.4)
        table_bottom.scale(0.4)

        # Position the bottom table below the top table
        table_bottom.next_to(table_top, DOWN)
        
        # Add the table to the scene
        self.play(FadeIn(table_top), FadeIn(table_bottom))

        # Add an explanation text about the cipher key
        explanation_text = Text(
            "This table represents the cipher key used in AES-CTR 128."
        ).scale(0.6).next_to(table_top, UP)

        self.play(FadeIn(explanation_text))
        self.wait(1)

        # Define each line of the explanation separately for better alignment
        line1 = Text("A cipher key is used to encrypt data.", font_size=30)
        line2 = Text("Each 4-bit binary value", font_size=30)
        line3 = Text("can be represented as a hexadecimal number.", font_size=30)

        # Group the lines vertically with spacing and center them
        paragraph_group = VGroup(line1, line2, line3).arrange(
            DOWN,  # Arrange lines vertically
            center=True,  # Center the group horizontally
            buff=0.3  # Space between lines
        )

        # Position the paragraph group relative to the table
        paragraph_group.next_to(table_bottom, DOWN)

        # Animate the paragraph group fading in
        self.play(FadeIn(paragraph_group, shift=DOWN, scale=0.5))
        self.wait(2)

        # Fade out the paragraph group afterward
        self.play(FadeOut(paragraph_group, shift=UP, scale=2),FadeOut(explanation_text, shift=UP, scale=2))

        # Display the table and wait
        self.wait(1)

        array_to_matrix = Text("We can convert the array into a 4X4 matrix.").scale(0.5)
        self.play(table_top.animate.shift(UP*3), table_bottom.animate.shift(UP*3))
        self.wait(1)
        self.play(FadeIn(array_to_matrix))
        self.play(FadeOut(array_to_matrix))

        # Create a matrix using Manim's Matrix class
        matrix = Matrix([
            [f"{0x32:02X}", f"{0x88:02X}", f"{0x31:02X}", f"{0xE0:02X}"],
            [f"{0x43:02X}", f"{0x5A:02X}", f"{0x98:02X}", f"{0x37:02X}"],
            [f"{0xF3:02X}", f"{0x30:02X}", f"{0xA2:02X}", f"{0x07:02X}"],
            [f"{0xA8:02X}", f"{0x8D:02X}", f"{0xA2:02X}", f"{0x34:02X}"]
        ])

        # Add the matrix to the scene
        self.play(ReplacementTransform(table_top,matrix),FadeOut(table_bottom))
        self.wait()

     