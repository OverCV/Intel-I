/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion2;


import jade.core.Agent;


public class AgenteRecibeM2 extends Agent {
    
    @Override
    protected void setup()
    {
       ComportRecibirM2 cm = new ComportRecibirM2();
       this.addBehaviour(cm);
        
    }
    
   
    
    
}
