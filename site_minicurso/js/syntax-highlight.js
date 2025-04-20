// Função para aplicar destaque de sintaxe ao código Python
function applySyntaxHighlighting() {
    document.querySelectorAll('.code-block pre').forEach(function(codeBlock) {
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
        
        // Aplicar destaque de sintaxe
        let highlightedCode = code;
        
        // Substituir caracteres especiais para evitar problemas com HTML
        highlightedCode = highlightedCode.replace(/&/g, '&amp;')
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
            } else {
                // Se não existe um header, adicionar o botão diretamente ao bloco
                const copyBtn = document.createElement('button');
                copyBtn.textContent = 'Copiar';
                copyBtn.className = 'copy-btn';
                copyBtn.style.position = 'absolute';
                copyBtn.style.top = '10px';
                copyBtn.style.right = '10px';
                block.appendChild(copyBtn);
                
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

// Executar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    // Carregar o CSS de destaque de sintaxe
    const syntaxCss = document.createElement('link');
    syntaxCss.rel = 'stylesheet';
    syntaxCss.href = 'css/syntax-highlight.css';
    document.head.appendChild(syntaxCss);
    
    // Aplicar destaque de sintaxe após um pequeno delay para garantir que o CSS foi carregado
    setTimeout(applySyntaxHighlighting, 100);
});
