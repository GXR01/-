import java.util.Scanner;

public class isPrimeNum{
    public static void main(String[] args){
        //输入
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个正整数：");
        int num = sc.nextInt();

        //判断
        for(int i=2;i<num;i++){
            if(num%i ==0){
                System.out.println(num+"不是质数")
                break;
                }
            else
                System.out.println(num+"是质数")
    }
}
