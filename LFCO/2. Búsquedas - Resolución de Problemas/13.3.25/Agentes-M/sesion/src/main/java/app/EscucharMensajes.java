package app;


import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;

/**
 *
 * @author lfcastil
 */
public class EscucharMensajes extends CyclicBehaviour {
    
    private VentanaChatALL ventana;
    
    public EscucharMensajes(VentanaChatALL ventana) {
        this.ventana = ventana;
    }
    
    @Override
    public void action() {
        ACLMessage msg = myAgent.receive();
        if (msg != null) {
            String emisor = msg.getSender().getLocalName();
            String contenido = msg.getContent();
            
            ventana.mostrarMensaje(emisor + ": " + contenido);
        } else {
            block();
        }
    }
}