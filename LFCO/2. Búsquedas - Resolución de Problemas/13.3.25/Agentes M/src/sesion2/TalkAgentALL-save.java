// C:\Users\overd\Links\Academia\Inteligent\Systems\Classroom\LFCO\2. Búsquedas - Resolución de Problemas\13.3.25\Agentes M\src\sesion2\TalkAgentALL.java
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion2;

import jade.core.AID;
import jade.domain.DFService;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.domain.FIPAException;
import jade.gui.GuiAgent;
import jade.gui.GuiEvent;
import jade.lang.acl.ACLMessage;
import jade.util.leap.Iterator;
import java.util.List;
import java.util.ArrayList;

/**
 *
 * @author lfcastil
 */
public class TalkAgentALL extends GuiAgent {

    VentanaChatALL ventana;
    
    @Override
    protected void setup()
    {
       ventana = new VentanaChatALL(this, this.getLocalName());
       ventana.setBounds(10,10,400,400);
       ventana.setVisible(true);
       
       registrerServiceCHAT();
       
       EscucharMensajes em = new EscucharMensajes(ventana);
       this.addBehaviour(em);
       
       
    }
    
    @Override
    protected void onGuiEvent(GuiEvent ge) {
        
        if (ge.getType() == 0)// origen Evento
        {
            ACLMessage msg = new ACLMessage(ACLMessage.CONFIRM);
            AID x = new AID ((String)ge.getParameter(0), 
                                AID.ISLOCALNAME);
            msg.addReceiver(x);
            msg.setContent((String)ge.getParameter(1));
            
            send(msg);
        }
        else
        
        if (ge.getType() == 1)// 
        {
            ACLMessage msg = new ACLMessage(ACLMessage.CONFIRM);
            
            List lst = BuscarServicioChat();
            
            for (int i=0; i<lst.size();i++)
            { AID x = (AID) lst.get(i);
            
           
             msg.addReceiver(x);
            }
            msg.setContent((String)ge.getParameter(0));
            
            send(msg);
        }
    }
    
    protected List BuscarServicioChat()
    {
      List myList = new ArrayList();
      
        DFAgentDescription dfd = new DFAgentDescription();

    try {
      DFAgentDescription[] result = DFService.search(this, dfd);
      System.out.println("total Agentes Servicios en la Plataforma " + result.length + "Buscando cuales tiene servicio CHAT " );
      String out = " ";
      for (int i=0; i<result.length; i++) {
       
        Iterator iter = result[i].getAllServices();
        while (iter.hasNext()) {
          ServiceDescription sd = (ServiceDescription)iter.next();
          
          if (sd.getName().equalsIgnoreCase("CHAT"))
                myList.add(result[i].getName());
                
        }
        
      }
        System.out.println(this.getLocalName()+": "+out);
    }
    catch (Exception fe) {
      System.err.println(getLocalName() + " search with DF unsucceeded - "
        + fe.getMessage());
      doDelete();
    }
    return  myList;
    }
    
    
    private void registrerServiceCHAT()
    {
      DFAgentDescription dfd = new DFAgentDescription();
      dfd.setName(this.getAID());
      
      ServiceDescription sd = new ServiceDescription();
      sd.setType("CHAT");
      sd.setName("CHAT");
      
      dfd.addServices(sd);
      try{
          DFService.register(this,dfd);
      }
     catch(FIPAException ex)
     {
      System.err.println("el Agente :"  + getLocalName() + "No ha podido registar el servicio : " + ex.getMessage());
      doDelete();
     }
    }
    
}
