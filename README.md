# Desafio Niuco 2025 - Explorando Marte

## Descrição

Este repositório contém a implementação do desafio "Explorando Marte", proposto pela Niuco. O objetivo é simular o controle de sondas enviadas a Marte, garantindo que elas se movimentem corretamente dentro de um planalto retangular e evitando colisões entre si.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: FastAPI
- **Testes**: PyTest
- **Padrões de Projeto**: Factory, Command e Strategy
- **CI/CD**: GitHub Actions

## Como Executar o Projeto

### Requisitos

- Python 3.9+
- Pip

### Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/GuilhermeCanato/Niuco_desafio.git
   cd Niuco_desafio
   ```
3. Ative a venv (opcional)
   ```sh
   Scripts/activate
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```sh
   fastapi dev main.py
   ```
4. Acesse o link disponibilizado no terminal
    ```sh
   http://127.0.0.1:8000/docs
   ```
   
## Como Funciona

O sistema recebe os seguintes dados de entrada:

```json
{
  "altura_planalto": 5,
  "largura_planalto": 5,
  "sondas": [
    { "x": 1, "y": 2, "direcao": "N", "comandos": "LMLMLMLMM" },
    { "x": 3, "y": 3, "direcao": "E", "comandos": "MMRMMRMRRM" }
  ]
}
```

E retorna a posição final de cada sonda após executar os comandos:

```json
[
  { "x": 1, "y": 3, "direcao": "N" },
  { "x": 5, "y": 1, "direcao": "E" }
]
```

## Padrões de Projeto

### Factory Pattern
Utilizado para criar objetos das sondas de forma padronizada.

### Command Pattern
Cada comando (L, R, M) é tratado como um objeto de comando, facilitando a extensibilidade.

### Strategy Pattern
Utilizado para determinar a lógica de movimento baseado na direção atual da sonda.

## Testes

Os testes unitários cobrem:
- Movimentação e mudança de direção
- Respeito aos limites do planalto
- Colisões entre sondas
- Casos de erro e exceções

Para rodar os testes:
```sh
pytest
```

## Debugging

Para debugar o código no VSCode:
1. Defina breakpoints no código.
2. Configure o `launch.json` para Python.
3. Rode o debugger passo a passo.

## CI/CD

Um pipeline foi configurado via GitHub Actions para rodar os testes automaticamente em cada push. 

## Link da playlist do youtube com a gravação do desenvolvimento do projeto

https://www.youtube.com/playlist?list=PLVmDe8Y2NmfDHhPB-bkLLB1HpA9dg6-vp

## Autor

- **Guilheme Canato** - [GitHub](https://github.com/GuilhermeCanato)
