# Estrutura Didática Aprimorada para Minicurso de Automação com Python

## Visão Geral do Minicurso

### Título
**Automatizando Tarefas com Python: Do Básico à Prática**

### Duração Total
3 horas (180 minutos)

### Público-Alvo
Iniciantes em programação interessados em automação de tarefas

### Objetivo Geral
Capacitar os participantes a criar scripts de automação em Python para tarefas cotidianas, desde a extração de dados da web até a geração de relatórios em PDF.

## Estrutura Modular

### Módulo 1: Boas-vindas e Contextualização (15 minutos)
**Objetivo de Aprendizagem:** Compreender a importância da automação e os benefícios que ela pode trazer para o dia a dia.

#### Tópicos:
1. **Apresentação pessoal e quebra-gelo** (3 min)
   - Dinâmica rápida para conhecer os participantes
   - Nivelamento de expectativas

2. **O poder da automação no mundo moderno** (5 min)
   - Exemplos reais de como a automação transforma processos
   - Demonstração visual de "antes e depois" da automação
   - Estatísticas sobre economia de tempo com automação

3. **Visão geral do minicurso** (5 min)
   - Apresentação da jornada de aprendizado
   - O que será construído ao final (projeto integrador)
   - Como os módulos se conectam entre si

4. **Estabelecimento do contrato de aprendizagem** (2 min)
   - Momentos para perguntas
   - Incentivo à participação ativa
   - Recursos disponíveis durante e após o minicurso

### Módulo 2: Preparando o Ambiente de Desenvolvimento (20 minutos)
**Objetivo de Aprendizagem:** Configurar corretamente todas as ferramentas necessárias para o desenvolvimento de scripts de automação em Python.

#### Tópicos:
1. **Por que Python para automação?** (3 min)
   - Comparação com outras linguagens
   - Ecossistema de bibliotecas para automação
   - Curva de aprendizado x potencial de aplicação

2. **Instalação guiada do Python** (5 min)
   - Download e instalação passo a passo
   - Verificação da instalação via terminal/prompt
   - Explicação sobre o PATH do sistema

3. **Configuração do VS Code como ambiente de desenvolvimento** (5 min)
   - Instalação e configuração básica
   - Extensões recomendadas para Python
   - Atalhos úteis para produtividade

4. **Instalação das bibliotecas necessárias** (5 min)
   - Explicação sobre o pip e gerenciamento de pacotes
   - Instalação das bibliotecas principais (Selenium, Pandas, OpenPyXL, FPDF)
   - Verificação das instalações

5. **Configuração do WebDriver para Selenium** (2 min)
   - Download do ChromeDriver
   - Configuração do PATH para o WebDriver
   - Teste rápido de funcionamento

### Módulo 3: Fundamentos de Python para Automação (30 minutos)
**Objetivo de Aprendizagem:** Dominar os conceitos básicos de Python necessários para criar scripts de automação eficientes.

#### Tópicos:
1. **Sintaxe básica e estrutura de um script Python** (5 min)
   - Indentação e sua importância
   - Comentários e documentação
   - Execução de scripts via terminal e via IDE

2. **Variáveis, tipos de dados e operações** (7 min)
   - Tipos básicos (int, float, str, bool)
   - Operações com diferentes tipos
   - Conversão entre tipos (type casting)
   - Formatação de strings (f-strings)

3. **Estruturas de controle de fluxo** (7 min)
   - Condicionais (if, elif, else)
   - Loops (for, while)
   - Controle de loops (break, continue)
   - Exemplo prático: validação de entradas do usuário

4. **Funções e modularização** (7 min)
   - Definição e chamada de funções
   - Parâmetros e retorno
   - Escopo de variáveis
   - Importação de módulos

5. **Manipulação de erros e exceções** (4 min)
   - Try/except/finally
   - Tipos comuns de exceções
   - Criação de mensagens de erro amigáveis
   - Exemplo prático: tratamento de erros em inputs

### Módulo 4: Automação Web com Selenium (35 minutos)
**Objetivo de Aprendizagem:** Utilizar o Selenium para automatizar interações com páginas web, extraindo dados e realizando ações como um usuário humano.

#### Tópicos:
1. **Introdução ao Selenium e WebDriver** (5 min)
   - O que é e para que serve
   - Arquitetura básica (cliente-servidor)
   - Navegadores suportados
   - Limitações e considerações éticas

2. **Navegação básica e localização de elementos** (8 min)
   - Abrindo páginas e gerenciando janelas
   - Métodos de localização (ID, CSS, XPath, etc.)
   - Ferramentas de inspeção do navegador
   - Exemplo prático: navegando até um site e extraindo o título

3. **Interação com elementos da página** (8 min)
   - Cliques e preenchimento de formulários
   - Seleção de opções em dropdowns
   - Trabalho com frames e janelas
   - Exemplo prático: preenchimento de um formulário de login

4. **Esperas e sincronização** (7 min)
   - Problemas de timing em páginas dinâmicas
   - Esperas explícitas vs. implícitas
   - Condições de espera personalizadas
   - Exemplo prático: esperando um elemento carregar antes de interagir

5. **Extração de dados estruturados** (7 min)
   - Capturando texto e atributos
   - Navegando em tabelas e listas
   - Salvando dados extraídos
   - Exemplo prático: extração de produtos em promoção (como no exemplo do curso)

### Módulo 5: Manipulação de Dados com Pandas (25 minutos)
**Objetivo de Aprendizagem:** Processar e analisar dados extraídos da web utilizando a biblioteca Pandas.

#### Tópicos:
1. **Introdução ao Pandas e suas estruturas de dados** (5 min)
   - Series e DataFrames
   - Criação a partir de diferentes fontes
   - Visualização básica de dados
   - Exemplo prático: criando um DataFrame a partir dos dados extraídos

