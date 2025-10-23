from maspy import *
from agente_veiculo import AgenteVeiculoAutonomo
from agente_estacao import AgenteEstacaoDeRecarga
from ambiente_sma import AmbienteCidade

if __name__ == "__main__":
    
    # Cria o Ambiente
    cidade = AmbienteCidade("MinhaCidade")
    
    # Cria os Agentes
    veiculos = [
        AgenteVeiculoAutonomo("AVA_1", bateria_inicial=30),
        AgenteVeiculoAutonomo("AVA_2", bateria_inicial=15),
        AgenteVeiculoAutonomo("AVA_3", bateria_inicial=50)
    ]
    
    estacoes = [
        AgenteEstacaoDeRecarga("EstacaoNorte", num_vagas=1, preco_base=0.75, localizacao=(2,2)),
        AgenteEstacaoDeRecarga("EstacaoSul", num_vagas=2, preco_base=0.50, localizacao=(8,8))
    ]
    
    agentes = veiculos + estacoes

    # Conecta os Agentes ao Ambiente
    Admin().connect_to(agentes, cidade)
    
    # Inicia o sistema
    print("--- Iniciando Simulação SMA de Recarga ---")
    Admin().start_system()