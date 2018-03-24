
# Command

Podemos utilizar o design pattern command quando precisamos executar uma sequência de comandos em cima de algum dado, por exemplo executar uma sequência de ações em um pedido.

Para aplicar o padrão command, podemos utilizar uma classe abstrata para 'forçar' as classes filhas a implementar um método comum.

## Quando usar?

Quando temos uma fila de dados para processar e precisamos ter uma 'conexão forte' com alguma operação que será utilizada sobre ele, utilizamos o padrão de projeto command.

## Diferença do Command para o Strategy

> A ideia do Command é abstrair um comando que deve ser executado, pois não é possível executá-lo naquele momento (pois precisamos por em uma fila ou coisa do tipo). Já no Strategy, a ideia é que você tenha uma estratégia (um algoritmo) para resolver um problema.