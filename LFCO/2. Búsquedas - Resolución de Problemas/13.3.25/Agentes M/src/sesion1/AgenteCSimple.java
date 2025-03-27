/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion1;

import jade.core.Agent;


/**
 *
 * @author lfcastil
 */
public class AgenteCSimple extends Agent {
    
    @Override
    protected void setup()
    {
        this.doWait(8000);
        
        System.out.println(" Soy el Agente " + this.getLocalName());
        
        SimpleB s = new SimpleB(20);
        this.addBehaviour(s);
        
        SimpleB s1 = new SimpleB(100);
        this.addBehaviour(s1);
        
    }
    
   
    
    
}
