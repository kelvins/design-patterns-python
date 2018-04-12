
# Monostate (Borg)

Proposto por Alex Martelli, o padrão _Monostate_ também conhecido como _Borg_ é uma variação do padrão [_Singleton_](../singleton).
Alex sugere que os desenvolvedores devem se preocupar com o estado e o comportamento e não com a identidade do objeto.
Este padrão permite criar mais de uma instância (objeto) de uma classe porém todos os objetos terão o mesmo estado, se comportando assim como um _Singleton_.

## Quando usar?

Quando precisamos criar apenas um objeto de uma determinada classe.
Um exemplo seria quando precisamos de apenas um objeto para conexão com o banco de dados.