# Dataset 测试数据生成脚本
# 二维数据格式
# Col1 Col2 Col3 Col4 Col5
# Wang 32   12   13    Male
# Zhang 32   11  24    Female
# https://mockaroo.com

# Usage 使用介绍
# python3 dataset-generator.py resultType length range 
# Goal 1: 支持生成一维数字型数组

import os,sys,getopt
import numpy as np
from numpy import random

# 入口函数，第一个版本支持生成一维数字型数组
def main(argv):
    resultType = 'l'
    length = 100
    range = 10000

    print("Welcome usage mock-gen!")

    try:
        opts, args = getopt.getopt(argv, "hr:l:n:", ["resultType=","length=","range="])
        # print(opts)
    except getopt.GetoptError:
        print("Usage: python3 mock-gen.py -resultType <typename> -length <length> -range <range>")

    for opt, arg in opts:
        if opt in ("-r", "--resultType"):
            resultType = arg
        elif opt in ("-l", "--length"):
            length = int(arg)
        elif opt in ("-n", "--range"):
            range = int(arg)

    print( get_random_list(length, range) )

def get_random_list(length, max):
    i = 0
    result = []

    while i < length :
        result.append(np.random.randint(0,max))
        i = i + 1

    return result



if __name__ == "__main__":
    main(sys.argv[1:])