Entonces el del laberinto.

Hace que en el SRC tiene varios elementos, los agentes, los comportamientos y el laberinto.

En agentes tiene el laberinto y el que resuelve el laberinto, uno lo tiene y el otro lo resuelve, pero, acá en comportamientos, uno escucha y otro envía mensajes, como cuando  entonces el recibir es un escuchador y el otro un disparador.

Entonces el recieve va y mira varias cosas, pero en un punto es sólo escuchar.
Entonces el tiene un objeto recibir mensaje, que le lelega la config del laberinto, y si encontró el cuadrado del laberinto envía la respuesta de que solucionó, él resuelve con el algoritmo y cuando lo encuentra (0,0) pues termina, de forma que un agente serializa el problema y lo envía, lo decodifica toma el mensaje, aplica el algoritmo (backtracking, busquedas) y al encontrar la solución envía el siguiente paso.

Dice que falta algo, la clase laberinto, en esa tiene cuadro y laberinto (le cuadrado es serializable, es una interfaz que permite serializar un objeto en java, lo que llegue lo pone en el laberinto), el Laberinto tiene lo que es pura recursión en los switch-case, si lo encontró pues mira el proceso de imprimir la solución y listo.

Entonces decía que había un DF (Dir Facilitador) y dice que se encarga de resolver laberintos, lo registra en la plataforma como eso, un Agente que hace eso, al registrar servicios si tiene 20 agentes, cada agente que esté dice eso, que resuelve laberintos, de forma que le pregunta a los que puedan, jade registra el servicio y va y busca luego, da el listado y nos comunicamos con esos. Por ejemplo lo de DA (Agente) e interactuar. Cuando estan ocupados pues lo avisan y listo, ese coso sólo hace eso, luego si el agente resuelve el laberinto fin.
Entonces el agente dice que puede recibir mensajes le pueden llegar las cosas serializadas y listo, trabaja
Luego el laberinto debe buscar qué agentes pueden resolver el laberinto, entonces sale todo ese listado y uno se comunica con cualquiera de ellos. Luego llega el mensaje para todos o uno de ellos.

Entonces lo ejecuta y con un DO-while va
