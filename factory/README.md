
# Factory

Faz sentido utilizar o padrão factory quando precisamos criar um objeto de alguma classe com os mesmos parâmetros, por exemplo a conexão com uma base de dados.

**Nota**: no exemplo o código não compila, é para entender o conceito.

## Quando usar?

Podemos usar o padrão factory quando precisamos criar um mesmo objeto em diversos lugares do código, por exemplo, criar uma conexão com o banco de dados em diversas classes.

## Diferença entre o Factory e o Builder

O builder nos auxilia na criação de um objeto mas estamos no controle, podemos criar um objeto de diversas formas.
Já o padrão factory, nos dá um objeto pronto, com os parâmetros já definidos.