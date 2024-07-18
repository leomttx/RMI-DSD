import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ola extends Remote { // Interface que extende a interface Remote(Interface Remota)
    String digaola() throws RemoteException;
}