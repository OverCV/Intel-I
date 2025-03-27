package app;

import jade.gui.GuiEvent;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *
 * @author lfcastil
 */
public class VentanaChatALL extends JFrame {
    
    private TestTalkAgentALL myAgent;
    private JTextArea mensajesArea;
    private JTextField mensajeField;
    private JTextField destinatarioField;
    private JButton enviarButton;
    private JButton enviarTodosButton;
    
    public VentanaChatALL(TestTalkAgentALL agent, String title) {
        super(title);
        this.myAgent = agent;
        
        // Configuración del panel
        JPanel panel = new JPanel(new BorderLayout());
        
        // Área de mensajes
        mensajesArea = new JTextArea(15, 30);
        mensajesArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(mensajesArea);
        panel.add(scrollPane, BorderLayout.CENTER);
        
        // Panel inferior para entrada de mensaje
        JPanel bottomPanel = new JPanel(new BorderLayout());
        
        // Panel para destinatario
        JPanel destinatarioPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        destinatarioPanel.add(new JLabel("Destinatario:"));
        destinatarioField = new JTextField(15);
        destinatarioPanel.add(destinatarioField);
        bottomPanel.add(destinatarioPanel, BorderLayout.NORTH);
        
        // Panel para mensaje y botones
        JPanel mensajePanel = new JPanel(new BorderLayout());
        mensajeField = new JTextField(20);
        mensajePanel.add(mensajeField, BorderLayout.CENTER);
        
        JPanel botonesPanel = new JPanel(new FlowLayout());
        enviarButton = new JButton("Enviar");
        enviarTodosButton = new JButton("Enviar a Todos");
        
        botonesPanel.add(enviarButton);
        botonesPanel.add(enviarTodosButton);
        mensajePanel.add(botonesPanel, BorderLayout.EAST);
        
        bottomPanel.add(mensajePanel, BorderLayout.CENTER);
        panel.add(bottomPanel, BorderLayout.SOUTH);
        
        // Agregar panel principal al frame
        this.getContentPane().add(panel);
        
        // Eventos de botones
        enviarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String destinatario = destinatarioField.getText().trim();
                String mensaje = mensajeField.getText().trim();
                
                if (!destinatario.isEmpty() && !mensaje.isEmpty()) {
                    GuiEvent ge = new GuiEvent(this, 0);
                    ge.addParameter(destinatario);
                    ge.addParameter(mensaje);
                    myAgent.postGuiEvent(ge);
                    
                    mensajesArea.append("Yo -> " + destinatario + ": " + mensaje + "\n");
                    mensajeField.setText("");
                }
            }
        });
        
        enviarTodosButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String mensaje = mensajeField.getText().trim();
                
                if (!mensaje.isEmpty()) {
                    GuiEvent ge = new GuiEvent(this, 1);
                    ge.addParameter(mensaje);
                    myAgent.postGuiEvent(ge);
                    
                    mensajesArea.append("Yo -> TODOS: " + mensaje + "\n");
                    mensajeField.setText("");
                }
            }
        });
        
        // Configuración final del frame
        this.pack();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public void mostrarMensaje(String mensaje) {
        mensajesArea.append(mensaje + "\n");
    }
}