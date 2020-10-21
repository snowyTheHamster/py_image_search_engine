import cv2
import os
import csv
import PySimpleGUI as sg

layout = [
    [sg.Text('Use reference Image to search for similar Images in folder.')],
    [sg.Text('1. Select reference image')],
    [sg.Text('2. Select folder with images')],
    [sg.Text('3. Choose Search Algorithm')],
    [sg.Text('4. Click "Search"')],
    [sg.Text('5. Results available below and exported to results.csv file')],
    [sg.Text('')],
    [sg.Text('Reference Image:')],
    [sg.Input(key='_REF_IMG_'), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Text('Select folder with images to search:')],
    [sg.Input(key='_IMGS_'), sg.FolderBrowse()],
    [sg.Text('')],
    [sg.Text('SEARCH METHOD', font=(22))],
    [sg.Radio('Histogram', "_RADIO_FILESIZE_", default=True, key='Radio_filesize_1'), sg.Radio('AKAZE', "_RADIO_FILESIZE_", key='Radio_filesize_2', disabled=True), sg.Radio('ORB', "_RADIO_FILESIZE_", key='Radio_filesize_3', disabled=True)],
    [sg.Button("Search", size=(10, 1), bind_return_key=True, key='_SEARCH_')],
    [sg.Output(size=(70,30))],
]

window = sg.Window('Image Search Engine', layout, element_justification='left')

ignore_files = [
    '.DS_Store',
    '.gitkeep',
]

while True:
    event, values = window.read()
    if event is None:
        break
    if event == '_SEARCH_':

        TARGET_FILE_FULL_PATH = values['_REF_IMG_']
        TARGET_FILE = TARGET_FILE_FULL_PATH.split('/')[-1]
        IMG_DIR = values['_IMGS_']
        IMG_SIZE = (200, 200)

        target_img_path = os.path.join(IMG_DIR, TARGET_FILE)
        target_img = cv2.imread(target_img_path)
        target_img = cv2.resize(target_img, IMG_SIZE)
        target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])

        print(f'TARGET_FILE: {TARGET_FILE_FULL_PATH} \n')
        files = os.listdir(IMG_DIR)

        with open('results.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for file in files:
                if file in ignore_files or file == TARGET_FILE:
                    continue

                comparing_img_path = os.path.join(IMG_DIR, file)
                comparing_img = cv2.imread(comparing_img_path)
                comparing_img = cv2.resize(comparing_img, IMG_SIZE)
                comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])

                ret = cv2.compareHist(target_hist, comparing_hist, 0)
                print(file, ret)
                csvwriter.writerow([f'{file}', f'{ret}'])
                
            print('Histogram: higher value means images are similar to reference image \n')
            print('result saved to results.csv')