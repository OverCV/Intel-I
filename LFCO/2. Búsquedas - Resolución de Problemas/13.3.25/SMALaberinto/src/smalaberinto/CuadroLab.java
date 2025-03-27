/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package smalaberinto;


/**
 *
 * @author lfcastil
 */
public class CuadroLab implements java.io.Serializable {
    
  //  public int cuadro[][] = 
  //  {   { 1,  0,  0, -1, 0, 0 },
  //      { 0, -1,  0, -1, -1, 0} ,
  //      { 0,  0,  0, 0, -1, 0} ,
  //      {-1,  0, -1, 0, -1, 0} ,
  //      { 0, -1, -1, 0, -1, 0} ,
  //      { 0,  -1, 0, 0, 0, 0} 
  //  };
    
    public int cuadro[][];
    
    public CuadroLab (int x, int y)
    {
        this.cuadro = new int [x][y];      
    }
    
    public void initCuadro(int cuadrito [] [])
    {
      this.cuadro = cuadrito;
    }
           
    public void setBloqueCuadro(int x1, int y1)
    {
        this.cuadro [x1][y1] = -1;
    }
    
    public void setLibreCuadro(int x1, int y1)
    {
        this.cuadro [x1][y1] = 0;
    }
    
    public void setInicioCuadro(int x2, int y2)
    {
        this.cuadro[x2][y2]= 1;
    }
    
    /**
     this.cuadro[][] = 
    {   { 1,  0,  0, -1, 0, 0 },
        { 0, -1,  0, -1, -1, 0} ,
        { 0,  0,  0, 0, -1, 0} ,
        {-1,  0, -1, 0, -1, 0} ,
        { 0, -1, -1, 0, -1, 0} ,
        { 0,  -1, 0, 0, 0, 0} 
    };
    * */
    public void initCuadroCompleto()
    {
        //fila 1
        setInicioCuadro(0,0);
        setLibreCuadro(0,1);
        setLibreCuadro(0,2);
        setBloqueCuadro(0,3);
        setLibreCuadro(0,4);
        setLibreCuadro(0,5);
        //fila 2
        setLibreCuadro(1,0);
        setBloqueCuadro(1,1);
        setLibreCuadro(1,2);
        setBloqueCuadro(1,3);
        setBloqueCuadro(1,4);
        setLibreCuadro(1,5);
        //fila 3
        setLibreCuadro(2,0);
        setLibreCuadro(2,1);
        setLibreCuadro(2,2);
        setLibreCuadro(2,3);
        setBloqueCuadro(2,4);
        setLibreCuadro(2,5);
         //fila 4
        setBloqueCuadro(3,0);
        setLibreCuadro(3,1);
        setBloqueCuadro(3,2);
        setLibreCuadro(3,3);
        setBloqueCuadro(3,4);
        setLibreCuadro(3,5);
        //fila 5
        setLibreCuadro(4,0);
        setBloqueCuadro(4,1);
        setBloqueCuadro(4,2);
        setLibreCuadro(4,3);
        setBloqueCuadro(4,4);
        setLibreCuadro(4,5);
        //fila 6
         setLibreCuadro(5,0);
         setBloqueCuadro(5,1);
         setLibreCuadro(5,2);
         setLibreCuadro(5,3);
         setLibreCuadro(5,4);
         setLibreCuadro(5,5);
      
    }
    
    @Override
    public String  toString ()
    {
        String cad = " ";
        for (int[] cuadro1 : cuadro) {
            for (int j = 0; j< cuadro[0].length; j++) {
                cad = cad + cuadro1[j] + " ";
            }
            cad = cad + "\n";
        }
       
       return cad;                 
    }
    
}
