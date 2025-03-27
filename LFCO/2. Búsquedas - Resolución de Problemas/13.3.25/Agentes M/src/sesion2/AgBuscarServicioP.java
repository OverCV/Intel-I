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

public class AgBuscarServicioP extends Agent{
    
    public String servicio;
    
    /** Creates a new instance of BuscarServicio */
    public AgBuscarServicioP() {
    }
    
    protected void setup()
    { 
        Object [] arg2 = getArguments();
     
        servicio = (String) arg2[0];
     
        
        System.out.println(" Hola yo soy el agente :" +this.getLocalName() + "buscando servicios registrados ");
     doWait(1000);
     this.BuscarServicios(servicio);
    }
 
	

    protected void BuscarServicios(String servicio)
    {
     DFAgentDescription dfd = new DFAgentDescription();

    try {
      DFAgentDescription[] result = DFService.search(this, dfd);
      System.out.println("total Agentes Servicios en la Plataforma " + result.length + "Buscando cuales tiene servicio " + servicio );
      String out = " ";
      for (int i=0; i<result.length; i++) {
       
        Iterator iter = result[i].getAllServices();
        while (iter.hasNext()) {
          ServiceDescription sd = (ServiceDescription)iter.next();
          
          if (sd.getName().equalsIgnoreCase(servicio))
                 out += result[i].getName()+" provides "+ " "+sd.getName();
        }
        
      }
        System.out.println(this.getLocalName()+": "+out);
    }
    catch (Exception fe) {
      System.err.println(getLocalName() + " search with DF unsucceeded - "
        + fe.getMessage());
      doDelete();
    }

        
    }
    
}