import os
import subprocess
import sys

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    return result.returncode

def setup_git(user_name, user_email, commit_name, repo_url=None ):
    print("🚀 Configurando Git...")

    # 1. Config global
    run(f'git config --global user.name "{user_name}"')
    run(f'git config --global user.email "{user_email}"')

    # 2. Inicializa repositório
    run("git init")

    # 3. Cria .gitignore se não existir
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write("""# Ignore arquivos locais
contas.xlsx
*.zip
*.7z
*.log
*.tmp
__pycache__/
.env
tor_temp_profile/
""")
        print("📄 .gitignore criado")

    # 4. Adiciona e commita
    run("git add .")
    run(f'git commit -m "🔰 {commit_name}"')

    # 5. (Opcional) Seta origem e faz push
    if repo_url:
        try:
            run(f"git remote add origin {repo_url}")
        except:pass
        run("git branch -M main")
        run("git push -u origin main")

    print("✅ Git configurado com sucesso!")

# --- Executa com seus dados ---
if __name__ == "__main__":
    repositorio = "Minicurso_Python_SEEL"
    repositorio_link = f"https://github.com/breenafernanda/{repositorio}.git"
    
    # Verifica se foi passado um parâmetro de commit via linha de comando
    if len(sys.argv) > 1:
        commit = sys.argv[1]
    else:
        commit = 'supportv0'  # Valor padrão caso nenhum parâmetro seja fornecido
    
    print(f"📝 Mensagem de commit: {commit}")
    setup_git("breenafernanda", "d201810853@uftm.edu.br", commit, repositorio_link)
