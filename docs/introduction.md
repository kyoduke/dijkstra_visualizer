# Introdução ao Visualizador do Algoritmo de Dijkstra

## Visão Geral

Esta aplicação é uma implementação visual do algoritmo de Dijkstra projetada para simular a busca de caminhos em um ambiente de mina de carvão. Ela fornece uma plataforma interativa para entender como o algoritmo de Dijkstra funciona para encontrar o caminho mais curto entre dois pontos em uma grade, com obstáculos representando barreiras da mina.

## Propósito

O principal propósito desta ferramenta de visualização é educacional. Ela ajuda os usuários a:

1. Entender a mecânica do algoritmo de Dijkstra
2. Visualizar como o algoritmo explora um espaço
3. Ver como a busca de caminhos funciona ao redor de barreiras
4. Aprender sobre eficiência algorítmica na travessia de grafos

## Contexto

O algoritmo de Dijkstra, publicado pelo cientista da computação Edsger W. Dijkstra em 1956, é um algoritmo de busca em grafos que resolve o problema do caminho mais curto de fonte única. O algoritmo funciona através de:

1. Atribuição de valores iniciais de distância a todos os nós
2. Definição da distância do nó inicial como zero e todos os outros nós como infinito
3. Visitação do nó não visitado com a menor distância conhecida
4. Exame de cada vizinho não visitado do nó atual
5. Cálculo de suas distâncias provisórias através do nó atual
6. Comparação da distância recém-calculada com o valor atual atribuído
7. Atribuição da distância menor e atualização do caminho

No contexto da nossa visualização de mina de carvão, cada célula na grade representa uma localização na mina, e as barreiras representam áreas intransponíveis.

## Tecnologias Utilizadas

O visualizador é construído com:

- **Python**: A linguagem de programação principal
- **Pygame**: Um conjunto de módulos Python projetados para escrever jogos, fornecendo funcionalidades para gráficos e entrada do usuário

## Representação Visual

Em nossa visualização:
- A exploração do algoritmo é mostrada em tempo real
- O caminho final é destacado uma vez encontrado
- Diferentes cores representam diferentes estados dos nós durante a exploração

Esta abordagem proporciona um entendimento intuitivo de como o algoritmo de Dijkstra funciona, tornando conceitos abstratos concretos e acessíveis.