# Referência Rápida: Python para Automação

## Conceitos Básicos

### Variáveis e Tipos de Dados
```python
# Strings (texto)
nome = "Maria"

# Números
idade = 30
altura = 1.65

# Booleanos
ativo = True

# Listas (coleção ordenada e mutável)
frutas = ["maçã", "banana", "laranja"]

# Dicionários (pares chave-valor)
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

# Tuplas (coleção ordenada e imutável)
coordenadas = (10, 20)

# Conjuntos (coleção não ordenada sem duplicatas)
cores = {"vermelho", "verde", "azul"}
```

### Estruturas de Controle
```python
# Condicionais
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

# Loops
for fruta in frutas:
    print(fruta)

contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Funções
```python
# Definição de função
def saudacao(nome, periodo="dia"):
    return f"Bom {periodo}, {nome}!"

# Chamada de função
mensagem = saudacao("Ana", "tarde")
print(mensagem)  # Bom tarde, Ana!

# Função com argumentos variáveis
def soma(*numeros):
    return sum(numeros)

total = soma(1, 2, 3, 4)  # 10
```

### Manipulação de Exceções
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Entrada inválida. Digite um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
finally:
    print("Operação finalizada.")
```

## Manipulação de Arquivos

### Leitura e Escrita
```python
# Leitura de arquivo
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Leitura linha por linha
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Escrita em arquivo
with open("novo_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Adicionar conteúdo (append)
with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Conteúdo adicional\n")
```

### Manipulação de Caminhos
```python
import os

# Caminhos
caminho_atual = os.getcwd()
caminho_arquivo = os.path.join(caminho_atual, "dados", "arquivo.txt")

# Verificar existência
if os.path.exists(caminho_arquivo):
    print("O arquivo existe!")

# Criar diretório
os.makedirs("novo_diretorio", exist_ok=True)
```

## Bibliotecas Essenciais

### Requests (HTTP)
```python
import requests

# Requisição GET
resposta = requests.get("https://api.exemplo.com/dados")
dados = resposta.json()

# Requisição POST
payload = {"nome": "João", "email": "joao@exemplo.com"}
resposta = requests.post("https://api.exemplo.com/usuarios", json=payload)
```

### Datetime (Manipulação de Datas)
```python
from datetime import datetime, timedelta

# Data e hora atual
agora = datetime.now()
print(f"Data atual: {agora.strftime('%d/%m/%Y')}")
print(f"Hora atual: {agora.strftime('%H:%M:%S')}")

# Operações com datas
amanha = agora + timedelta(days=1)
uma_semana_atras = agora - timedelta(days=7)
```

### JSON (Manipulação de Dados)
```python
import json

# Converter dicionário para string JSON
dados = {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"}
json_str = json.dumps(dados, ensure_ascii=False, indent=4)

# Converter string JSON para dicionário
dados_dict = json.loads(json_str)

# Ler arquivo JSON
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Escrever arquivo JSON
with open("saida.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
```

## Dicas para Automação

### Boas Práticas
1. **Modularize seu código**: Divida em funções e classes para facilitar manutenção
2. **Adicione logs**: Use a biblioteca `logging` para registrar eventos importantes
3. **Trate exceções**: Sempre preveja possíveis erros e trate-os adequadamente
4. **Use variáveis de ambiente**: Para armazenar informações sensíveis
5. **Documente seu código**: Adicione docstrings e comentários explicativos

### Padrões Comuns
```python
# Configuração de logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='automacao.log'
)

# Uso de variáveis de ambiente
import os
api_key = os.environ.get("API_KEY", "chave_padrao")

# Temporizador para operações
import time
inicio = time.time()
# ... operações ...
fim = time.time()
duracao = fim - inicio
print(f"Operação concluída em {duracao:.2f} segundos")
```

### Depuração
```python
# Depuração básica
print(f"Valor da variável: {variavel}")

# Depuração avançada
import pdb
pdb.set_trace()  # Pausa a execução e abre console interativo

# Verificação de tipos
from typing import List, Dict
def processar_nomes(nomes: List[str]) -> Dict[str, int]:
    return {nome: len(nome) for nome in nomes}
```
