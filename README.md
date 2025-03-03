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
A entrada dos dados é feito através de uma API, por motivos de eficiência na comunicação do usuário ao sistema, além de abrir portas para integrações e automações com mais facilidade.

O sistema recebe os seguintes dados de entrada:

```json
{
    "land": {
        "height": 5,
        "width": 5
    },
    "probes": [
        {
            "x": 1,
            "y": 2,
            "direction": "N",
            "command": "LMLMLMLMM"
        },
        {
            "x": 3,
            "y": 3,
            "direction": "E",
            "command": "MMRMMRMRRM"
        }
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

Para rodar todos os testes:
```sh
pytest
```

Para rodar um arquivo específico de teste:
```sh
pytest tests/test_land.py
```

## Debugging

Foi utilizado, para esse projeto, o debugging python padrão do VsCode. Breakpoints para melhor análise e entendimento nos casos de erros.

## CI/CD

Um pipeline foi configurado via GitHub Actions para rodar os testes automaticamente em cada push. Para acessar os logs, acesse a aba actions do repositório, clique no teste desejado e nos logs, na aba 'Upload test results' vai ter o link para download do arquivo report.xml contendo os logs do pytest

## Link da playlist da gravação do desenvolvimento do projeto

https://www.youtube.com/playlist?list=PLVmDe8Y2NmfDHhPB-bkLLB1HpA9dg6-vp

## Link do projeto rodando como web service na plataforma Railway

https://niucodesafio-production.up.railway.app/docs

## Autor

- **Guilheme Canato** - [GitHub](https://github.com/GuilhermeCanato)
