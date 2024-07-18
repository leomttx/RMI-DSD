import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ola_Imple extends UnicastRemoteObject implements ola { // Essa classe é o objeto remoto pq implementa a interface remota

    protected ola_Imple() throws RemoteException {
        super(); // Chama o construtor da classe pai
    }

    @Override // Sobrescreve o método digaola() da interface ola
    public String digaola() throws RemoteException {
        return "Olá, mundo!";
    }
}
