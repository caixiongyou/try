# import matplotlib.pyplot as plt
# import numpy as np
#
# # 数据准备
# conv_layers = np.arange(2, 55, 2)  # 卷积层索引 2-54，步长2
# pruning_before = np.linspace(0, 60, len(conv_layers))  # 剪枝前数据
# pruning_after = np.linspace(60, 0, len(conv_layers))   # 剪枝后数据
#
# # 绘图设置
# plt.figure(figsize=(15, 6), dpi=100)
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
# plt.rcParams['axes.unicode_minus'] = False
#
# bar_width = 0.35
# x = np.arange(len(conv_layers))
#
# # 黑白配色方案
# colors = ['#333333', '#888888']  # 深灰 & 浅灰
# patterns = ['////', '....']       # 斜线 & 点状填充
#
# # 绘制柱状图
# bars_before = plt.bar(x - bar_width/2, pruning_before, bar_width,
#                      label='剪枝前',
#                      color=colors[0],
#                      edgecolor='black',
#                      hatch=patterns[0])
#
# bars_after = plt.bar(x + bar_width/2, pruning_after, bar_width,
#                     label='剪枝后',
#                     color=colors[1],
#                     edgecolor='black',
#                     hatch=patterns[1])
#
# # 坐标轴和标题
# plt.xlabel('卷积层索引', fontsize=12, color='black')
# plt.ylabel('数值 (%)', fontsize=12, color='black')
# plt.title('剪枝前后对比（黑白版）', fontsize=14, pad=20, color='black')
# plt.xticks(x, conv_layers, rotation=45)
# plt.yticks(np.arange(0, 61, 10))
#
# # 数据标签样式调整
# for bar in bars_before + bars_after:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2., height,
#              f'{int(height)}',
#              ha='center', va='bottom',
#              color='black',  # 标签文字保持黑色
#              fontsize=8)
#
# # 图例和网格
# plt.legend(frameon=True, facecolor='white')
# plt.grid(axis='y', color='#CCCCCC', linestyle='--', linewidth=0.5)
#
# # 边框调整
# for spine in plt.gca().spines.values():
#     spine.set_color('black')
#
# plt.tight_layout()
# plt.savefig('bw_pruning_comparison.png', bbox_inches='tight')
# plt.show()

import cv2

p1 = cv2.imread(r'E:\jang\Documents\p1.JPG')
p2 = cv2.imread(r'E:\jang\Documents\p2.JPG')
p3 = cv2.imread(r'E:\jang\Documents\p3.JPG')
debugg_a = 0