// MyClient.java
import java.rmi.*;

public class MyClient {
    public static void main(String args[]) {
        try {
            // Assuming the server is running on localhost and on default port 1099
            Adder stub = (Adder) Naming.lookup("rmi://localhost/AdderService");
            System.out.println("Result of add(15, 30): " + stub.add(15, 30));
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
