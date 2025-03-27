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
import jade.domain.FIPAException;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import comportamientos.RecibirACLMessages;

                    // heredar de Agent
public class AgResuelveLab extends Agent{
    
    // Configuración 
    @Override
    protected void setup(){
        System.out.println(" Soy un Agente Resuelve un Laberinto >>> " +
                this.getLocalName()
                );
        registrarServicio();
        
        
        RecibirACLMessages rc1 = new RecibirACLMessages();
        this.addBehaviour(rc1);
        
    }
    
    
    private void registrarServicio()
    {
      DFAgentDescription dfd = new DFAgentDescription();
      dfd.setName(this.getAID());
      
      ServiceDescription sd = new ServiceDescription();
        sd.setType("ResolverLab");
        sd.setName("ResolverLab");
      dfd.addServices(sd);
      try{
          DFService.register(this,dfd);
          System.out.println("Registro servicio realizado "+sd.toString());
      }
     catch(FIPAException ex)
     {
      System.err.println("el Agente :"  + getLocalName() + "No ha podido registar el servicio : " + ex.getMessage());
      doDelete();
     }
      
} }
