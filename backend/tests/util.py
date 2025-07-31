def checkPixels(image, expected_color):
    width, height, channels = image.shape
    for x in range(width):
        for y in range(height):
            for c in range(channels):
                if image[x][y][c] != expected_color[c]:
                    return False
    return True

def checkAlphaPixels(image, ref_image,alpha):
    width, height, channels = image.shape
    for x in range(width):
        for y in range(height):
            for c in range(channels):
                if image[x][y][c] != ref_image[x][y][c]* alpha:
                    print(image[x][y][c])
                    print(ref_image[x][y][c]* alpha)
                    print(f"X{x} y{y} c{c}")
                    return False
    return True