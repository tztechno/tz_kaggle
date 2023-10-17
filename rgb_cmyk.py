def rgb_to_cmyk(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    # Find the maximum value among the normalized RGB components
    max_value = max(r_normalized, g_normalized, b_normalized)

    # Calculate the Key (black) component
    k = 1.0 - max_value

    # Avoid division by zero
    if k == 1.0:
        c = m = y = 0.0
    else:
        # Calculate the Cyan, Magenta, and Yellow components
        c = (1.0 - r_normalized - k) / (1.0 - k)
        m = (1.0 - g_normalized - k) / (1.0 - k)
        y = (1.0 - b_normalized - k) / (1.0 - k)

    return c, m, y, k

# Example usage
r = 255
g = 0
b = 0
cmyk = rgb_to_cmyk(r, g, b)
print("CMYK:", cmyk)
