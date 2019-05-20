# ¿Qué es el analisis de sentimientos?
Emociones - mental

## Opiniones
**Definicion:** Una opinion (regular) es una quintupla `(ei, aij, ooijkl, hk, tl)`. Una opinion comparativa contiene dos opiniones

* e: Entidad
* a: aspecto de e
* oo: orientacion de la opinion acerca del aspecto (a) de la entidad (e)
* h: opinion holder (opinador)
* t: Tiempo cuando la opinion es expresada

Dependiendo del conexto se asume que el autor de la opinion es quien escribe. Al opinador tambien se le conoce como fuente de opinion.
Hay dos tipos de opiniones: comparativas o regulares. Lac comparativas regularmente seran polaridades encontrada. Sin embargo, esto no se da siempre. Ej: Uno es bueno pero el otro es mejor.
La quintupla no es la unica forma de expresar opiniones pero ayuda a tener una opinion completa

### Opiniones regulares

* Opinion directa: "La calidad de voz de este telefono es fabulosa"
* Opinion indirecta: "Despues de tomar esta medicina, mi mano se sintio mucho mejor" Se sabe positiva esta opinion por que la mejora de la mano es algo deseable.

## Entidad
Una entidad es un conjunto `{GENERAL, Ai}` y a su vez el aspecto A se compone como `{ai1, ai2, ..., ain}`
Entonces en un documento se tiene un conjunto finito de opinadores que opinan sobre entidades y por tanto sobre los aspectos de dichas entidades.
La tarea encontrar las opiniones emitidas. No interesa saber sobre lo que no se opino.
Se requiere completar las siguientes tareas:

1. *(extraccion de entidades y agrupamiento)* Extraer todas las entidades en el documento, y agrupar los sinonimos de las entidades en clusters. Cada cluster de expresion de entidades sera una unica opinion
2. (*extraccion de aspectos y agrupamientos) *Para cada aspecto de las entidades se quiere saber como dichos aspectos aparecen en el documento y a que entidad perteneces. Igualmente agrupamiento por sinonimos
3. *(extraccion de opinadores y tiempo) *Extraer a los opinadores y el tiempo de las opiniones
4. *(clasificacion del sentimiento de aspectos)* Determinar, para cada opinion, si tiene aspectos positivos, negativos o neutrales
5. *(generacion de quintuplas de opinion) *Producir todas las quintuplas de opiniones `()` expresadas en el documento.

A este conjunto de tareas se les conoce como un problema **NLP complete**
