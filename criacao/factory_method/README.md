
# Factory Method

- Expõe um método ao cliente para criar os objetos.
- Usa herança e subclasses para definir o objeto a ser criado.
- O Factory Method é usado para criar um produto.

## Quando usar?

Podemos usar o padrão factory method quando precisamos criar um mesmo objeto em diversos lugares do código, por exemplo, criar um perfil de usuário em diversas classes.

## Diferença entre o Factory Method e o Builder

O builder nos auxilia na criação de um objeto mas estamos no controle, podemos criar um objeto de diversas formas.
Já o padrão factory, nos dá um objeto pronto, com os parâmetros já definidos.