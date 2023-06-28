def rgba_to_hex(rgba):
    r, g, b, a = rgba
    r_hex = int(r * 255)
    g_hex = int(g * 255)
    b_hex = int(b * 255)
    a_hex = int(a * 255)
    hex_code = "#{:02x}{:02x}{:02x}{:02x}".format(r_hex, g_hex, b_hex, a_hex)
    return hex_code

# Read RGBA values from file
rgba_list = []
with open("input.txt", "r") as file:
    for line in file:
        rgba = tuple(map(float, line.strip().split(',')))
        rgba_list.append(rgba)

# Convert RGBA values to hexadecimal
hex_codes = []
for rgba in rgba_list:
    hex_code = rgba_to_hex(rgba)
    hex_codes.append(hex_code)

# Write hexadecimal codes to file
with open("output.txt", "w") as file:
    for hex_code in hex_codes:
        file.write(hex_code + "\n")
