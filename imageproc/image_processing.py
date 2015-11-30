import pygame as pg

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel
def grayPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    ave_intensity = (red_intensity + green_intensity+ blue_intensity)//3
    return (ave_intensity, ave_intensity, ave_intensity)

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel
def channel(pixel,chan):
    return (pixel[chan],pixel[chan],pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])


# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity
def intensify(pixel,quantity):
    return (pixel[0]+quantity, pixel[1]+quantity, pixel[2]+quantity)

def lighten(pixel):
    if pixel[0] <= 245:
        pixel[0] = pixel[0] + 10
    else:
        pixel[0] = 255
    if pixel[1] <= 245:
        pixel[1] = pixel[1] + 10
    else:
        pixel[1] = 255
    if pixel[2] <= 245:
        pixel[2] = pixel[2] + 10
    else:
        pixel[2] = 255
    return (pixel[0], pixel[1], pixel[2])

def darken(pixel):
    if pixel[0] >= 10:
        pixel[0] = pixel[0] - 10
    else:
        pixel[0] = 0
    if pixel[1] >= 10:
        pixel[1] = pixel[1] - 10
    else:
        pixel[1] = 0
    if pixel[2] >= 10:
        pixel[2] = pixel[2] - 10
    else:
        pixel[2] = 0
    return (pixel[0], pixel[1], pixel[2])
def invert(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = inverse(pixels3d[x,y])
def bw(image_surf):
        # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = grayPixel(pixels3d[x,y])

def light(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = lighten(pixels3d[x,y])

def dark(image_surf):
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = darken(pixels3d[x,y])
