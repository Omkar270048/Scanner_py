import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local
from transform import perspective_transform


def load_and_resize_image(image_path, height=500):
    """Load an image and resize it for processing."""
    original_img = cv2.imread(image_path)
    copy = original_img.copy()
    ratio = original_img.shape[0] / float(height)
    img_resize = imutils.resize(original_img, height=height)
    return img_resize, copy, ratio


def preprocess_image(img_resize):
    """Convert image to grayscale, blur, and detect edges."""
    gray_image = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edged_img = cv2.Canny(blurred_image, 75, 200)
    return edged_img


def find_document_contour(edged_img):
    """Find the contour of the document in the image."""
    cnts, _ = cv2.findContours(edged_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            return approx
    return None


def apply_perspective_transform(copy, doc_points, ratio):
    """Apply perspective transform to the image based on document points."""
    doc_points = np.array(doc_points).reshape(4, 2) * ratio
    warped_image = perspective_transform(copy, doc_points)
    return cv2.cvtColor(warped_image, cv2.COLOR_BGR2GRAY)


def threshold_image(warped_image):
    """Apply local thresholding to the warped image."""
    T = threshold_local(warped_image, 11, offset=10, method="gaussian")
    return (warped_image > T).astype("uint8") * 255


def save_and_display_image(image, output_path):
    """Save the image to disk and display it."""
    cv2.imwrite(output_path, image)
    cv2.imshow("Final Scanned image", imutils.resize(image, height=650))
    cv2.waitKey(0)


def main(image_path, output_path='./scan.png'):
    """Main function to run the document scanning process."""
    img_resize, copy, ratio = load_and_resize_image(image_path)
    edged_img = preprocess_image(img_resize)
    doc = find_document_contour(edged_img)

    if doc is not None:
        doc_points = [tuple(d[0]) for d in doc]
        warped_image = apply_perspective_transform(copy, doc_points, ratio)
        thresholded_image = threshold_image(warped_image)
        save_and_display_image(thresholded_image, output_path)
    else:
        print("No document contour found.")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Document Scanner')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--output_path', type=str, default='./scan.png', help='Path to save the output image')
    args = parser.parse_args()

    main(args.image_path, args.output_path)
