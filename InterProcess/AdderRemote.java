// AdderRemote.java
import java.rmi.*;
import java.rmi.server.*;

public class AdderRemote extends UnicastRemoteObject implements Adder {
    // Constructor
    public AdderRemote() throws RemoteException {
        super();
    }

    // Implementation of the add method
    public int add(int x, int y) {
        return x + y;
    }
}
