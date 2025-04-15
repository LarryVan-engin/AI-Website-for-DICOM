import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import glob

#matplotlib inline

labels_df = pd.read_csv('train/CT_hermorrhage/labels.csv')
labels = np.array(labels_df[' hemorrhage'].tolist())

files = sorted(glob.glob('train/CT_hermorrhage/head_ct/head_ct/*.png'))
print(f"Số lượng tệp ảnh: {len(files)}")
