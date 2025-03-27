/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package sesion1;

import jade.core.behaviours.SimpleBehaviour;
/**
 *
 * @author lfcastil
 */
public class SimpleB extends SimpleBehaviour{
   int n =0;
    
  public SimpleB(int n)
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

    @Override
    public boolean done() {
      return true;
    }
    
    
}
