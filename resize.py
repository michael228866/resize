from PIL import Image
import os

# 要修改的圖片所在的資料夾路徑
folder_path = "./character1"
# 要修改的圖片的大小
new_size = (28, 28)
for i in range(1,20):
    #資料夾名1~20
    folder_path = "./character"+str(i)
    # 讀取資料夾中的圖片文件
    for file in os.listdir(folder_path):
        # 如果文件是圖片文件
        if file.endswith(".jpg") or file.endswith(".png"):
            # 打開圖片文件
            image = Image.open(os.path.join(folder_path, file))
            # 修改圖片大小
            image = image.resize(new_size)
            # 保存圖片
            image.save(os.path.join(folder_path, file))
