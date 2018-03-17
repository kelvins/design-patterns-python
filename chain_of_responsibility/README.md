
# Chain of Responsibility

O padrão de projeto Chain of Responsibility nos permite aplicar uma lógica sequencial de forma dinâmica. Utilizando este padrão podemos deixar de usar diversos IFs e ELSEs por uma cadeia de classes que serão executadas em sequência. Isso facilita bastante a manutenção do código.

> A ideia do padrão é resolver problemas como esses: de acordo com o cenário, devemos realizar alguma ação. Ao invés de escrevermos código procedural, e deixarmos um único método descobrir o que deve ser feito, quebramos essas responsabilidades em várias diferentes classes, e as unimos como uma corrente.

## Quando usar?

> O padrão Chain of Responsibility cai como uma luva quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição. Nesses casos, o Chain of Responsibility nos possibilita a separação de responsabilidades em classes pequenas e enxutas, e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos novamente.

## Desvantagens

Os padrões Strategy e Chain of Responsibility, assim como outros, separam melhor as responsabilidades e deixam o código mais flexível porém, introduzem uma indireção, delegando o trabalho a outras classes, tornando o código mais complexo e consequentemente mais difícil de compreender. 

