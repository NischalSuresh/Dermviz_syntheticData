import cv2
import os

back_image_dir = '/Users/ngandige/Documents/Veytel/Dermviz/Synthetic_data/full_back_images'
crop_save_path = '/Users/ngandige/Documents/Veytel/Dermviz/Synthetic_data/crops/'
files = os.listdir(back_image_dir)
files = [file for file in files if not file.startswith('.DS_Store')]

def draw_square(event, x, y, flags, param):
    global ix, iy, drawing, crop_count
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        w = abs(x - ix)
        h = abs(y - iy)
        side = max(w, h)
        x2, y2 = ix + side, iy + side
        crop_img = img[min(iy, y):min(iy, y) + side, min(ix, x):min(ix, x) + side]
        crop_file_name = file + f'_crop_{crop_count}.jpg'
        cv2.imwrite(crop_save_path + crop_file_name, crop_img)
        cv2.rectangle(img, (ix, iy), (x2, y2), (0, 255, 0), 2)
        # add text next to rectangle indicating crop number
        cv2.putText(img, f'{crop_count}', (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
        crop_count += 1    
        

for i in range(49,len(files)):
    file = files[i]
    print(file)
    drawing = False
    ix, iy = -1, -1
    crop_count = 0
    image_path = os.path.join(back_image_dir, file)
    img = cv2.imread(image_path)
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', draw_square)
    while True:
        key = cv2.waitKey(1)
        if key == 27: 
            break
    cv2.destroyAllWindows()
    cv2.imwrite('/Users/ngandige/Documents/Veytel/Dermviz/Synthetic_data/backs_processed' + f'/processed_{file}', img)