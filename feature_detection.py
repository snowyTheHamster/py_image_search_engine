import cv2
import os
import csv

TARGET_FILE = '05.png'
IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'
IMG_SIZE = (200, 200)

target_img_path = IMG_DIR + TARGET_FILE
target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)
target_img = cv2.resize(target_img, IMG_SIZE)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)
# detector = cv2.ORB_create()
detector = cv2.AKAZE_create()
(target_kp, target_des) = detector.detectAndCompute(target_img, None)

print('TARGET_FILE: {TARGET_FILE}')

with open('feat_results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    files = os.listdir(IMG_DIR)
    for file in files:
        if file == '.DS_Store' or file == TARGET_FILE:
            continue

        comparing_img_path = IMG_DIR + file
        try:
            comparing_img = cv2.imread(comparing_img_path, cv2.IMREAD_GRAYSCALE)
            comparing_img = cv2.resize(comparing_img, IMG_SIZE)
            (comparing_kp, comparing_des) = detector.detectAndCompute(comparing_img, None)
            matches = bf.match(target_des, comparing_des)
            dist = [m.distance for m in matches]
            ret = sum(dist) / len(dist)
        except cv2.error:
            ret = 100000

        print(file, ret)
        csvwriter.writerow([f'{file}', f'{ret}'])
        
    print('lower value is closer')