import numpy as np
import cv2

def order_points(pts):
    # Initialize the list of coordinates to be ordered
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)

    # Top-left point will have the smallest sum
    rect[0] = pts[np.argmin(s)]

    # Bottom-right point will have the largest sum
    rect[2] = pts[np.argmax(s)]

    # Compute the difference between the points
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # Return ordered coordinates
    return rect

def perspective_transform(image, pts):
    # Unpack the ordered coordinates individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Compute the width and height of the new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # Construct the set of destination points
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # Compute the perspective transform matrix
    transform_matrix = cv2.getPerspectiveTransform(rect, dst)

    # Apply the transform matrix
    warped = cv2.warpPerspective(image, transform_matrix, (maxWidth, maxHeight))

    return warped
