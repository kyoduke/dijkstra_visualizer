# Como Usar o Visualizador do Algoritmo de Dijkstra

Este guia explica como usar efetivamente a aplicação do Visualizador do Algoritmo de Dijkstra.

## Iniciando a Aplicação

1. Certifique-se de ter Python e Pygame instalados em seu sistema
2. Execute a aplicação com o comando: `python dijkstra_visualizer.py`
3. Uma tela de boas-vindas aparecerá com uma explicação da aplicação e instruções
4. Clique no botão "Iniciar Aplicação" para prosseguir para a tela principal de visualização
5. A aplicação principal abrirá com uma grade e botões de controle na parte inferior

## Elementos da Interface

A interface consiste em:

### Tela de Boas-vindas
- Uma tela informativa de boas-vindas com:
  - Título e breve descrição
  - Instruções sobre como usar a aplicação
  - Legenda de cores explicando o que cada cor representa
  - Botão "Iniciar Aplicação" para prosseguir para a visualização principal

### Tela Principal de Visualização
- Uma área de grade representando a mina de carvão
- Três botões de controle na parte inferior:
  - **Iniciar Algoritmo**: Inicia a visualização da busca de caminho
  - **Limpar Caminho**: Remove o caminho visualizado, mas mantém barreiras e pontos de início/fim
  - **Reiniciar Tudo**: Reinicia completamente a grade para seu estado inicial

## Controles Básicos

### Controles do Mouse

- **Clique esquerdo**:
  - Primeiro clique: Coloca o ponto de início (laranja)
  - Segundo clique: Coloca o ponto de destino (turquesa)
  - Cliques subsequentes ou arrastar: Coloca barreiras/paredes (preto)
- **Clique direito**:
  - Remove qualquer nó colocado (início, fim ou barreira)

### Controles de Botões

- **Iniciar Algoritmo**: Clique para iniciar a visualização da busca de caminho (funciona apenas quando os pontos de início e fim estão colocados)
- **Limpar Caminho**: Clique para remover o caminho visualizado, mas manter barreiras e pontos de início/fim
- **Reiniciar Tudo**: Clique para reiniciar completamente a grade

### Atalhos de Teclado

- **Barra de Espaço**: Equivalente a clicar no botão "Iniciar Algoritmo"
- **Tecla C**: Equivalente a clicar no botão "Reiniciar Tudo"
- **Tecla Escape**: Retorna à tela de boas-vindas

## Guia de Uso Passo a Passo

1. **Tela de Boas-vindas**:
   - Leia as instruções e a legenda de cores para entender a aplicação
   - Clique no botão "Iniciar Aplicação" para prosseguir para a visualização principal

2. **Fase de Configuração**:
   - Clique com o botão esquerdo em qualquer lugar da grade para colocar o ponto de início (laranja)
   - Clique com o botão esquerdo em outro lugar para colocar o ponto de destino (turquesa)
   - Adicione barreiras (preto) clicando ou arrastando o mouse sobre as células restantes
   - Clique com o botão direito para remover qualquer elemento colocado se quiser fazer alterações

3. **Fase de Visualização**:
   - Clique no botão "Iniciar Algoritmo" ou pressione a Barra de Espaço
   - Observe como o algoritmo explora a grade:
     - Células verdes representam nós na fronteira (a serem explorados)
     - Células vermelhas representam nós que foram visitados
     - Quando o destino é encontrado, o caminho ótimo aparece em amarelo

4. **Revisar e Modificar**:
   - Após a conclusão da visualização, você pode:
     - Clicar em "Limpar Caminho" para remover a visualização, mas manter a configuração de barreiras
     - Clicar em "Reiniciar Tudo" para começar completamente do zero
     - Fazer modificações nas barreiras existentes (se você não limpou o caminho)
     - Pressionar Escape para retornar à tela de boas-vindas

## Dicas para Uso Efetivo

- Crie diferentes padrões de barreiras arrastando o mouse para testar o comportamento do algoritmo
- Tente colocar os pontos de início e fim em distâncias diferentes
- Observe como o algoritmo sempre encontra o caminho mais curto
- Observe como a exploração se espalha igualmente em todas as direções
- Crie labirintos com caminhos de largura de uma célula para ver comportamentos interessantes de busca de caminho

## Limitações

- O tamanho da grade é fixado em 30x30 células
- Movimento diagonal não é suportado nesta implementação
- Todos os passos têm o mesmo peso (custo de 1) nesta implementação

## Próximos Passos

Após entender a visualização básica, considere explorar os documentos [Detalhes de Implementação](implementation_details.md) e [Explicação do Algoritmo](algorithm_explanation.md) para saber mais sobre como o algoritmo de Dijkstra funciona.