# Prueba de Entrada
Nombre: Diego Sebastian Quispe Amao
Codigo: 20202222I

## Implementación
Para esta primera parte vamos a definir una funcion Dijkstra la cual va a necesitar dos parametros, una variable *Grafo* y una variable *salida*.

Para este caso la variable *Grafo* tendra a los vertices y cada uno va a tener las conexiones que tiene con cada uno de ellos (incluido los pesos).

Entonces para esta primera etapa la lógica del algoritmo vamos a establecer la funcion *algoritmoDijkstra*

Para este caso, la variable salida lo que va a significar sera el grafo en el cual queremos encontrar el camino minimo a cada uno de los otros vertices.

# Optimización
Teniendo en cuenta que usualmente podemos tener grafos muy grandes y pesados, no es tan optimo tener la lista de cada uno por nodo, mejor es hacer un recorrido solamente para los dos vertices donde necesitamos el peso minimo. Entonces la siguiente entrega va a tratar de implementar esto ya teniendo la lógica de la implementación *general*

# Documentación
Se termino con la documentación y una pequeña optimización del codigo (ha sido muy simple), pero entiendo que ha sido un gran impacto a nivel de complejidad por que no se termina de leer todos los vertices
