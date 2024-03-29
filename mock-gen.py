# coding=UTF-8
# Dataset 测试数据生成脚本
# 二维数据格式
# Col1 Col2 Col3 Col4 Col5
# Wang 32   12   13    Male
# Zhang 32   11  24    Female
# https://mockaroo.com

# Usage 使用介绍
# python3 dataset-generator.py resultType length range 
# Goal 1: 支持生成一维数字型数组
# Goal 2: 将输出改成JSON格式，对一维数组输出统计指标，包括平均值、方差、最小值、最大值

import os,sys,getopt
import time, datetime
import threading
# import numpy as np
# from numpy import random

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

    # print( get_random_list(length, range) )
    generator_apm_log()

#生成APM格式的日志
def generator_apm_log():
    filename = "apm_test_log.txt"



    with open(filename,"a+") as f:
        try:
            i = 0
            user_str = ""
            while i < 10:
                user_str += str(time.ctime()) + " <sys> <id> \n"
                i = i + 1
            f.writelines(user_str)
            threading.Timer(0.01, generator_apm_log).start()
        except KeyboardInterrupt:
            f.close()
            sys.exit()

    return True

def get_random_list(length, max):
    i = 0
    result = []

    while i < length :
        result.append(np.random.randint(0,max))
        i = i + 1

    return result



if __name__ == "__main__":
    main(sys.argv[1:])