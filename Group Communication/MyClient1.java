import java.io.*;
import java.net.*;
import java.util.Scanner;
public class MyClient1 {
public static void main(String[] args) {
Scanner userInput = new Scanner(System.in);
try{
Socket s=new Socket("localhost",6667);
System.out.println("waiting for master to send msg\n");
DataInputStream dis=new DataInputStream(s.getInputStream());

int x = (Integer)dis.readInt();
System.out.println("recieved msg: "+x);
dis.close();
s.close();
}catch(Exception e){System.out.println(e);}
}
}