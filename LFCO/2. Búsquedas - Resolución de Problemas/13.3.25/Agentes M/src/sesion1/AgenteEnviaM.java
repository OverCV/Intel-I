/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion1;

import jade.core.Agent;


public class AgenteEnviaM extends Agent {
    
    @Override
    protected void setup()
    {
       
        Object [] param = this.getArguments();
        if (param.length > 0)
        {
        
        ComportEnviarMensaje ce = new ComportEnviarMensaje(param, "Primer mensaje");
        this.addBehaviour(ce);
        }
        else
        {
            System.out.println("debe contener al menos un nombre agente parametro ");
        }
        
    }
    
   
    
    
}
