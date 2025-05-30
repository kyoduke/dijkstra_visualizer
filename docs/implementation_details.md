# Detalhes de Implementação

Este documento descreve a implementação técnica do Visualizador do Algoritmo de Dijkstra.

## Estrutura do Código

A aplicação está organizada da seguinte forma:

- **Componentes Principais**:
  - Representação da Grade e do Nó
  - Implementação do algoritmo de Dijkstra
  - Componentes de visualização e interface do usuário
  - Tratamento de eventos

## Classes Principais

### Classe Node

A classe `Node` representa cada célula na grade e contém:

- Informações de posição (linha, coluna)
- Coordenadas em pixels (x, y)
- Estado da cor (representando diferentes estados durante a visualização)
- Nós vizinhos
- Métodos para mudar estados (make_start, make_end, make_barrier, etc.)
- Métodos para verificar estados (is_start, is_end, is_barrier, etc.)

```python
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
```

### Classe Button

A classe `Button` fornece controles de interface do usuário:

- Posição e tamanho
- Conteúdo de texto
- Estados de cor (normal e hover)
- Métodos para desenhar e detectar interações

```python
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.current_color = color
        self.font = pygame.font.SysFont('arial', 16)
```

## Implementação do Algoritmo

O algoritmo de Dijkstra é implementado na função `dijkstra()` com estes componentes principais:

1. **Fila de Prioridade**: Mantém os nós a visitar ordenados pela distância atual
2. **Dicionário de Distâncias**: Acompanha a menor distância atual para cada nó
3. **Dicionário "Veio De"**: Registra o caminho para reconstrução
4. **Atualizações de Visualização**: Atualiza a exibição durante a execução do algoritmo

O algoritmo é executado até que:
- O nó final seja encontrado (sucesso)
- A fila seja esvaziada sem encontrar o nó final (não existe caminho)

## Mecânica de Visualização

A visualização funciona através de:

1. **Codificação por Cores**:
   - Branco: Nós não visitados
   - Verde: Nós na fila (fronteira)
   - Vermelho: Nós visitados
   - Amarelo: Caminho final
   - Preto: Barreiras
   - Laranja: Nó inicial
   - Turquesa: Nó final

2. **Atualizações em Tempo Real**:
   - A função `draw()` atualiza a exibição após cada etapa do algoritmo
   - As cores dos nós mudam para refletir o estado atual do algoritmo

## Interação do Usuário

As interações do usuário são tratadas através de:

1. **Loop de Eventos**:
   - O sistema de eventos do Pygame processa entradas de mouse e teclado
   - Cliques em botões são detectados através de detecção de colisão
   - Interações com células da grade são gerenciadas através de cálculos de posição

2. **Ações dos Botões**:
   - Iniciar Algoritmo: Inicializa os vizinhos dos nós e executa o algoritmo de Dijkstra
   - Limpar Caminho: Reinicia nós que fazem parte do caminho, visitados ou na fronteira
   - Reiniciar Tudo: Cria uma nova grade, descartando todo o estado atual

## Considerações Técnicas

- **Desempenho**: A grade é limitada a 30x30 para um desempenho razoável
- **Simplicidade**: Todas as arestas têm peso 1 para facilitar a visualização
- **Extensibilidade**: A estrutura do código permite extensões potenciais como:
  - Diferentes algoritmos (A*, BFS, DFS)
  - Tamanhos de grade variáveis
  - Arestas com pesos

## Dependências

A aplicação requer:
- Python 3.x
- Biblioteca Pygame
- Bibliotecas Python padrão (queue, math, sys)