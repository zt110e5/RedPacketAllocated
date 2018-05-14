import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor
import random


#领红包程序
def RedPacketAllocated(number, money):
	#判断人数是不是整数
	if type(number) == type(1):
		moneyMin = 0.01

		#最大为平均值的2倍
		moneyMax = money / number * 2
		if money > number * 0.01:
			getMoney = random.randint(1,100)/100*moneyMax
			if getMoney < moneyMin:
				getMoney = moneyMin
				return round(getMoney,2)
			else:
				return round(getMoney,2)
		elif money == round(number*0.01,2):
			return 0.01
		elif money < round(number*0.01,2):
			print("金额太少，大兄弟多给点吧。。。")
			exit()
	else:
		print("输入的不是整数，请重新输入...")
		exit()

#领红包方法
def getRedPacketByThread(number,money):
	a = []
	#进程数
	pool = ThreadPoolExecutor(int(number))
	temp = number
	for i in range(number):
		if i + 1 == temp:
			getmoney = money
			print("第" + str(i + 1) + "个人得到了" + str(getmoney) + "元钱，红包已经被领完！")
		else:
			result = pool.submit(RedPacketAllocated, number, money)
			getmoney = result.result()
			number = number - 1
			money = round(money - getmoney, 2)
			print("第" + str(i + 1) + "个人得到了" + str(getmoney) + "元钱，还剩下" + str(number) + "个红包没有人领取，还剩下" + str(
				money) + "元钱！")
		a.append(getmoney)
	return a


if __name__ == "__main__":
	number = int(input("请输入红包个数:"))
	money = float(input("请输入总金额:"))
	# 程序测速
	a = time.clock()
	arr = []
	arr = getRedPacketByThread(number, money)
	sum = 0
	for item in arr:
		sum = sum + item
	# 程序测速
	b = time.clock()

	print("总共发送的钱为" + str(round(sum, 2)) + " 程序运行时间为：" + str(b - a))




