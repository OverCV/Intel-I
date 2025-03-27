/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion1;

import jade.core.behaviours.OneShotBehaviour;
import jade.lang.acl.ACLMessage;
import jade.core.AID;

/**
 *
 * @author lfcastil
 */
public class ComportEnviarMensaje extends OneShotBehaviour {

    Object parametros [];
    String mensaje;
    
    
    public ComportEnviarMensaje(Object[] par, String mensaje)
    {
      this.parametros = par;
      this.mensaje = mensaje;
      
    }
    
    @Override
    public void action() {
     
        //definir un objeto ACLMessage enviarlo
        ACLMessage msg = new ACLMessage(ACLMessage.REQUEST);
        for (int i=0;i<parametros.length;i++)
        {
        AID p = new AID((String)parametros[i], AID.ISLOCALNAME);
   
        msg.addReceiver(p);
        }
        msg.setContent(mensaje);
        
        this.myAgent.send(msg);
        
        
        
    }
    
    
}
