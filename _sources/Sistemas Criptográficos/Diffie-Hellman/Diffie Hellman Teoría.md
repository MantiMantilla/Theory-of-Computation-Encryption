# Teoría del Diffie-Hellman


En la página anterior describimos el protocolo de intercambio de llaves en terminos generales y simplificados. Acciones como 'mezclar' las claves, encriptar un mensaje o asegurar que el público no tiene acceso a ciertos valores sea porque son privados o porque son muy dificiles de calcular son todas afirmaciones acertadas, pero peligrosamente generales. Esta página busca elaborar con formalidad acerca de los procedimientos matemáticos, teoremas y demás abstracciones antes mencionadas.

Suponemos un ligero entendimiento de matemática discreta y algebra modular.


Como mencionamos anteriormente, Alice y Bob se ponen de acuerdo de manera pública en dos valores $g$ y $p$. Más específicamente, $p$ debe ser un primo muy grande y $g$ debe ser un entero positivo menor que $p$. Ahora, Alice escoge un entero positivo en privado $a$ y Bob escoge un entero positivo en privado $b$. Ambos números deben ser menores a $p$ y el número que escogió cada uno corresponde a su "clave privada". Con esta información, Alice y Bob están listos para publicar sus "claves públicas" $P_A$ y $P_B$, respectivamente, que corresponden a los números


$$P_A=g^{a}\hspace{0.5em}(\text{mod } p) \hspace{1em} \text{y} \hspace{1em} P_B=g^{b}\hspace{0.5em}(\text{mod } p).$$


Su clave compartida corresponde entonces a $K=g^{ab}$(mod $p$). Para calcularla, Alice eleva $P_B$ a la $a$ y calcula el residuo módulo $p$ y Bob eleva $P_A$ a la $b$ y calcula el residuo módulo $p$. Estas dos operaciones arrojan el mismo número $K$ por las siguientes propiedades algebráicas de la aritmética modular


$$(P_B)^{a}\equiv(g^{b})^{a}\equiv g^{ab}\equiv(g^{a})^{b}\equiv (P_A)^{b}\hspace{0.5em}(\text{mod } p).$$


La efectividad de este sistema de encriptación radica en que exponenciar y calcular residuos es un proceso que cualquier computador ejcuta de manera rápida (en tiempo polinomial). Así que tanto Alice como Bob pueden construir su "clave compartida" de manera rápida cada uno por aparte, como se menciona arriba. Ahora bien, si alguien tratase de calcular las "claves privadas" de Alice y Bob para obtener su "clave compaertida" se encontraría con el problema de calcular la soluciones $x$ y $y$ a las congruencias


$$P_A\equiv g^{x}\hspace{0.5em}(\text{mod } p) \hspace{1em} \text{y} \hspace{1em} P_B\equiv g^{y}\hspace{0.5em}(\text{mod } p).$$


Ahora bien, este problema es conocido como el problema del logaritmo discreto y es computacionalmente muy complejo, pues note que pertenece a la clase NP donde el verificador es el exponente. 
