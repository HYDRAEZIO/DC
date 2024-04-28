import java.io.*;
import java.net.*;
import java.util.Scanner;
public class MyMaster {
public static void main(String[] args) {
Scanner userInput = new Scanner(System.in);
try{
Socket s=new Socket("localhost",6668);
DataOutputStream dout=new DataOutputStream(s.getOutputStream());
System.out.println("Enter the first number: ");
int x = userInput.nextInt();
System.out.println("Enter the second number: ");
int y = userInput.nextInt();
dout.writeInt(x);
dout.writeInt(y);
dout.flush();
dout.close();
s.close();
}catch(Exception e){System.out.println(e);}
}
}