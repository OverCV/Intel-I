package sesion2;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lfcastil
 */

import jade.util.leap.Iterator;
import jade.core.Agent;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;

public class AgBuscarServicio extends Agent{
    
 
    
    /** Creates a new instance of BuscarServicio */
    public AgBuscarServicio() {
    }
    
    protected void setup()
    { 
        
        
        System.out.println(" Hola yo soy el agente :" +this.getLocalName() + "buscando servicios registrados ");
     doWait(1000);
     this.BuscarServicios();
    }
 
	

    protected void BuscarServicios()
    {
     DFAgentDescription dfd = new DFAgentDescription();

    try {
      DFAgentDescription[] result = DFService.search(this, dfd);
      System.out.println("total buscados " + result.length);
      for (int i=0; i<result.length; i++) {
        String out = result[i].getName()+" provides";
        Iterator iter = result[i].getAllServices();
        while (iter.hasNext()) {
          ServiceDescription sd = (ServiceDescription)iter.next();
          out += " "+sd.getName();
        }
        System.out.println(this.getLocalName()+": "+out);
      }
    }
    catch (Exception fe) {
      System.err.println(getLocalName() + " search with DF unsucceeded - "
        + fe.getMessage());
      doDelete();
    }

        
    }
    
}