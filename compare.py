import cv2
import numpy as np

# Load images
img1 = cv2.imread('I1B1.png')
img2 = cv2.imread('I2B1.png')

# Check if images loaded
if img1 is None or img2 is None:
    print("Error: Could not load images")
    exit()

# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# -------- ALIGNMENT START (ECC) --------
def preprocess_for_alignment(img):
    return cv2.GaussianBlur(img, (5, 5), 0)

def align_images_ecc(gray_ref, gray_target, color_target):
    # Resize target to match reference dimensions first
    h, w = gray_ref.shape
    gray_target_resized = cv2.resize(gray_target, (w, h))
    color_target_resized = cv2.resize(color_target, (w, h))

    # Preprocess for alignment only
    ref_pre = preprocess_for_alignment(gray_ref)
    tgt_pre = preprocess_for_alignment(gray_target_resized)

    # Float32 needed by ECC
    ref_f = ref_pre.astype(np.float32)
    tgt_f = tgt_pre.astype(np.float32)

    warp_matrix = np.eye(2, 3, dtype=np.float32)
    criteria = (
        cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
        1000,
        1e-6
    )

    try:
        _, warp_matrix = cv2.findTransformECC(
            ref_f, tgt_f,
            warp_matrix, cv2.MOTION_EUCLIDEAN, criteria
        )
        aligned_color = cv2.warpAffine(
            color_target_resized, warp_matrix, (w, h),
            flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP
        )
        print("ECC alignment successful")
        return aligned_color

    except cv2.error as e:
        print(f"ECC failed: {e} — using resized only")
        return color_target_resized

aligned_img2 = align_images_ecc(gray1, gray2, img2)

# Update gray2 from aligned color image
gray2 = cv2.cvtColor(aligned_img2, cv2.COLOR_BGR2GRAY)
# -------- ALIGNMENT END --------

# Overlay to check alignment quality
overlay = cv2.addWeighted(gray1, 0.5, gray2, 0.5, 0)
cv2.imshow("Overlay (check ghosting here)", overlay)

# Compute difference
diff = cv2.absdiff(gray1, gray2)

# Threshold
_, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)

# Noise cleaning
kernel = np.ones((3, 3), np.uint8)
clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours
contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes — uncomment the area filter once alignment is confirmed working
output = img1.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:  # filtering small noise — tune this number
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Show results
cv2.imshow("Original 1", img1)
cv2.imshow("Original 2", img2)
cv2.imshow("Difference", diff)
cv2.imshow("Threshold", thresh)
cv2.imshow("Cleaned", clean)
cv2.imshow("Final Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()