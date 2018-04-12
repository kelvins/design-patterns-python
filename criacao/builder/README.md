
# Builder

Com o design pattern builder, podemos criar uma classe builder, a qual é responsável por receber os parâmetros, verificar a validade dos parâmetros e até mesmo definir parâmetros padrões quando necessário.

A própria linguagem Python disponibiliza formas de parâmetros nomeados e parâmetros padrões, o que facilita bastante e muitas vezes elimina a necessidade da utilização do padrão builder.

## Quando usar?

> Sempre que tivermos um objeto complexo de ser criado, que possui diversos atributos, ou que possui uma lógica de criação complicada, podemos esconder tudo isso em um Builder.

> Porém, na linguagem Python, esse pattern muitas vezes é desnecessário, já que parâmetros nomeados e opcionais do construtor de classes podem muitas vezes lidar com a complexidade de criação do objeto.
