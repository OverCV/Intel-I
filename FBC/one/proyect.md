# UNIVERSIDAD
## INGENIERÍA DE SISTEMAS Y COMPUTACIÓN  
### SISTEMAS INTELIGENTES I - PRIMER PROYECTO  

### **UrbanLift: Sistema de Simulación para Optimización de Operaciones**  

**Descripción del Proyecto**  
UrbanLift, la empresa de transporte de pasajeros, busca optimizar la eficiencia de sus operaciones mediante la implementación de un sistema de simulación que modele la red vial de la ciudad en la que presta sus servicios.  

La estructura vial de la ciudad incluye:  
- Carreras y calles numeradas, transitables en uno o ambos sentidos.  
- Semáforos en las intersecciones, capaces de detener el tráfico por períodos configurables.  
- Una disposición no fija de paraderos para los vehículos de UrbanLift.  

### **Funcionalidades del Sistema**  
El sistema de simulación permitirá a los usuarios:  
1. **Realizar solicitudes de vehículos en cualquier momento y lugar**.  
   - El operador asignará el vehículo más cercano y trazará la ruta más eficiente hacia el destino del pasajero.  

2. **Designar la mejor ruta según criterios específicos**:  
   - **Ruta más corta**: Sin considerar la semaforización.  
   - **Ruta más rápida**: Independientemente del costo, considerando la semaforización.  
   - **Ruta con menor consumo de combustible**: Calculado dividiendo la longitud de la ruta entre la eficiencia del vehículo (ej. kilómetros por litro).  
   - **Ruta más económica para el pasajero**: Aunque no sea la más corta.  

3. **Servicio exclusivo "Tour-Trip"**:  
   - Visita todos los puntos de interés de la ciudad.  
   - Precio único, independientemente del consumo de combustible o tiempo por semaforización.  

### **Reporte de Viajes**  
Cada viaje concluido generará automáticamente un reporte detallado que incluye:  
- Costo del viaje.  
- Cantidad de calles y carreras transitadas.  
- Duración del servicio.  
- Comparación de rutas (si se seleccionó la ruta de menor consumo de combustible).  

### **Requisitos de Visualización**  
- Simulación en tiempo real de los viajes.  
- Identificador único asignado a cada vehículo en el modelo.  
- Visualización de calles y carreras en la GUI, distinguiendo el sentido de tránsito.  
- Reflejar cada paso de la simulación en la interfaz.  

### **Consideraciones Técnicas**  
- Aplicar los algoritmos de búsqueda más adecuados para cada tarea.  
- Justificar la elección de algoritmos en la sustentación.  
- La GUI puede ser por consola; implementaciones gráficas recibirán puntos adicionales.  

### **Normas del Proyecto**  
- **Grupos de trabajo**: Máximo de 2 personas.  
- **Fecha de entrega y sustentación**: 01-abril-2024.  
