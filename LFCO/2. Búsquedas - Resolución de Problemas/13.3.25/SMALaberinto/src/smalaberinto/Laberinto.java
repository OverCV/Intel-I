/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package smalaberinto;

/**
 *
 * @author Luis F
 */
public class Laberinto {
    
    /*public int cuadro[][] = 
    {   { 1,  0,  0, -1, 0, 0 },
        { 0, -1,  0, -1, -1, 0} ,
        { 0,  0,  0, 0, -1, 0} ,
        {-1,  0, -1, 0, -1, 0} ,
        { 0, -1, -1, 0, -1, 0} ,
        { 0,  -1, 0, 0, 0, 0} 
    };
    */
    public int cuadro[][];
    
 
    
    public Laberinto (CuadroLab cb)
    {
        this.cuadro = cb.cuadro;
    }
    
     public boolean verificarMov(int px, int py)
    {
        if ((px < 0)||(py <0)) 
            return false;
        if ((px == cuadro.length) || (py == cuadro[0].length))
            return false;

        if ((cuadro[px][py] == 2)||(cuadro[px][py]==-1))
         return false;
         
        return true; 
        
                   
    } 
    
    public void imprimirSolucion()
    {
        for (int i=0; i<cuadro.length;i ++)
        {
            for (int j=0; j< cuadro[0].length; j++)
                System.out.print(cuadro[i][j]+" ");
          System.out.println("");
        }
        System.out.println("=============================");
                       
    }
    
    
    public String toString()
    {
        return cuadro.toString();
    }
    
    /****
     * 
     * @param posx
     * @param posy
     * @return 
     */
    
    
    /////////////////////7
    
      public boolean encontroCamino2(int posx, int posy)
    {
        boolean abajo = false, izquierda = false, derecha = false, arriba = false;
        
        if ((posx == cuadro.length-1) && (posy == cuadro[0].length-1)) 
         {     
             System.out.println("SOLUCIONADO");  
             imprimirSolucion();
              return true;
         }
      else
         {
            // imprimirSolucion();
             for (int i=1; i<=4; i++)
             {
                 switch (i) {
                     
                     case 1:  if (verificarMov(posx, posy +1))
                                   { cuadro[posx][posy+1] = 1;
                                     abajo = encontroCamino2(posx, posy+1);
                                     if ( abajo == false)
                                         { 
                                             cuadro[posx][posy+1] = 2;
                                          }
                                     else
                                       return true;
                                   }
                                break;
                          
                     case 2:   if (verificarMov(posx+1, posy ))
                                 {    cuadro[posx+1][posy] = 1;
                                      derecha = encontroCamino2(posx+1, posy);
                                      if (derecha == false)
                                             cuadro[posx][posy+1] = 2;
                                      else
                                       return true;
                                 }
                                break;
                     case 3:
                             if (verificarMov(posx-1, posy ))
                               {    cuadro[posx-1][posy] = 1;
                                    izquierda = encontroCamino2(posx-1, posy);
                                    if (izquierda == false)
                                        cuadro[posx-1][posy] = 2;
                                    else
                                        return true;
                                }
                         break;
                         
                     case 4:  if (verificarMov(posx, posy-1 ))
                                   {    cuadro[posx][posy-1] = 1;
                                        arriba = encontroCamino2(posx, posy-1);
                                     if (arriba == false)
                                        cuadro[posx][posy-1] = 2;
                                     else
                                    return true;
                                   }
                              break;
                     
                 }
             }
           
             
         }
        return (arriba || abajo || derecha || izquierda);
    }    
    
}
