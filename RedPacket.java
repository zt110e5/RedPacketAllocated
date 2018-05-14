package zt;

import java.util.Scanner;
/**  
* 类说明: 微信抢红包算法
* @author ZhangJingbo
* @date 2018年5月14日   
*/
public class RedPacket {
	static double result[];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int redPacketNum = sc.nextInt();		//红包个数
		double money = sc.nextDouble();		//红包总金额
		//若每个人分不到0.01元，则显示金额太少，结束程序
		if (redPacketNum * 1.0 / 100 > money) {
			System.out.println("钱太少了，给兄弟们多发点吧!");
			return;
		}	
		RedPacketAllocated(redPacketNum, money * 100); 		//将金额由元转化为分
		for (double string : result) {
			System.out.println(string);
		}
		sc.close();
	}
	
	private static void RedPacketAllocated(int num, double money) {
		result = new double[num];
		double randomNums[] = new double[num];
		double randomSum = 0;		//随机数和
		double allocateSum = money - num;		//按每个人先分1分钱，剩下的再随机分配
		for (int i = 0; i < randomNums.length; i++) {
			randomNums[i] = Math.random()*allocateSum;
			randomSum += randomNums[i];
		}
		//对四舍五入做特殊处理
		double left = allocateSum;
		for(int i = 0; i < result.length - 1; i++) {
			result[i] = Math.round(randomNums[i]/randomSum*allocateSum);
			left -= result[i];
			result[i] = (result[i]+1)*1.0/100;
		}
		result[num - 1] = (left + 1)*1.0/100;
	}
	
}
