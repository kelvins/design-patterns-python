
# Proxy

O Proxy serve de intermediário entre o solicitante (_seeker_) e o provedor (_provider_). O solicitante é quem faz a requisição e o provedor entrega os recursos em resposta à requisição.

O Proxy é basicamente um _wrapper_ ou um objeto agente que encapsula o objeto que está realmente servindo.

## Quando usar?

Quando possuímos procedimentos complexos e precisamos fornecer uma interface simples para eles. Também pode ser utilizado para fornecer uma camada de segurança aos objetos. Pode também oferecer uma interface local para objetos remotos em servidores diferentes.

## Diferença entre o Proxy e o Facade

|                                             Proxy                                            |                            Facade                            |
|:--------------------------------------------------------------------------------------------:|:------------------------------------------------------------:|
| Oferece um substituto ou um placeholder para outro objeto a fim de controlar o acesso a ele. | Oferece uma interface para subsistemas grande de classes.    |
| Um objeto Proxy tem a mesma interface do objeto-alvo e armazena referências a esses objetos. | Minimiza a comunicação e as dependências entre subsistemas.  |
| Atua como um intermediário entre o cliente e o objeto encapsulado.                           | Um objeto Facade oferece uma interface única e simplificada. |