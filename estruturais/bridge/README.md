
# Bridge

O padrão bridge preza pela composição em vez da herança. O objetivo desse padrão é dissociar uma abstração de sua implementação para que os dois possam variar independentemente.

## Quando usar?

Para entender quando devemos utilizar o padrão bridge, vejamos o seguinte exemplo (implementado no código):

Suponha que temos um site com diferentes páginas e você deve proporcionar ao usuário a opção de mudar o tema do site. Uma ideia básica seria criar várias cópias de cada página com cada opção de tema, mas assim as duas hierarquias ficam correlacionadas (as páginas e os temas) e se um ou outro for alterado será preciso atualizar em todos os lugares.

O padrão `bridge` nos permite resolver esse problema com certa elegância. Podemos criar hierarquias independentes para as páginas e para os temas e então simplesmente compor elas, neste caso, carregando o tema para cada página.
