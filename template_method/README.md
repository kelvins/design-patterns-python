
# Template Method

Ao utilizar este padrão, criamos classes abstratas para abstrair métodos em comum entre diversas classes. Devemos utilizar o decorator `@abstractmethod` para obrigar as classes filhas a implementar os métodos abstratos.

Para utilizar classes abstratas em Python é preciso importar o módulo ABC:

```python
from abc import ABCMeta, abstractmethod
```

## Quando usar?

Toda vez que temos uma estrutura semelhante que queremos aproveitar no código, podemos aplicar o padrão de projeto Template Method.

> Com ele conseguimos definir em um nível mais macro a estrutura do algoritmo, deixando "buracos" que serão implementados de maneira diferente por cada uma das implementações específicas.

Assim, reutilizamos o código ao invés de repeti-lo, facilitando a manutenção e futuras alterações, uma vez que cada classe tem sua responsabilidade bem separada.