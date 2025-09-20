# # # This is a sample Python script.
# #
# # # Press Shift+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # import cv2
# # import socket
# # sever = socket.socket()
# # server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建socket对象
# # ser=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建socket对象
# # server.bind(("",8888))
# # filePath = r"D:\yolov5\data\output_video.avi"
# # camera = cv2.VideoCapture(filePath)
# # re = server.recvfrom(2048)
# # while True:
# #     ret,frame = camera.read()
# #     if not ret:
# #         break
# #     frame = cv2.resize(frame,(1000,700))
# #     data = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 15])[1]
# #     ser.sendto(data,(re[1][0],9999))
# # server.close()
# # ser.close()
#
#
# # def fibonacci(month):
# #     if month == 2 or month == 1:
# #         return 1
# #     else:
# #         return fibonacci(month-1) + fibonacci(month-2)
# # # 测试经过12个月份后的兔子对数
# # result = fibonacci(13)
# # print(result)
# # print("pth080")
#
#
# # # 使用 OpenCV 导入 cv2 的水印图像
# # import cv2
# # # 导入我们将要使用的logo
# # logo = cv2.imread("C:/Users/jang/Desktop/789.JPG")
# # # 导入我们要应用水印的图像
# # img = cv2.imread("C:/Users/jang/Desktop/123.PNG")
# # # cv2.resize调整图像的尺寸
# # img = cv2.resize(img, (640, 360), interpolation=cv2.INTER_LINEAR)
# # logo = cv2.resize(logo, (120, 120), interpolation=cv2.INTER_LINEAR)
# # # 计算logo的尺寸高度和宽度;其中_表示占位符,说明不需要用到这个参数
# # h_logo, w_logo, _ = logo.shape
# # # 图像的高度和宽度
# # h_img, w_img, _ = img.shape
# # # 计算中心计算中心的坐标，我们将在其中放置水印
# # center_y = int(h_img/2)
# # center_x = int(w_img/2)
# # # 从上、下、右、左计算
# # top_y = 0  # logo的上边界坐标
# # left_x = w_img - w_logo  # logo的左边界坐标
# # # top_y = center_y - int(h_logo/2)  # logo的上边界坐标
# # # left_x = center_x - int(w_logo/2)  # logo的左边界坐标
# # bottom_y = top_y + h_logo  # logo的下边界坐标
# # right_x = left_x + w_logo  # logo的右边界坐标
# # # 给图片添加水印
# # # destination相当于logo(水印)要放在图像上的位置区域
# # # destination = img[top_y:bottom_y, left_x:right_x]
# # # 基于cv2.addWeighted()进行图像融合操作,logo权重为1
# # # result = cv2.addWeighted(destination, 0, logo, 1, 0)
# # for row in range(h_logo):
# #     for col in range(w_logo):
# #         b, g, r = logo[row][col]
# #         if not (b <= 200 and g <= 200 and r <= 200):
# #             img[top_y + row][left_x + col] = (b, g, r)
# # # 显示和保存图像
# # # result相当于水印区域的值,赋给img的水印区域即可
# # # img[top_y:bottom_y, left_x:right_x] = result
# # # cv2.imwrite()表示保存图片
# # cv2.putText(img, "pth080", (320, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# # cv2.imwrite("C:/Users/jang/Desktop/watermarked.jpg", img)
# # cv2.imshow("Watermarked Image", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# """
# 六图连结
# """
# import cv2
# import numpy as np
#
#
# def hebing_horizontal(img1, img2):
#     # 获取两张图片的宽度和高度
#     h1, w1 = img1.shape[:2]
#     h2, w2 = img2.shape[:2]
#
#     if h1 > h2:
#         w2 = int(h1 * w2 / h2)
#         img2 = cv2.resize(img2, (w2, h1))
#     else:
#         w1 = int(h2 * w1 / h1)
#         img1 = cv2.resize(img1, (w1, h2))
#
#     # 创建一个新的空白图片，宽度为两张图片的宽度之和，高度为两张图片中高度最大值
#     new_img = np.zeros((max(h1, h2), w1 + w2, 3), dtype=np.uint8)
#     # 将第一张图片复制到新图片的左侧
#     new_img[:max(h1, h2), :w1] = img1
#     # 将第二张图片复制到新图片的右侧
#     new_img[:max(h1, h2), w1:w1 + w2] = img2
#     return new_img
#
#
# def hebing_vertical(img1, img2):
#     # 获取两张图片的宽度和高度
#     h1, w1 = img1.shape[:2]
#     h2, w2 = img2.shape[:2]
#
#     if w1 > w2:
#         h2 = int(w1 * h2 / w2)
#         img2 = cv2.resize(img2, (w1, h2))
#     else:
#         h1 = int(w2 * h1 / w1)
#         img1 = cv2.resize(img1, (w2, h1))
#
#     # 创建一个新的空白图片，宽度为两张图片中宽度最大值，高度为两张图片的高度之和
#     new_img = np.zeros((h1 + h2, max(w1, w2), 3), dtype=np.uint8)
#     # 将第一张图片复制到新图片的上方
#     new_img[:h1, :max(w1, w2)] = img1
#     # 将第二张图片复制到新图片的下方
#     new_img[h1:h1 + h2, :max(w1, w2)] = img2
#     return new_img
#
#
# # 读取两张图片
# img1 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u1.PNG')
# img2 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u2.PNG')
# img3 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u3.PNG')
# img4 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u4.PNG')
# img5 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u5.PNG')
# img6 = cv2.imread(r'C:\Users\jang\Desktop\uno_pic\u6.PNG')
# img12 = hebing_horizontal(img1, img2)  # 水平连结1、2
# img34 = hebing_horizontal(img3, img4)  # 水平连结1、2、3
# img56 = hebing_horizontal(img5, img6)  # 水平连结4、5
# img1234 = hebing_vertical(img12, img34)  # 水平连结4、5、6
# new_img = hebing_vertical(img1234, img56)  # 将两组水平连结的结果进行垂直连结
# # 显示连结后的图片
# # new_img = cv2.resize(new_img, (int(new_img.shape[1] * 0.75), int(new_img.shape[0] * 0.75)))
# cv2.imshow('SixPicture Concatenation', new_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#

import cv2

# 读取图像
logo = cv2.imread('789.JPG')
img = cv2.imread("123.PNG")

# 调整图像大小
img = cv2.resize(img, (640, 360), interpolation=cv2.INTER_LINEAR)
logo = cv2.resize(logo, (120, 120), interpolation=cv2.INTER_LINEAR)

h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

top_y = 0
left_x = w_img - w_logo

bottom_y = top_y + h_logo
right_x = left_x + w_logo



for row in range(h_logo):
    for col in range(w_logo):
        b, g, r = logo[row][col]
        if not (b <= 200 and g <= 200 and r <= 200):
            img[top_y + row][left_x + col] = (b, g, r)



# 添加文本
text = "wcw327"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # 红色
thickness = 2

# 计算文本的中心位置
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_width, text_height = text_size
center_x = (w_img - text_width) // 2
center_y = (h_img + text_height) // 2

# 添加文本到图像
cv2.putText(img, text, (center_x, center_y), font, font_scale, font_color, thickness)

# 保存和显示图像
cv2.imwrite("D:/pythonzl/aaa/LL.JPG", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()