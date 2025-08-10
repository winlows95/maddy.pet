import re

def invert_color(hex_color):
    # Remove the '#' symbol
    hex_color = hex_color.lstrip('#')

    # If short form (e.g. 'abc'), expand it to 'aabbcc'
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])

    # Convert hex to integer RGB values
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Invert each channel
    r_inv = 255 - r
    g_inv = 255 - g
    b_inv = 255 - b

    # Format back to hex string
    return f'#{r_inv:02x}{g_inv:02x}{b_inv:02x}'

def invert_css_colors(css_content):
    # Regex to find hex color codes (#RGB or #RRGGBB)
    hex_color_pattern = re.compile(r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})')

    # Replace each color with its inverted version
    inverted_css = hex_color_pattern.sub(lambda match: invert_color(match.group(0)), css_content)
    return inverted_css

if __name__ == '__main__':
    input_file = 'css/tacit-css.css'
    output_file = 'css/tacit-cssINVERT.css'

    with open(input_file, 'r') as f:
        css_content = f.read()

    inverted_css = invert_css_colors(css_content)

    with open(output_file, 'w') as f:
        f.write(inverted_css)

    print(f"Inverted colors written to {output_file}")
