import numpy as np
from unittest import TestCase

file_name='E:\work\idea_workspace\py\quantitative_trade\com\qt\demo\股票行情数据000001SZ.csv'
class TestNumpyStock(TestCase):
    """
    读取指定列
    numpy.loadtxt 常用关键字参数:
    1. fname 文件名；
    2. delimiter 分隔符；
    3. usecols 选取列（元组）；
    4. unpack 是否按列拆成多个数组；
    5. encoding、skiprows 处理 UTF-8 与表头。
    CSV 列: 股票代码,交易日期,开盘价,最低价,最高价,收盘价,成交量 → 索引 0..6
    """

    def testReadFile(self):
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print(close_price, volume)
        # [ 9.71 10.3   9.99  9.6   9.85  9.86  9.47 10.2  10.3  10.62 11.11 11.36 11.79 11.79 11.64 11.66 11.95 13.04 12.8  13.19]
        # [ 340827.  635330.  611960.  392572.  604457.  415480. 1730708.  765325. 895014.  664370.  936335.  472975.  824456.  469410.  345713.  329749. 368640.  540952.  373428.  324698.]

    # 计算最大值与最小值（最高价序列、最低价序列）
    def testMaxAndMin(self):
        high_price, low_price = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(4, 5),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("high_price:", high_price.max())  # 13.44
        print("low_price:", low_price.min())    # 8.88


    # 极差：最高价序列与最低价序列各自的 peak-to-peak
    def testPtp(self):
        high_price, low_price = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(4, 5),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("max - min of high price:", np.ptp(high_price))  # 3.8099999999999987
        print("max - min of low price:", np.ptp(low_price))    # 3.9399999999999995

    # 计算成交里加权平均价格
    # 成交里加权平均价格，英文名WAP(Volume-Weighted Average Price，成交里加权平均价格)是一个非常重要的经济学里，代表着金融资产的"平均”价格
    # 成交量加权平均价格 VWAP ≈ sum(收盘价 * 成交量) / sum(成交量)
    def testAVG(self):
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("avg_price:{}".format(np.average(close_price)))
        print("VWAP:{}".format(np.average(close_price, weights=volume)))
        # avg_price:11.0115
        # VWAP:10.768422980338055

    # 计算中位数  收盘价的中位数
    def testMedian(self):
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("close_price median:{}".format(np.median(close_price)))
        # close_price median:10.864999999999998

    # 计算方差  收盘价的方差
    def testVar(self):
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("close_price variance:{}".format(np.var(close_price)))
        print("close_price variance:{}".format(close_price.var()))
        # close_price variance: 1.3352127499999997
        # close_price variance: 1.3352127499999997

    # 计算股票收益率、年波动率及月波动率
    # 波动率是对价格变动的一种度里，历史波动率可以根据历史价格数据计算得出。计算历史波动率时，需要用到对数收益率
    # 年波动率等于对数收益率的标准差除以其均值，再乘以交易日的平方根，通常交易日取250天
    # 月波动率等于对数收益率的标准差除以其均值，再乘以交易月的平方根。通常交易月取12月
    def testVolatility(self):
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        log_return = np.diff(np.log(close_price))

        annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250)

        monthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12)

        print("annual_volatility:{}".format(annual_volatility))
        print("monthly_volatility:{}".format(monthly_volatility))
        # annual_volatility:34.45147972091315
        # monthly_volatility:7.547941033030367