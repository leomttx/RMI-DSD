import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

public class cliente {
    public static void main(String[] args) {
        // o stub é responsável por fazer a comunicação entre o cliente e o servidor
        try {
            
            ola stub = (ola) Naming.lookup("rmi://localhost:1099/Ola");
            System.out.println(stub.digaola());

        } catch (MalformedURLException | RemoteException | NotBoundException e) {

            e.printStackTrace();
        } // Procura o objeto remoto no Registry
     }
}
