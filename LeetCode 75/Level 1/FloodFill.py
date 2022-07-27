'''Instructions
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
'''
'''Examples
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
'''
'''Thoughts
1. If the newcolor is equal to the color at sr sc return the original image
2. Change color at sr sc and recursion on near by pints
'''

def flood_fill(image, sr, sc, newColor):
    change_color = image[sr][sc]
    if change_color == newColor:
        return image
    length = len(image[0])
    width = len(image)
    def change(y, x):
        if image[y][x] == change_color:
            image[y][x] = newColor
            if y + 1 < width:
                change(y+1, x)
            if y - 1 >= 0:
                change(y-1, x)
            if x + 1 < length:
                change(y, x+1)
            if x - 1 >= 0:
                change(y, x-1)
    change(sr,sc)
    return image