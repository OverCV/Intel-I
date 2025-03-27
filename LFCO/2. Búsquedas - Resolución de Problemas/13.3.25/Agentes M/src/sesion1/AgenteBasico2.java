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
public class AgenteBasico2 extends Agent {
    
    @Override
    protected void setup()
    {
        System.out.println(" Soy el Agente " + this.getLocalName());
    }
    
}
