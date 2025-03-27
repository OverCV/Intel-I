/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion2;

import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;

/**
 *
 * @author lfcastil
 */
public class ComportRecibirM extends CyclicBehaviour {

    @Override
     public void action() {
        
        ACLMessage msg;
        
        msg = this.myAgent.blockingReceive();
        //esta linea pasa cuando llega un mensaje
        
        
        System.out.println(" Mensaje recibido ");
        System.out.println( " del Agente --> "+ msg.getSender().getLocalName());
        System.out.println(" mensaje = " + msg.getContent());
        
        if (msg.getPerformative() == ACLMessage.REQUEST)
        {
            System.out.println(" llego un REQUEST ");
        }
        
    }
    
}
