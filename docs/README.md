# Visualizador do Algoritmo de Dijkstra

Esta documentação fornece uma visão geral da aplicação Visualizador do Algoritmo de Dijkstra. Esta ferramenta visualiza o algoritmo de busca de caminhos de Dijkstra no contexto de uma mina de carvão, representada como uma grade 2D.

## Índice

1. [Introdução](introduction.md)
2. [Como Usar](how_to_use.md)
3. [Detalhes de Implementação](implementation_details.md)
4. [Explicação do Algoritmo](algorithm_explanation.md)

## Início Rápido

1. Execute a aplicação com o comando `python dijkstra_visualizer.py`
2. Leia as instruções na tela inicial e clique em "Iniciar Aplicação" para começar
3. Use o botão esquerdo do mouse para colocar:
   - Primeiro clique: Ponto de início (laranja)
   - Segundo clique: Ponto de destino (turquesa)
   - Cliques subsequentes ou arrastar: Barreiras/paredes (preto)
4. Use o botão direito do mouse para remover qualquer nó colocado
5. Clique no botão "Iniciar Algoritmo" ou pressione a Barra de Espaço para iniciar a visualização
6. Clique em "Limpar Caminho" para limpar o caminho mantendo barreiras e pontos de início/fim
7. Clique em "Reiniciar Tudo" ou pressione 'C' para reiniciar completamente a grade
8. Pressione 'Escape' para retornar à tela inicial

## Legenda de Cores

- **Laranja**: Ponto de início
- **Turquesa**: Ponto de destino
- **Preto**: Barreiras/Paredes
- **Vermelho**: Nós visitados
- **Verde**: Nós na fronteira
- **Amarelo**: Caminho final
- **Branco**: Nós não visitados

Para informações mais detalhadas, consulte os arquivos de documentação vinculados no Índice.