# :computer: Padrões de Projeto em Python

Material de estudo sobre padrões de projeto em Python com código, descrição e em pt-br :brazil:

|                       | Padrões Comportamentais       | Se concentram nos algoritmos e atribuições de responsabilidades          |
|-----------------------|-------------------------------|--------------------------------------------------------------------------|
| [:link:][1]           | [Chain of Responsibility][25] | Nos permite aplicar uma lógica sequencial de forma dinâmica              |
| [:cop:][2]            | [Command][26]                 | Executa uma sequência de comandos em cima de algum dado                  |
| [:speech_balloon:][3] | [Interpreter][27]             | Quando precisamos interpretar diversas operações                         |
| [:loop:][4]           | [Iterator][28]                | Uma maneira de acessar elementos de um objeto sem expor o conteúdo       |
| [:alien:][5]          | [Mediator][29]                | Encapsula a lógica de comunicação entre um conjunto de objetos           |
| [:floppy_disk:][6]    | [Memento][30]                 | Guardar um estado que possa ser restaurado futuramente                   |
| [:sunglasses:][7]     | [Observer][31]                | Criar uma lista de observadores interessados pela criação de um objeto   |
| [:anger:][8]          | [State][32]                   | Define um conjunto de estados e os mesmos possuem uma ordem definida     |
| [:bulb:][9]           | [Strategy][33]                | Passa como parâmetro uma função (estratégia) para outro método           |
| [:ledger:][10]        | [Template Method][34]         | Classes abstratas para abstrair métodos em comum entre diversas classes  |
| [:runner:][11]        | [Visitor][35]                 | Permite navegar pelos elementos de uma estrutura de dados                |

|                             | Padrões de Criação     | São aqueles que abstraem ou adiam o processo de criação dos objetos               |
|-----------------------------|------------------------|-----------------------------------------------------------------------------------|
| [:hammer:][12]              | [Abstract Factory][36] | Cria um ou mais métodos de fábrica para criar uma família de objetos relacionados |
| [:construction_worker:][13] | [Builder][37]          | Recebe parâmetros, verifica a validade e até definir parâmetros padrões           |
| [:factory:][14]             | [Factory Method][38]   | Permite expor métodos ao cliente para criar novos objetos                         |
| :one:                       | [Monostate (Borg)][39] | Cria mais de uma instância da classe mas todos os objetos tem o mesmo estado      |
| [:sheep:][16]               | [Prototype][40]        | O padrão prototype é um padrão utilizado basicamente para clonar objetos          |
| [:gem:][17]                 | [Singleton][41]        | Garante que apenas um objeto de uma determinada classe seja criado                |

|                        | Padrões Estruturais | Se preocupam com a forma como classes e objetos são compostos                  |
|------------------------|---------------------|--------------------------------------------------------------------------------|
| [:electric_plug:][18]  | [Adapter][42]       | Embrulha um objeto em um adapter para torná-lo compatível com outras classes   |
| [:aerial_tramway:][19] | [Bridge][43]        | Dissocia uma abstração de sua implementação para que possam variar             |
| [:herb:][20]           | [Composite][44]     | Permite tratar objetos individuais de forma uniforme                           |
| [:art:][21]            | [Decorator][45]     | Permite compor/decorar os parâmetros de forma dinâmica                         |
| [:package:][22]        | [Facade][46]        | Promove o desacoplamento da implementação com vários clientes                  |
| [:leaves:][23]         | [Flyweight][47]     | Minimiza o uso de custos computacionais compartilhando dados entre objetos     |
| [:8ball:][24]          | [Proxy][48]         | Um objeto agente que encapsula o objeto que está realmente servindo            |

## :dancers: Contribuindo

Se você tem interesse em contribuir com o projeto :heart_eyes: por favor leia o documento [CONTRIBUTING](https://github.com/kelvins/design-patterns-python/blob/master/CONTRIBUTING.md).

## :book: Referências

- [Curso Design Patterns Python I: Boas práticas de programação. Alura Online.](https://cursos.alura.com.br/course/design-patterns-python)
- [Curso Design Patterns Python II: Boas práticas de programação. Alura Online.](https://cursos.alura.com.br/course/design-patterns-python-2)
- [Aprendendo Padrões de Projeto em Python. Chetan Giridhar. Novatec.](https://novatec.com.br/livros/padroes-projeto-python/)
- [Design Patterns for Humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [Design Patterns: Refactoring Guru](https://refactoring.guru/design-patterns/python)
- [Padrões de Projeto de Software](https://pt.wikipedia.org/wiki/Padr%C3%A3o_de_projeto_de_software)

[1]: https://pt.wikipedia.org/wiki/Chain_of_Responsibility
[2]: https://pt.wikipedia.org/wiki/Command
[3]: https://pt.wikipedia.org/wiki/Interpreter
[4]: https://pt.wikipedia.org/wiki/Iterador
[5]: https://pt.wikipedia.org/wiki/Mediator
[6]: https://pt.wikipedia.org/wiki/Memento_(inform%C3%A1tica)
[7]: https://pt.wikipedia.org/wiki/Observer
[8]: https://pt.wikipedia.org/wiki/State
[9]: https://pt.wikipedia.org/wiki/Strategy
[10]: https://pt.wikipedia.org/wiki/Template_Method
[11]: https://pt.wikipedia.org/wiki/Visitor_Pattern
[12]: https://pt.wikipedia.org/wiki/Abstract_Factory
[13]: https://pt.wikipedia.org/wiki/Builder
[14]: https://pt.wikipedia.org/wiki/Factory_Method
[16]: https://pt.wikipedia.org/wiki/Prototype
[17]: https://pt.wikipedia.org/wiki/Singleton
[18]: https://pt.wikipedia.org/wiki/Adapter
[19]: https://pt.wikipedia.org/wiki/Bridge_(padr%C3%A3o_de_projeto_de_software)
[20]: https://pt.wikipedia.org/wiki/Composite
[21]: https://pt.wikipedia.org/wiki/Decorator
[22]: https://pt.wikipedia.org/wiki/Fa%C3%A7ade
[23]: https://pt.wikipedia.org/wiki/Flyweight
[24]: https://pt.wikipedia.org/wiki/Proxy_(padr%C3%B5es_de_projeto)

[25]: comportamentais/chain_of_responsibility
[26]: comportamentais/command
[27]: comportamentais/interpreter
[28]: comportamentais/iterator
[29]: comportamentais/mediator
[30]: comportamentais/memento
[31]: comportamentais/observer
[32]: comportamentais/state
[33]: comportamentais/strategy
[34]: comportamentais/template_method
[35]: comportamentais/visitor
[36]: criacao/abstract_factory
[37]: criacao/builder
[38]: criacao/factory_method
[39]: criacao/monostate
[40]: criacao/prototype
[41]: criacao/singleton
[42]: estruturais/adapter
[43]: estruturais/bridge
[44]: estruturais/composite
[45]: estruturais/decorator
[46]: estruturais/facade
[47]: estruturais/flyweight
[48]: estruturais/proxy
