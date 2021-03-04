import cv2
import numpy as np
import pytesseract
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Sachithra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
	text = pytesseract.image_to_string(img)
	return text

img = cv2.imread('job1.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)


# get grayscale image
def get_grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
	return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
	kernel = np.ones((5, 5), np.uint8)
	return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
	kernel = np.ones((5, 5), np.uint8)
	return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
	kernel = np.ones((5, 5), np.uint8)
	return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
	return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
	coords = np.column_stack(np.where(image > 0))
	angle = cv2.minAreaRect(coords)[-1]
	if angle < -45:
		angle = -(90 + angle)

	else:
		angle = -angle
	(h, w) = image.shape[:2]
	center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
	return rotated


# template matching
def match_template(image, template):
	return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

image = cv2.imread('job1.jpg')

gray = get_grayscale(image)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

print(ocr_core(img))
