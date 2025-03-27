/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package comportamientos;

/**
 *
 * @author lfcastil
 */
import jade.core.behaviours.CyclicBehaviour;

import jade.lang.acl.ACLMessage;
import jade.core.AID;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import smalaberinto.CuadroLab;

public class SendACLMessages extends CyclicBehaviour {

    AID nAgente;
    
    public SendACLMessages(AID nAgente)
    {
        this.nAgente = nAgente;
    }
    
    
    @Override
    public void action()
    {
        ACLMessage  msg = new ACLMessage(ACLMessage.REQUEST);
        System.out.println("Nombre Agente Resuelve es" +nAgente.getLocalName());
        
       if (nAgente != null)
           
 {
        
        msg.addReceiver(nAgente);
         try {
             CuadroLab cl = new CuadroLab(6,6);
             cl.initCuadroCompleto();
             msg.setContentObject(cl); //Envio Laberinto
             }
        catch (Exception ce)
        { System.out.println("error " +ce.toString());}

        this.myAgent.send(msg);
        
        ACLMessage resp = this.myAgent.blockingReceive();
        System.out.println(" " + resp.getContent());
       
    }
       
    }
}
