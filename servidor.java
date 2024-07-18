import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class servidor {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.createRegistry(1099); 
   
            Naming.rebind("rmi://localhost:1099/Ola", new ola_Imple()); // Registra o objeto remoto no Registry
            
            System.out.println("Servidor pronto");
            
        } catch (RemoteException | MalformedURLException e) {
            e.printStackTrace();
        } // É no Registry que são registrado os objetos remotos e onde os clientes procuram por eles
    }
}
