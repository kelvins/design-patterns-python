
# Observer

O padrão observer nos permite passar uma lista de observadores, interessados pela criação de um objeto, para uma classe, e iterar sobre ela para rodar todos os observadores.

Assim, caso tenhamos um novo observador, basta incluí-lo na lista de observadores.

## Quando usar?

> Quando o acoplamento da nossa classe está crescendo, ou quando temos diversas ações diferentes a serem executadas após um determinado processo. Nestes casos, podemos implementar o Observer.

> Ele permite que diversas ações sejam executadas de forma transparente à classe principal, reduzindo o acoplamento entre essas ações, facilitando a manutenção e evolução do código.
