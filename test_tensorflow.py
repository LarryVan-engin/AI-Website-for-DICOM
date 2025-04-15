import cv2
import os

# Đường dẫn đến tệp ảnh
image_path = 'label/test.jpg'

# Kiểm tra tệp ảnh
if not os.path.exists(image_path):
    print(f"Tệp ảnh không tồn tại: {image_path}")
else:
    # Đọc ảnh
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Không thể đọc được ảnh. Hãy kiểm tra định dạng hoặc tệp ảnh.")
    else:
        # Thay đổi kích thước ảnh
        image_resized = cv2.resize(image, (128, 128))
        print("Ảnh đã được thay đổi kích thước thành công.")


#import dataset của kaggle
import kagglehub

# Download latest version
path = kagglehub.dataset_download("kmader/siim-medical-images")

print("Path to dataset files:", path)