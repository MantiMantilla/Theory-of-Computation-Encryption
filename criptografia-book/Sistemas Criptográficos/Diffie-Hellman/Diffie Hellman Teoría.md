<!-- #region -->
# Teoría

## Motivación

En la página anterior describimos el protocolo de intercambio de llaves en terminos generales y simplificados. Acciones como 'mezclar' las claves, encriptar un mensaje o asegurar que el público no tiene acceso a ciertos valores sea porque son privados o porque son muy dificiles de calcular son todas afirmaciones acertadas pero peligrosamente generales. Esta página busca elaborar con formalidad acerca de los procedimientos matemáticos, teoremas y demás abstracciones antes mencionadas.

Suponemos un ligero entendimiento de matemática discreta y algebra para desarrollar expresiones de lógica.


## El algoritmo

En la página anterior estudiamos el paso a paso del algoritmo sin pensar mucho en como generamos los valores mencionados. Vamos paso por paso estudiando los valores necesarios.

1. Alice tiene un mensaje que quiere enviar a Bob.

Nada fuera de lo usual acá. Es tan solo la motivación detras los siguientes pasos.

2. Alice y Bob concuerdan en un valor generador $g$ y un módulo $p$ para publicar.



3. Alice publica su cifrado en la red con Bob como destinatario (Aunque cualquiera podría interceptarlo).

4. Bob utiliza el mismo secreto compartido para desencriptar el cifrado y leerlo.

Estos pasos describen la comunicación entre dos partes simétrica. Veamos ahora su contraparte asimétrica.

1. Alice tiene un mensaje que quiere enviar a Bob.

2. Alice conoce la llave pública (accesible por todo interesado) de Bob y encripta su mensaje con la llave.

3. El cifrado solo puede desencriptarse con la llave privada de Bob. Las claves existen en pares, siendo la versión pública del destinatario la que se usa para encriptar el mensaje y la privada para desencriptarlo.

3. Alice publica su cifrado en la red con Bob como destinatario (Aunque cualquiera podría interceptarlo).

4. Bob, como único conocedor de su llave privada, desencripta y lee el mensaje original de Alice.


## Demostraciones


## Conclusiones
<!-- #endregion -->
