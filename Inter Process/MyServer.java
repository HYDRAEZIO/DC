// MyServer.java
import java.rmi.*;
import java.rmi.registry.*;

public class MyServer {
    public static void main(String args[]) {
        try {
            // Create and export a remote object
            Adder stub = new AdderRemote();
            // Bind the remote object's stub in the registry
            Naming.rebind("rmi://localhost/AdderService", stub);
            System.out.println("Server is ready.");
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
