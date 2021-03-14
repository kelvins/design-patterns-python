
# Decorator

Ao utilizar o design pattern decorator, podemos compor/decorar os parâmetros de forma dinâmica. Neste exemplo, podemos compor múltiplos impostos em um mesmo orçamento apenas passando um imposto para o construtor do anterior.

## Quando usar?

> Sempre que percebemos que temos comportamentos que podem ser formados por comportamentos de outras classes envolvidas em uma mesma hierarquia, como foi o caso dos impostos, que podem ser composto por outros impostos. O Decorator introduz a flexibilidade na composição desses comportamentos, bastando escolher no momento da instanciação, quais instancias serão utilizadas para realizar o trabalho.

## Decorator do Python

Ao utilizar o recurso de decorator da linguagem Python, podemos chamar outra função ou método (neste caso o wrapper do IPVX) antes de executar uma função ou método, e assim compor os resultados.

```python
def IPVX(metodo_ou_funcao):
    # Chama o calculo do imposto ISS, pega o resultado e soma com R$ 50,00
    # O wrapper eh chamado antes do calcula do ISS
    # Recebe o self do ISS, onde o decorator esta aplicado
    # metodo_ou_funcao sera o metodo calcula
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper


class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):

        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)
```

A diferença entre o design pattern decorator e o decorator do Python é que o decorator do Python fica "fixo" no código, já o design pattern decorator, podemos compor os decorators em tempo de execução.
