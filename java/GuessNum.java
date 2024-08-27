import java.util.Random

public class GuessNum {
    public static void main(String[] args){
        //生成随机数字
        Random r = new Random();
        int num = 1+r.nextInt(100);
        //猜数字
       while(true){
            Scanner sc = new Scanner(System.in);
            System.out.prinln("请输入你要猜的数字：")
            int guessNum = sc.nextInt();
            if(guessNum>num){
	Sytem.out.println("大了");
            }
            else if(guessNum<num){
	Sytem.out.println("小了");
            }
            else if(guessNum==num){
	Sytem.out.println("猜中了");
            }
	break;
          }
    }
}
