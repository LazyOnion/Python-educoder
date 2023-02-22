def estimate_pi_by_bbp(n_terms = 1000) -> float:
    """
    利用 Bailey–Borwein–Plouffe 公式进行计算，此方法可以得到 15 位精度的 pi 值
    :param n_terms:计算项数 n，默认值 1000
    :return:返回保留小数点后15位的 pi 值
    """
    res = 0
    for i in range(n_terms + 1):
        res = res + (1 / 16 ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return res
