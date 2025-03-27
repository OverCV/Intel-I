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
import smalaberinto.CuadroLab;
import smalaberinto.Laberinto;

public class RecibirACLMessages extends CyclicBehaviour {
    
    public void action()
    {
        ACLMessage msg = this.myAgent.receive();
        
        if (msg != null)
        {
            
            try 
              {
                 Object obj =  msg.getContentObject();  
                 if (obj instanceof CuadroLab) 
                 {
                    Laberinto lab =new Laberinto((CuadroLab)obj);
                   
                    if ( lab.encontroCamino2(0,0) == true)
                       {
            
                        System.out.println("Solucionado");
                        ACLMessage resp = new ACLMessage(ACLMessage.INFORM);
                        resp.addReceiver(msg.getSender());
                        resp.setContent("Solucionado " + lab.toString());
                        
                       }
                    else
                    {  System.out.println("No hay solucion");
                       ACLMessage resp = new ACLMessage(ACLMessage.INFORM);
                        resp.addReceiver(msg.getSender());
                        resp.setContent("no hay solucion " );
                    }
                 }
              }
			  
                 catch (Exception e) {;}
       }
   }
 }
 