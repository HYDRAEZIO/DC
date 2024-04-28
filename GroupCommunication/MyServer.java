import java.io.*;
import java.net.*;
import java.util.Scanner;
public class MyServer {
public static void main(String[] args){
try{
ServerSocket ss=new ServerSocket(6668);
System.out.println("waiting for master to connect...");
Socket s=ss.accept();
//establishes connection with master
System.out.println("master connected");
System.out.println("enter number of slaves:");
ServerSocket ss2=new ServerSocket(6667);
Scanner sc = new Scanner(System.in);
int n=sc.nextInt();
Socket[] sl= new Socket[n];
for(int i=0;i<n;i++){
sl[i]=ss2.accept();
//establishes connection with slaves
System.out.println("slave "+(i+1)+"connected\n");}
System.out.println("waiting for master to send msg\n");
DataInputStream dis=new
DataInputStream(s.getInputStream());
int x = (Integer)dis.readInt();
int y = (Integer)dis.readInt();
System.out.println("recieved msg from master..");
int sum = (x + y);
System.out.println(sum);
dis.close();
System.out.println("sending sum msg to slaves..\n");
for(int i=0;i<n;i++){
DataOutputStream dout=new
DataOutputStream(sl[i].getOutputStream());
dout.writeInt(sum);
dout.flush();dout.close();}
System.out.println("disconnecting slaves..\n");

ss2.close();
System.out.println("disconnecting master..\n");
ss.close();
}catch(Exception e){System.out.println(e);}
} 
}