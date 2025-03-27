/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package agentes;

/**
 *
 * @author lfcastil
 */
// primer cambio
import jade.core.Agent;
import comportamientos.SendACLMessages;
import jade.core.AID;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;

                    // heredar de Agent
public class AgLaberinto extends Agent{
    
    AID agenteJuego;
    // Configuración 
    @Override
    protected void setup(){
        System.out.println(" Soy un Agente necesita Salir Laberinto  >>> " +
                this.getLocalName()
                );
        
       
        
        this.doWait(8000);
         buscarServicio();
        SendACLMessages rc1 = new SendACLMessages(agenteJuego);
        this.addBehaviour(rc1);
        
    }
    
    
    public void buscarServicio()
            
    {
            System.out.println("Buscando Agente Solucione Lab ");
            // Bsqueda del servicio en las p�ginas amarillas.
            ServiceDescription servicio = new ServiceDescription();
            servicio.setType("ResolverLab");
            servicio.setName("ResolverLab");

            DFAgentDescription descripcion = new DFAgentDescription();
            descripcion.addServices(servicio);

          try {
                DFAgentDescription[] resultados = DFService.search(this, descripcion);
                if (resultados.length > 0) {
                    
                    System.out.println("encontrado");
                   
                    for (DFAgentDescription agent : resultados) {
                        agenteJuego = agent.getName();
                        
                    }
                } else {
                    
                    System.out.println("no encontrado");
                    doWait(1000);

                }
            } catch (Exception e) {
                System.out.println("error al buscar el juego: " + e.getMessage());
            }
        }

   

   
    
}
