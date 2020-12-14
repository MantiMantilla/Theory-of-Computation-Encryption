# Diffie - Hellman: Ilustración

## Motivación

Con el advenimiento de la criptografía de llave pública, resultaba imperativo el desarrollo de un sistema robusto para establecer un canal de comunicación seguro. Procedimientos anteriores bajo la premisa de llaves privadas requerían convenir un intercambio presencial o vulnerable y expuesto de llaves para encriptar y desencriptar el contenido de los mensajes del canal establecido. Los primeros sistemas de criptografía de llave pública como el knapsack contemplan un procedimiento de generación de llaves que en su momento parecía robusto pero que, según el trabajo de los creadores del RSA, es suceptible a ataques altamente eficientes que permiten calcular las claves privadas en tiempo polinomial.

El knapsack, como sistema de encripción, presenta procedimientos para cada etapa y ciclo de un canal de comunicación. Una vez establecidas las claves, puede establecerse la comunicación encriptando mensajes, liberandolos y desencriptandolos en su destino. Aunque existen posibles vulnerabilidades en cada etapa, nosotros nos enfocaremos por ahora en el procedimiento para la generación e intercambio de claves, Diffie-Hellman. Sistemas robustos de encripción como el RSA apalancan su funcionamiento desde el procedimiento descrito a continuación.


<!-- #region -->
## Primeros conceptos

Seguiremos el ejemplo clásico de Alice y Bob. Estos dos personajes deben compartir mensajes el uno con el otro de forma secreta, es decir, sin que algún tercero pueda conocer e interpretar el contenido de los mensajes aún si sabe que existe el canal de comunicación. Como antes mencionado, el procedimiento Diffie Helman permite generar llaves con las cuales encriptar o desencriptar mensajes. Por lo pronto estudiaremos el proceso para alcanzar este *secreto compartido*.

### Idea general

La comunicación en secreto, según su descripción inicial, puede describirse por la siguiente secuencia de pasos (Suponga un escenario donde Alice quiere enviar un mensaje a Bob):

1. Alice tiene un mensaje que quiere enviar a Bob.

2. Independiente de como convenieron un secreto compartido, Alice utiliza el secreto para encriptar el mensaje.

3. Alice publica su cifrado en la red con Bob como destinatario (Aunque cualquiera podría interceptarlo).

4. Bob utiliza el mismo secreto compartido para desencriptar el cifrado y leerlo.

Estos pasos describen la comunicación entre dos partes simétrica. Veamos ahora su contraparte asimétrica.

1. Alice tiene un mensaje que quiere enviar a Bob.

2. Alice conoce la llave pública (accesible por todo interesado) de Bob y encripta su mensaje con la llave.

3. El cifrado solo puede desencriptarse con la llave privada de Bob. Las claves existen en pares, siendo la versión pública del destinatario la que se usa para encriptar el mensaje y la privada para desencriptarlo.

3. Alice publica su cifrado en la red con Bob como destinatario (Aunque cualquiera podría interceptarlo).

4. Bob, como unico conocedor de su llave privada, desencripta y lee el mensaje original de Alice.

Este procedimiento es suceptible a vulnerabilidades que estudiaremos con más detalle pronto. Note que hasta ahora Alice y bob no comparten información más allá del mensaje encriptado y la clave para encriptar. El valor de este procedimiento está en que idealmente la clave privada es desconocida por todos menos por el destinatario. En teoría, siempre podría establecerse un canal de comunicación por encripción asimétrica. En práctica, para que el cifrado con una llave pública sea seguro debe hacerse con claves que exigen un alto costo computacional. En su lugar, sería preferible establecer un canal de comunicación por encripción simétrica. Tenemos entonces el siguiente escenario.


````{margin}
```{admonition} Nota
Tecnologías como la criptografía de curva elíptica vuelven el intercambio asimétrico más factible, aunque no lo contemplamos en nuestra investigación.
```
````

````{margin}
```{admonition} Nota
Una red pública no necesariamente se refiera al contexto digital. Estos procedimientos son valiosos bajo cualquier contexto donde la comunicación entre partes es vulnerable a terceros.
```
````

Alice y Bob pertenecen a una red pública y quieren comunicarse de manera privada. Pueden establecer cada vez su canal por encripción asimétrica, pero esto es altamente ineficiente. Pueden también establecer un canal de comunicación simétrico, pero para este deben ya compartir una clave con la que encriptar y desencriptar mensajes y convenir una en una red pública es altamente riesgoso. Un escenario ideal sería en el que Alice y Bob pudieran convenir una clave o *secreto compartido* sin que los otros miembros de la red se enteren para poder comunicarse con encripción simétrica.

### Compromiso

En 1976 Whitfield Diffie y Martin Hellman publicaron un método que permite establecer un *secreto compartido* entre dos partes para habilitar un canal de comunicación eficiente. El objetivo es generar una llave privada conocida por ambas partes de forma que puedan de forma eficiente encriptar y desencriptar de forma simetrica la información que se comparten. Las ineficiencias de la criptografía asimétrica son evidentes si el objetivo es compartir muchos mensajes extensos, pero para un paso sencillo, como compartir una llave de incripción simétrica, resulta atractiva la comunicación asimétrica.

En terminos generales, el protocolo de intercambio de llaves Diffie-Hellman establece una instancia de un canal de comunicación asimétrica para compartir información entre dos partes en una única ocasión para esa sesión (Luego veremos que restringir una sesión a un único mensaje puede ser atractivo). En esta instancia, las partes generan una llave simétrica a partir de sus claves privadas y públicas, conocida solo por ellos, para luego establecer un canal de comunicación simétrico, descifrable solo por los dos con una misma llave compartida.
<!-- #endregion -->

## Protocolo

Veamos de forma ilustrativa el protocolo en acción. Entraremos en detalle de los aspectos matemáticos en la siguiente página.
Se dijo con anterioridad, que el algoritmo Diffie-Hellman inicia una instancia de comunicación asimétrica, pero esta es distinta a lo que ya describimos.

1. En lugar de Alice y Bob definir una llave pública y una llave privada respectivamente, solo nos interesa que definan su llave privada y que acuerden entre sí, expuesto al público, dos valores $g$ y $p$.

Note en la animación que a cada parte le corresponde un espacio privado (seguro para los secretos) y comparten un espacio público disponible para ellos y cualquier tercero.






## Vulnerabilidades

### Ataque de intermediario
