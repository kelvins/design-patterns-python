# Padrão Strategy

Ao utilizar este padrão podemos passar como parâmetro uma função, ou melhor, uma estratégia, para outro método.

Isso permite remover vários comandos condicionais, uma vez que não precisamos verificar manualmente qual foi a estratégia passada como parâmetro.

**Nota**: diferença entre função e método: um método pertence a uma classe e uma função não pertence necessariamente a uma classe.

**Duck typing**: é um estilo de tipagem em que os métodos e propriedades de um objeto determinam a semântica válida, em vez de sua herança de uma classe particular ou implementação de uma interface explicita. Não importa a instância que passamos, contanto que ela tenha o método `calcula`.

## Quando usar?

> O padrão Strategy é muito útil quando temos um conjunto de algoritmos similares, e precisamos alternar entre eles em diferentes pedaços da aplicação. O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos diferentes, e de passar esses algoritmos para classes clientes que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado, e apenas manda o algoritmo rodar. Isso faz com que o código da classe cliente fique bastante desacoplado das implementações dos algoritmos, possibilitando assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem precisar alterar o seu código.