import matplotlib.animation as ani
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
mpl.rcParams['font.size'] = 12  # 字体大小
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# 抛硬币实验一

m = 20  # 实验次数

n = (5, 50, 500, 1000, 5000)  # 每次抛硬币次数
fig, axlist = plt.subplots(3, 3, figsize=(6, 6), dpi=100)
fig.suptitle('模拟抛硬币', fontsize=10, y=0.95)
for index, value in enumerate(n):
    result = np.random.choice(2, (m, value))
    feq = result.mean(axis=1)
    ax = axlist[np.unravel_index(index, axlist.shape)]
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    ax.set_ylim(0, 1)
    ax.plot(np.arange(m + 2), np.ones(m + 2) * 0.5, 'r--', linewidth=1)
    ax.bar(np.arange(m) + 1, feq, width=.5, color=cm.get_cmap('tab20').colors[
        index])
    ax.set_title('抛%s次硬币' % value, pad=-20, fontsize=8)

#
# # 抛硬币实验二
num = 3000

result = np.add.accumulate(np.random.choice(2, num)) / (np.arange(num) + 1)

ax = axlist[np.unravel_index(5, axlist.shape)]
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.set_ylim(0, 1)
ax.plot(result)
ax.plot(np.arange(num), np.ones(num) * .5, 'r--', linewidth=1)
ax.set_title('硬币正面出现的频率', pad=-20, fontsize=8)

axani = plt.subplot2grid((3, 3), (2, 0), colspan=3)
axani.set_title('动态展示', pad=-10, fontsize=9)
line, = axani.plot(result[:1])
plt.ylim(0, 1)

#动画
frames = 1000
def animate(i):
    plt.xlim(0, (i + 1) * num / frames)
    line.set_xdata(np.arange((i + 1) * num // frames))
    line.set_ydata(result[0:((i + 1) * num // frames)])
    return line,


def init():
    return line,


ani = ani.FuncAnimation(fig=fig,
                        func=animate,
                        frames=frames,
                        interval=200, repeat=True,
                        blit=False)  # plt.tight_layout()
# plt.savefig('抛硬币模拟.png', format='png', bbox_inches='tight', transparent=True,
# dpi=200)  # bbox_inches='tight' 图片边界空白紧致, 背景透明
plt.show()