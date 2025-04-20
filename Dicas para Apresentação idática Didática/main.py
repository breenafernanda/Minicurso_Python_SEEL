import os
import sys
import time
from datetime import datetime

def criar_diretorios():
    """Cria os diretórios necessários para o projeto."""
    diretorios = ['dados', 'output', 'logs']
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)
    print("Diretórios criados com sucesso.")

def configurar_log():
    """Configura o sistema de log."""
    import logging
    
    # Criar diretório de logs se não existir
    os.makedirs('logs', exist_ok=True)
    
    # Configurar logging
    log_file = f"logs/automacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger("automacao")
    logger.info("Sistema de log configurado.")
    
    return logger

def executar_extracao(logger):
    """Executa o processo de extração de dados."""
    logger.info("Iniciando processo de extração de dados...")
    
    try:
        from extrator import extrair_todos_dados
        df = extrair_todos_dados()
        logger.info(f"Extração concluída com sucesso. {len(df)} produtos extraídos.")
        return df
    except Exception as e:
        logger.error(f"Erro durante a extração de dados: {e}", exc_info=True)
        sys.exit(1)

def executar_processamento(df, logger):
    """Executa o processo de processamento de dados."""
    logger.info("Iniciando processamento de dados...")
    
    try:
        from processador import limpar_dados, analisar_dados, gerar_graficos
        
        # Limpar dados
        df_limpo = limpar_dados(df)
        
        # Analisar dados
        resultados = analisar_dados(df_limpo)
        
        # Gerar gráficos
        graficos = gerar_graficos(df_limpo, resultados)
        
        logger.info("Processamento de dados concluído com sucesso.")
        return df_limpo, resultados, graficos
    except Exception as e:
        logger.error(f"Erro durante o processamento de dados: {e}", exc_info=True)
        sys.exit(1)

def gerar_relatorio(df, resultados, graficos, logger):
    """Gera o relatório Excel."""
    logger.info("Iniciando geração do relatório Excel...")
    
    try:
        from relatorio_excel import criar_relatorio_excel
        caminho_relatorio = criar_relatorio_excel(df, resultados, graficos)
        logger.info(f"Relatório Excel gerado com sucesso em {caminho_relatorio}")
        return caminho_relatorio
    except Exception as e:
        logger.error(f"Erro durante a geração do relatório Excel: {e}", exc_info=True)
        sys.exit(1)

def gerar_catalogo(df, logger):
    """Gera o catálogo PDF."""
    logger.info("Iniciando geração do catálogo PDF...")
    
    try:
        from catalogo_pdf import criar_catalogo_pdf
        caminho_catalogo = criar_catalogo_pdf(df)
        logger.info(f"Catálogo PDF gerado com sucesso em {caminho_catalogo}")
        return caminho_catalogo
    except Exception as e:
        logger.error(f"Erro durante a geração do catálogo PDF: {e}", exc_info=True)
        sys.exit(1)

def main():
    """Função principal que orquestra todo o fluxo de automação."""
    print("=" * 80)
    print("SISTEMA DE AUTOMAÇÃO DE CATÁLOGO DE OFERTAS")
    print("=" * 80)
    print(f"Data e hora de início: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 80)
    
    # Criar diretórios necessários
    criar_diretorios()
    
    # Configurar sistema de log
    logger = configurar_log()
    
    # Registrar início da execução
    logger.info("Iniciando execução do sistema de automação...")
    
    # Medir tempo de execução
    tempo_inicio = time.time()
    
    try:
        # Etapa 1: Extração de dados
        print("\n[1/4] Extraindo dados de produtos em promoção...")
        df = executar_extracao(logger)
        
        # Etapa 2: Processamento de dados
        print("\n[2/4] Processando e analisando dados...")
        df_processado, resultados, graficos = executar_processamento(df, logger)
        
        # Etapa 3: Geração de relatório Excel
        print("\n[3/4] Gerando relatório Excel...")
        caminho_relatorio = gerar_relatorio(df_processado, resultados, graficos, logger)
        
        # Etapa 4: Geração de catálogo PDF
        print("\n[4/4] Gerando catálogo PDF...")
        caminho_catalogo = gerar_catalogo(df_processado, logger)
        
        # Calcular tempo total de execução
        tempo_total = time.time() - tempo_inicio
        
        # Exibir resumo da execução
        print("\n" + "=" * 80)
        print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")
        print("-" * 80)
        print(f"Tempo total de execução: {tempo_total:.2f} segundos")
        print(f"Total de produtos processados: {len(df_processado)}")
        print(f"Relatório Excel: {caminho_relatorio}")
        print(f"Catálogo PDF: {caminho_catalogo}")
        print("=" * 80)
        
        logger.info(f"Execução concluída com sucesso em {tempo_total:.2f} segundos.")
        
    except Exception as e:
        logger.error(f"Erro durante a execução: {e}", exc_info=True)
        print(f"\nERRO: {e}")
        print("Consulte o arquivo de log para mais detalhes.")
        sys.exit(1)

if __name__ == "__main__":
    main()