2. **Limpeza e transformação de dados** (7 min)
   - Tratamento de valores ausentes
   - Remoção de duplicatas
   - Conversão de tipos
   - Exemplo prático: limpando dados extraídos da web

3. **Filtragem e seleção de dados** (5 min)
   - Seleção por índice e rótulo
   - Filtragem por condições
   - Ordenação de dados
   - Exemplo prático: filtrando produtos por desconto

4. **Análise básica e agregações** (5 min)
   - Estatísticas descritivas
   - Agrupamento e agregação
   - Exemplo prático: calculando médias e totais de descontos

5. **Exportação de dados processados** (3 min)
   - Salvando em diferentes formatos
   - Integração com outras bibliotecas
   - Exemplo prático: exportando dados processados para Excel

### Módulo 6: Trabalhando com Planilhas usando OpenPyXL (20 minutos)
**Objetivo de Aprendizagem:** Criar e manipular planilhas Excel de forma programática para automatizar relatórios e análises.

#### Tópicos:
1. **Introdução ao OpenPyXL** (3 min)
   - Diferenças entre Pandas e OpenPyXL
   - Quando usar cada um
   - Estrutura básica (workbooks, worksheets, cells)

2. **Criação e leitura de planilhas** (5 min)
   - Criando novos workbooks
   - Acessando planilhas existentes
   - Navegando entre células e planilhas
   - Exemplo prático: criando uma planilha de produtos

3. **Manipulação de células e dados** (5 min)
   - Escrita e leitura de valores
   - Tipos de dados suportados
   - Fórmulas e cálculos
   - Exemplo prático: preenchendo dados de produtos

4. **Formatação e estilização** (5 min)
   - Formatação de células (cores, fontes, bordas)
   - Mesclagem de células
   - Ajuste de largura e altura
   - Exemplo prático: criando um relatório visualmente atraente

5. **Recursos avançados** (2 min)
   - Gráficos e imagens
   - Tabelas dinâmicas
   - Proteção de planilhas
   - Exemplo prático: adicionando um gráfico de barras para descontos

### Módulo 7: Geração de Documentos PDF (20 minutos)
**Objetivo de Aprendizagem:** Criar documentos PDF personalizados a partir de dados processados para relatórios profissionais.

#### Tópicos:
1. **Introdução à biblioteca FPDF** (3 min)
   - Comparação com outras bibliotecas PDF
   - Estrutura básica de um documento
   - Fluxo de trabalho para criação de PDFs

2. **Criação de documentos e páginas** (4 min)
   - Configuração de página (tamanho, orientação, margens)
   - Adição de novas páginas
   - Cabeçalhos e rodapés
   - Exemplo prático: criando a estrutura básica do catálogo

3. **Adição de texto e formatação** (5 min)
   - Fontes, tamanhos e estilos
   - Alinhamento e posicionamento
   - Cores e efeitos
   - Exemplo prático: adicionando títulos e descrições de produtos

4. **Incorporação de imagens** (5 min)
   - Formatos suportados
   - Redimensionamento e posicionamento
   - Manipulação de imagens da web
   - Exemplo prático: adicionando imagens de produtos ao catálogo

5. **Elementos avançados e finalização** (3 min)
   - Tabelas e listas
   - Links e marcadores
   - Metadados do documento
   - Exemplo prático: finalizando o catálogo de ofertas

### Módulo 8: Projeto Integrador - Catálogo Automatizado de Ofertas (15 minutos)
**Objetivo de Aprendizagem:** Integrar todas as tecnologias aprendidas em um único fluxo de trabalho automatizado.

#### Tópicos:
1. **Revisão do fluxo completo de automação** (3 min)
   - Diagrama do processo end-to-end
   - Conexões entre as diferentes etapas
   - Pontos de atenção e possíveis falhas

2. **Execução guiada do projeto completo** (7 min)
   - Extração de dados com Selenium
   - Processamento com Pandas
   - Armazenamento em Excel com OpenPyXL
   - Geração de PDF com FPDF
   - Demonstração do resultado final

3. **Ideias para expansão e personalização** (3 min)
   - Agendamento de execução
   - Envio automático por e-mail
   - Hospedagem na web
   - Integração com outras ferramentas

4. **Perguntas e respostas finais** (2 min)
   - Esclarecimento de dúvidas
   - Compartilhamento de recursos adicionais
   - Próximos passos na jornada de automação

## Estratégias Didáticas Transversais

### Abordagem Prática
- Cada módulo inclui exemplos práticos e demonstrações em tempo real
- Código-fonte completo disponibilizado para acompanhamento
- Exercícios incrementais que constroem o projeto final

### Recursos Visuais
- Diagramas de fluxo para ilustrar processos
- Capturas de tela comentadas
- Código colorido para destacar conceitos importantes

### Interatividade
- Perguntas direcionadas ao longo da apresentação
- Mini-desafios para resolução em conjunto
- Momentos de "faça você mesmo" com suporte

### Contextualização
- Exemplos baseados em cenários reais do dia a dia
- Conexão entre conceitos técnicos e aplicações práticas
- Discussão sobre casos de uso além do escopo do minicurso

## Materiais de Apoio

### Para o Instrutor
- Roteiro detalhado com tempos sugeridos
- Notas de apresentação para cada slide
- Respostas para perguntas frequentes
- Lista de verificação pré-minicurso

### Para os Participantes
- Slides em formato digital
- Código-fonte comentado de todos os exemplos
- Folhas de referência rápida para cada tecnologia
- Guia de recursos para aprofundamento
- Exercícios adicionais para prática pós-minicurso
