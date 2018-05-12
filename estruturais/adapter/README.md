
# Adapter

O padrão adapter é um design pattern de software que permite a interface de uma classe existente ser utilizada como uma outra interface.

Este padrão permite embrulhar algum objeto incompatível em um adaptador para torna-lo compatível com outras classes.

## Quando usar?

Quando precisamos que uma classe existente funcione com outras classes sem modificar seu código fonte.

## Exemplo

Suponha que temos um jogo onde existe um caçador de leões.

Neste caso, temos uma classe base Lion que implementa o método rugido (roar) e é herdada pelas outras classes relacionadas a leões.

Porém, agora temos um novo animal, um cão selvagem. Neste caso, o cão não tem rugido (roar) e sim latido (bark). Sendo assim, precisamos criar um adaptador que herde de Lion mas que chame o método latido em vez de rugido.
 
Para facilitar o entendimento, veja o exemplo de código em Python.
