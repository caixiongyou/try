import os  # 用于处理文件和目录路径
import cv2  # OpenCV库，用于图像处理
import numpy as np  # 用于处理数据
import tqdm  # 用于显示进度条


def visual_bbox_results(seq_class, seq_name, initial_text_results_dir):
    """
    函数用于在图像上绘制边界框并保存结果。
    :param seq_class: 序列类别
    :param seq_name: 序列名称
    :param initial_text_results_dir: 初始文本结果目录,(即"我们的方法“跟踪结果txt文件路径)
    """
    # 我们的方法 跟踪结果txt文件路径, 路径由函数传入
    ours_path = os.path.join(initial_text_results_dir, "%s.txt" % seq_name)
    print(ours_path)  # 打印路径，用于调试
    ours_results = np.loadtxt(ours_path, delimiter='\t')  # 读取跟踪结果;delimiter(可选):用于分隔值的字符,默认为任意连续的空格.
    # 调整边界框坐标格式，使其适合绘制
    ours_results[:, 2] = ours_results[:, 2] + ours_results[:, 0]
    ours_results[:, 3] = ours_results[:, 3] + ours_results[:, 1]

    # tracker1 跟踪结果txt文件路径
    tracker1_path = "/path/results/lasot/%s.txt" % seq_name  # 这里的/path可能要替换为数据存放在PC上的路径,后面也是同样道理。%s代表格式化,相当于用seq_name填充到路径里面的相应位置
    print(tracker1_path)  # 打印路径，用于调试
    tracker1_results = np.loadtxt(tracker1_path, delimiter='\t')  # 读取跟踪结果;delimiter(可选):用于分隔值的字符,默认为任意连续的空格.
    # 调整边界框坐标格式，使其适合绘制
    tracker1_results[:, 2] = tracker1_results[:, 2] + tracker1_results[:, 0]
    tracker1_results[:, 3] = tracker1_results[:, 3] + tracker1_results[:, 1]

    # groundtruth.txt文件路径
    gt_path = "/path/LaSOT/data/%s/%s/groundtruth.txt" % (seq_class, seq_name)
    print(gt_path)  # 打印路径，用于调试
    gt_data = np.loadtxt(gt_path, delimiter=',')  # 读取真实标注数据;delimiter(可选):用于分隔值的字符,这里为','号.
    # 调整边界框坐标格式，使其适合绘制
    gt_data[:, 2] = gt_data[:, 2] + gt_data[:, 0]
    gt_data[:, 3] = gt_data[:, 3] + gt_data[:, 1]

    # 图像文件夹路径
    ds_dir = "/path/LaSOT/data/%s/%s/img" % (seq_class, seq_name)

    # 可视化结果保存路径
    save_dir = "/path/%s" % (seq_name)
    img_list = os.listdir(ds_dir)  # 获取图像列表
    img_list.sort()  # 对图像列表进行排序
    # "/path/LaSOT/data/%s/%s/groundtruth.txt" % (seq_class, seq_name)的数据与"/path/LaSOT/data/%s/%s/img" % (seq_class, seq_name)一一对应
    for index in range(gt_data.shape[0]):  # 遍历每一帧图像
        img_load_path = os.path.join(ds_dir, img_list[index])  # 获取图像加载路径
        img_save_path = os.path.join(save_dir, img_list[index])  # 获取图像保存路径

        img_item = cv2.imread(img_load_path)  # 读取图像

        # 在图像上绘制真实标注的边界框，颜色为绿色
        cv2.rectangle(img_item,
                      (int(gt_data[index, 0]), int(gt_data[index, 1])),
                      (int(gt_data[index, 2]), int(gt_data[index, 3])),
                      color=(0, 255, 0), thickness=3)

        # 在图像上绘制我们方法的边界框，颜色为红色
        cv2.rectangle(img_item,
                      (int(ours_results[index, 0]), int(ours_results[index, 1])),
                      (int(ours_results[index, 2]), int(ours_results[index, 3])),
                      color=(0, 0, 255), thickness=3)

        # 在图像上绘制tracker1的边界框，颜色为黄色
        cv2.rectangle(img_item,
                      (int(tracker1_results[index, 0]), int(tracker1_results[index, 1])),
                      (int(tracker1_results[index, 2]), int(tracker1_results[index, 3])),
                      color=(0, 255, 255), thickness=3)

        print(img_save_path)  # 打印保存路径，用于调试
        if not os.path.exists(save_dir):  # 检查保存目录是否存在
            os.makedirs(save_dir)  # 如果不存在，则创建目录

        cv2.imwrite(img_save_path, img_item)  # 保存绘制了边界框的图像


# 我们的方法 跟踪结果txt文件夹的路径
ds_dir = "/path/results/lasot"   # 这里的ds_dir与上面的名字相同,含义不同
ds_list = os.listdir(ds_dir)  # 获取目录下所有文件
txt_files = [file for file in ds_list if file.endswith(".txt")]  # 筛选出txt文件
txt_files.sort()  # 对文件名进行排序

for ds_item in tqdm.tqdm(txt_files):  # 使用tqdm显示进度条
    if "_time" in ds_item:  # 如果文件名包含_time，则跳过
        continue
    seq_name = ds_item[:-4]  # 从文件名中提取序列名称

    seq_class = seq_name.split("-")[0]  # 从序列名称中提取序列类别
    print(seq_class, seq_name)  # 打印序列类别和名称
    visual_bbox_results(seq_class, seq_name, ds_dir)  # 调用函数进行可视化