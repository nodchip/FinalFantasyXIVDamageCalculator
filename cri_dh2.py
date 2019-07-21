import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
from matplotlib import rcParams

def func1(critical, directhit):
    critical_ratio = (200.0 * (critical - 380.0) / 3300.0 + 50.0) / 1000.0
    critical_damage_scale = (200.0 * (critical - 380.0) / 3300.0 + 1400.) / 1000.0
    critical_up = critical_ratio * critical_damage_scale + (1.0 - critical_ratio) * 1.0
    directhit_ratio = (550.0 * (directhit - 380.0) / 3300.0) / 1000.0
    directhit_damage_scale = 1.25
    directhit_up = directhit_ratio * directhit_damage_scale + (1.0 - directhit_ratio) * 1.0
    return (critical_up * directhit_up - 1.0) * 100.0


def main():
    matplotlib.font_manager.findSystemFonts()
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
    plt.figure(figsize=(12, 8))
    for sum in range(3000, 6000, 200):
        x = np.arange(380, sum - 380, 10)
        y = func1(x, sum - x)
        plt.plot(x, y, label='クリ+DH={sum}'.format(sum=sum))
    plt.xlabel('←ダイレクトヒット クリティカル→')
    plt.ylabel('ダメージ上昇率')
    plt.legend()
    plt.grid()
    #plt.show()
    plt.savefig('figure.png')


if __name__ == '__main__':
    main()
