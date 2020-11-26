# Chocolatería Solución

<sup><b><i style="font-size:13px">Tags: </i></b><i style="font-size:11px">Introducción, Dos variables</i></sup>

## Enunciado

La chocolatería Perla Caribe es un pequeño emprendimiento que fabrica y comercializa chocolates artesanales con cacao de distintas variedades comprado directamente a agricultores locales. Actualmente producen dos tipos de chocolates: chocolate oscuro y chocolate blanco. Una unidad de cualquier tipo de chocolate pesa 60g. Una unidad de chocolate oscuro se vende a 7,000 COP y una unidad de chocolate blanco se vende a 6,000 COP. Los costos asociados a materia prima, mano de obra y demás costos operacionales equivalen a 3,500 COP por cada unidad de chocolate oscuro y 2,000 COP por cada unidad de chocolate blanco.

La producción de estos chocolates requiere de dos ingredientes en común: manteca de cacao y azúcar. Por cada unidad de chocolate oscuro se requiere 6g de manteca de cacao y 21 g de azúcar. Por cada unidad de chocolate blanco se requiere 22g de manteca de cacao y 18g de azúcar. Cada semana, la chocolatería Perla Caribe tiene disponible 12kg de manteca de cacao y 20kg de azúcar. La demanda de chocolate oscuro es ilimitada, pero a lo sumo le demandan 315 unidades de chocolate blanco por semana.

La chocolatería Perla Caribe quiere maximizar su utilidad (ingresos menos costos). Formule un modelo matemático que represente la situación y que les permita cumplir con su objetivo.

## Formulación

**a.** Escriba término a término la(s) variable(s) de decisión que utilizará en el modelo.

\begin{align*}
    x_1: \text{unidades de chocolate oscuro producidos cada semana} \\
    x_2: \text{unidades de chocolate blanco producidos cada semana}
\end{align*}

**b.** Escriba término a término la(s) restricción(es) lineal(es) y descríbala(s)

Restricciones asociadas a la disponibilidad de recursos:

\begin{align*}
    6x_1 + 22x_2 \leq 12,000\\
    21x_1 + 18x_2 \leq 20,000
\end{align*}

Restricciones asociadas a la demanda de productos:

\begin{align*}
    x_1 \leq 10,000
\end{align*}


Restricciones asociadas a tipo de variables:

\begin{align*}
    x_1 \geq 0\\
    x_2 \geq 0
\end{align*}

**c.** Escriba término a término la función objetivo que maximiza la utilidad.

$$
    \text{maximizar} (\$7,000 - \$3,500)x_1 + (\$6,000-\$2,000)x_2
$$

## Formulación matemática

**Variables de decisión:**

$x_1$: unidades de chocolate oscuro producidos cada semana


$x_2$: unidades de chocolate blanco producidos cada semana

**Modelo:**

$$
    \text{maximizar }  \$3,500x_1 + \$4,000x_2 \text{ (1)}
$$

Sujeto a,

\begin{align*}
    6x_1 + 22x_2 &\leq 12,000; &(2)\\
    21x_1 + 18x_2 &\leq 20,000; &(3)\\
    x_2 &\leq 10,000; &(4)\\
    x_1 &\geq 0; &(5)\\
    x_2 & \geq 0. &(6)
\end{align*}

La función objetivo (1) maximiza las utilidades. Las restricciones (2) y (3) describen que se debe respetar la disponibilidad de manteca de cacao y azúcar, respectivamente. La restricción (4) garantiza no se sobrepase la demanda máxima de chocolate blanco. La restricciones (5) y (6) describen la naturaleza de la variables $x_1$ y $x_2$, respectivamente. 

## Implementación

**d.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución óptima del problema?

```{code-cell} ipython3
:class: thebe

import numpy as np
np.random.seed(1337)
data = np.random.randn(2, 100)
print(data[1, :10])
```

```{thebe-button} Correr el código
```

## Créditos

Equipo Principios de Optimización<br>
Instancia: Alfaima Solano<br>
Fecha: 30/09/2020