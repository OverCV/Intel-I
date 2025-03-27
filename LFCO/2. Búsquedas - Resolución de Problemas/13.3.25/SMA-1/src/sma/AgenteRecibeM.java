// C:\Users\overd\Links\Academia\Inteligent\Systems\Classroom\LFCO\2. Búsquedas - Resolución de Problemas\13.3.25\SMA-1\src\sma\AgenteRecibeM.java
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package sma;

import jade.core.Agent;

/**
 *
 * @author luisfercastillo
 */
public class AgenteRecibeM extends Agent{
    
    protected void setup()
    {
        ComportRecibirM  cs = new ComportRecibirM();
        this.addBehaviour(cs);
        
    }
    
}
