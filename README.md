# RedPacketAllocated
微信抢红包算法


## 初始化红包
每个红包最低为0.01元，即一分钱。因此所以红包分配算法做初始化的时候，**必须先保证每个红包都不能出现0元或负数**。我们可以先给每个红包分配一分钱，剩下的再进行后续分配。这样，就保证了每个红包至少1分钱的入账。
结合上述分析，每个人至少一分钱，则n人的红包总数额不能低于n分钱。系统会在分配前做判断，若不能保证每个红包至少一分钱，如4分钱分给5个人，系统就会报错，分配算法提前终止。


## 生成随机数
对于多少个红包，生成多少个随机数。
但是分配原则是：**每个随机数占随机数和的比例，跟每个红包放的钱占总分配钱的比例是一样的**。所以，每个红包分配到的金额数，可以先用数组中与自己对应的随机数（例如你是第8个人，那就是randNum[7]）除以随机数和（randSum），得出比值，再乘以可分配数额（allocateSum）得出。因为金额的最小单位是分，所以需要做四舍五入。加上最初固定的1分钱，那所有红包的数额都计算出来了。


## 末位特殊处理
到了这一步，有个问题是java普通开发中的四舍五入是不准确的，特别是处理这种金融问题。是不能出现发红包的总金额跟每个人领到的数目之和不一样的尴尬情况！
解决方法：对于前面n-1个红包采用上述随机数比值的分配方式，最后一个红包就不用这种方式了，改为**拿可分配金额数减去之前n-1个红包已经分配的金额数**。这也是为何最后一个人总是拿到较大的红包的原因。原因就是末位特殊处理机制便使多出来但无法分配的一小部分落入最后一个红包。


#python版本修改
微信团队公布的算法：红包金额的区间为:【0.01 ～ 平均值的2倍】
