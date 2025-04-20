// Funções para o site da SEEL

// Função para alternar entre as abas do cronograma
function switchCronogramaTab(dayNumber) {
    // Esconder todas as abas de conteúdo
    document.querySelectorAll('.cronograma-content').forEach(function(content) {
        content.classList.remove('active');
    });
    
    // Remover a classe active de todas as abas
    document.querySelectorAll('.cronograma-tab').forEach(function(tab) {
        tab.classList.remove('active');
    });
    
    // Mostrar a aba selecionada
    document.getElementById('day-' + dayNumber).classList.add('active');
    
    // Adicionar a classe active à aba clicada
    document.querySelector('.cronograma-tab[data-day="' + dayNumber + '"]').classList.add('active');
}

// Função para destacar o item de menu ativo
function highlightActiveMenu() {
    const currentPage = window.location.pathname.split('/').pop();
    
    document.querySelectorAll('.nav-link').forEach(function(link) {
        link.classList.remove('active');
        
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });
}

// Função para aplicar destaque de sintaxe ao código Python
function applySyntaxHighlighting() {
    document.querySelectorAll('.code-block pre code').forEach(function(codeBlock) {
        const code = codeBlock.textContent;
        
        // Padrões para diferentes elementos do código Python
        const patterns = [
            // Palavras-chave
            { pattern: /\b(def|class|if|else|elif|for|while|try|except|finally|with|return|import|from|as|in|is|not|and|or|True|False|None|break|continue|pass|raise|assert|global|nonlocal|lambda|yield)\b/g, className: 'python-keyword' },
            
            // Funções built-in
            { pattern: /\b(print|len|range|int|str|float|list|dict|set|tuple|sum|min|max|sorted|map|filter|zip|enumerate|open|input|type|dir|help|super|any|all|iter|next|round|abs|pow|divmod)\b(?=\s*\()/g, className: 'python-builtin' },
            
            // Strings
            { pattern: /(["'])((?:\\\1|(?:(?!\1)).)*)(\1)/g, className: 'python-string' },
            { pattern: /(f["'])((?:\\\1|(?:(?!\1)).)*)(\1)/g, className: 'python-string' },
            { pattern: /(r["'])((?:\\\1|(?:(?!\1)).)*)(\1)/g, className: 'python-string' },
            
            // Comentários
            { pattern: /#.*$/gm, className: 'python-comment' },
            
            // Números
            { pattern: /\b\d+(\.\d+)?\b/g, className: 'python-number' },
            
            // Decoradores
            { pattern: /@\w+/g, className: 'python-decorator' },
            
            // Operadores
            { pattern: /(\+|\-|\*|\/|\%|\=|\<|\>|\!|\&|\||\^|\~|\:)/g, className: 'python-operator' },
            
            // Métodos
            { pattern: /\.(\w+)(?=\s*\()/g, className: 'python-method' },
            
            // Self
            { pattern: /\bself\b/g, className: 'python-self' },
            
            // Import statements
            { pattern: /\b(import|from|as)\b/g, className: 'python-import' },
            
            // Funções definidas
            { pattern: /(?<=def\s+)(\w+)(?=\s*\()/g, className: 'python-function' },
            
            // Classes definidas
            { pattern: /(?<=class\s+)(\w+)(?=\s*[:\(])/g, className: 'python-class' },
            
            // Parâmetros de função
            { pattern: /(?<=\()([^)]+)(?=\))/g, className: 'python-parameter' }
        ];
        
        // Substituir caracteres especiais para evitar problemas com HTML
        let highlightedCode = code.replace(/&/g, '&amp;')
                                 .replace(/</g, '&lt;')
                                 .replace(/>/g, '&gt;');
        
        // Aplicar cada padrão
        patterns.forEach(function(item) {
            highlightedCode = highlightedCode.replace(item.pattern, function(match) {
                return `<span class="${item.className}">${match}</span>`;
            });
        });
        
        // Atualizar o conteúdo do bloco de código
        codeBlock.innerHTML = highlightedCode;
    });
    
    // Adicionar botão de cópia para cada bloco de código
    document.querySelectorAll('.code-block').forEach(function(block) {
        // Verificar se o bloco já tem um botão de cópia
        if (!block.querySelector('.copy-btn')) {
            const header = block.querySelector('.code-header');
            
            if (header) {
                // Se já existe um header, adicionar o botão às ações
                let actions = header.querySelector('.code-actions');
                
                if (!actions) {
                    actions = document.createElement('div');
                    actions.className = 'code-actions';
                    header.appendChild(actions);
                }
                
                const copyBtn = document.createElement('button');
                copyBtn.textContent = 'Copiar';
                copyBtn.className = 'copy-btn';
                actions.appendChild(copyBtn);
                
                // Adicionar evento de clique
                copyBtn.addEventListener('click', function() {
                    const code = block.querySelector('pre').textContent;
                    navigator.clipboard.writeText(code).then(function() {
                        const originalText = copyBtn.textContent;
                        copyBtn.textContent = 'Copiado!';
                        setTimeout(function() {
                            copyBtn.textContent = originalText;
                        }, 2000);
                    });
                });
            }
        }
    });
}

// Função para inicializar os editores CodeMirror nos desafios
function initializeCodeEditors() {
    if (typeof CodeMirror !== 'undefined') {
        document.querySelectorAll('.challenge-editor').forEach(function(textarea) {
            const id = textarea.id;
            const challengeId = id.replace('editor-', '');
            
            const editor = CodeMirror.fromTextArea(textarea, {
                mode: 'python',
                theme: 'dracula',
                lineNumbers: true,
                autoCloseBrackets: true,
                matchBrackets: true,
                indentUnit: 4,
                tabSize: 4,
                indentWithTabs: false,
                lineWrapping: true
            });
            
            // Armazenar o editor em um objeto global
            window.codeEditors = window.codeEditors || {};
            window.codeEditors[challengeId] = editor;
        });
        
        // Configurar botões de solução e reset
        setupChallengeButtons();
    }
}

// Função para configurar os botões dos desafios
function setupChallengeButtons() {
    // Soluções para os desafios
    const solutions = {
        'intro-1': 'print("Olá, mundo!")',
        'intro-2': `def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

# Teste da função
idade = int(input("Digite sua idade: "))
print(verificar_maioridade(idade))`,
        'selenium-1': `from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Inicializar o navegador Chrome
driver = webdriver.Chrome(Options())

# Acessar uma URL
driver.get("https://www.google.com")

# Encontrar um elemento na página (campo de pesquisa)
campo_pesquisa = driver.find_element(By.NAME, "q")

# Interagir com o elemento
campo_pesquisa.send_keys("Selenium Python")

# Esperar um pouco para visualizar
time.sleep(2)

# Fechar o navegador
driver.quit()`
    };
    
    // Botões de solução
    document.querySelectorAll('.btn-solution').forEach(function(button) {
        const challengeId = button.getAttribute('data-challenge');
        button.addEventListener('click', function() {
            if (window.codeEditors && window.codeEditors[challengeId] && solutions[challengeId]) {
                window.codeEditors[challengeId].setValue(solutions[challengeId]);
            }
        });
    });
    
    // Botões de reset
    document.querySelectorAll('.btn-reset').forEach(function(button) {
        const challengeId = button.getAttribute('data-challenge');
        button.addEventListener('click', function() {
            if (window.codeEditors && window.codeEditors[challengeId]) {
                const originalCode = document.getElementById('editor-' + challengeId).textContent;
                window.codeEditors[challengeId].setValue(originalCode);
                const resultElement = document.getElementById('result-' + challengeId);
                if (resultElement) {
                    resultElement.textContent = '';
                }
            }
        });
    });
}

// Função para inicializar o menu mobile
function initializeMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
}

// Inicializar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    // Destacar o item de menu ativo
    highlightActiveMenu();
    
    // Inicializar o menu mobile
    initializeMobileMenu();
    
    // Configurar as abas do cronograma
    document.querySelectorAll('.cronograma-tab').forEach(function(tab) {
        tab.addEventListener('click', function() {
            const day = this.getAttribute('data-day');
            switchCronogramaTab(day);
        });
    });
    
    // Aplicar destaque de sintaxe ao código Python
    applySyntaxHighlighting();
    
    // Inicializar os editores de código
    initializeCodeEditors();
});
