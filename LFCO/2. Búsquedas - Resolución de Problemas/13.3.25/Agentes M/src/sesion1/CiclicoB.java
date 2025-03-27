/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion1;

import jade.core.behaviours.CyclicBehaviour;
/**
 *
 * @author lfcastil
 */
public class CiclicoB extends CyclicBehaviour{
   int n =0;
    
  public CiclicoB(int n)
    {
        this.n = n;
    }
  
    @Override
    public void action() {     
        for (int i=n;i<=2*n;i++)
        {
            System.out.println(" ciclo " + i);
        }
    }

    
    
}
