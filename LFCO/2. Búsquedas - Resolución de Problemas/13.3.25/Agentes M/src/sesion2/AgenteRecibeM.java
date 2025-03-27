/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion2;


import jade.core.Agent;


public class AgenteRecibeM extends Agent {
    
    @Override
    protected void setup()
    {
       ComportRecibirM cm = new ComportRecibirM();
       this.addBehaviour(cm);
        
    }
    
   
    
    
}
