import pandas as pd
import matplotlib.pyplot as plt

class CorrosaoMonitoramento:
    # Biblioteca de metais com densidade (g/cm³) e área superficial padrão (cm²)
    metais = {
        'aço-carbono': {'densidade': 7.85, 'area_padrao': 20},
        'alumínio': {'densidade': 2.70, 'area_padrao': 20},
        'cobre': {'densidade': 8.96, 'area_padrao': 20},
        'zinco': {'densidade': 7.14, 'area_padrao': 20},
        'ferro': {'densidade': 7.87, 'area_padrao': 20},
        'latão': {'densidade': 8.44, 'area_padrao': 20},
        'níquel': {'densidade': 8.90, 'area_padrao': 20},
        'titânio': {'densidade': 4.51, 'area_padrao': 20}
    }

    def __init__(self, metal):
        if metal in self.metais:
            self.densidade = self.metais[metal]['densidade']
            self.area_padrao = self.metais[metal]['area_padrao']
            self.metal = metal
        else:
            raise ValueError("Metal não encontrado na biblioteca.")
        self.dados = []

    def calcular_taxa_corrosao(self, massa_inicial, massa_final, area, tempo, salinidade=0):
        K = 8.76e4
        perda_massa = massa_inicial - massa_final
        taxa_corrosao = (K * perda_massa) / (self.densidade * area * tempo) * (1 + salinidade / 100)
        return taxa_corrosao

    def classificar_taxa_corrosao(self, taxa_corrosao):
        if taxa_corrosao < 0.1:
            return "Baixa"
        elif 0.1 <= taxa_corrosao < 0.5:
            return "Moderada"
        else:
            return "Alta"

    def sugerir_solucao(self, classificacao):
        if classificacao == "Baixa":
            return "Solução sugerida para Baixa taxa de corrosão: Monitoramento regular e manutenção preventiva."
        elif classificacao == "Moderada":
            return "Solução sugerida para Moderada taxa de corrosão: Implementação de revestimentos protetivos e inspeções periódicas."
        elif classificacao == "Alta":
            return "Solução sugerida para Alta taxa de corrosão: Aplicação de revestimentos mais resistentes e revisão do ambiente de exposição."

    def adicionar_dados_interativo(self):
        while True:
            data = input("Insira a data (YYYY-MM-DD) ou 'q' para sair: ")
            if data.lower() == 'q':
                break
            massa_inicial = float(input("Insira a massa inicial (g): "))
            massa_final = float(input("Insira a massa final (g): "))
            area = float(input(f"Insira a área (cm²), padrão é {self.area_padrao}: ") or self.area_padrao)
            tempo = float(input("Insira o tempo de exposição (horas): "))
            salinidade = float(input("Insira a salinidade (%) [opcional]: ") or 0)

            taxa_corrosao = self.calcular_taxa_corrosao(massa_inicial, massa_final, area, tempo, salinidade)
            classificacao = self.classificar_taxa_corrosao(taxa_corrosao)
            solucao = self.sugerir_solucao(classificacao)
            self.dados.append({
                'data': data,
                'massa_inicial': massa_inicial,
                'massa_final': massa_final,
                'area': area,
                'tempo': tempo,
                'salinidade': salinidade,
                'taxa_corrosao': taxa_corrosao,
                'classificacao': classificacao,
                'solucao': solucao
            })

    def gerar_grafico(self):
        if not self.dados:
            print("Nenhum dado adicionado. Adicione dados primeiro.")
            return

        df = pd.DataFrame(self.dados)
        df['data'] = pd.to_datetime(df['data'])
        df.set_index('data', inplace=True)
        df['taxa_corrosao'].plot(marker='o')
        plt.title(f'Taxa de Corrosão ao Longo do Tempo ({self.metal.capitalize()})')
        plt.xlabel('Data')
        plt.ylabel('Taxa de Corrosão (mm/ano)')
        plt.grid(True)
        plt.show()

    def imprimir_dados(self):
        if not self.dados:
            print("Nenhum dado adicionado. Adicione dados primeiro.")
            return

        df = pd.DataFrame(self.dados)
        print(df)

        # Mostrar sugestões de soluções para cada classificação de corrosão
        for index, row in df.iterrows():
            print(f"\nSolução sugerida para a data {index}:")
            print(row['solucao'])
            print("="*50)

# Exemplo de uso interativo com múltiplos dados
try:
    metal_escolhido = input("Escolha um metal para monitoramento (aço-carbono, alumínio, cobre, zinco, ferro, latão, níquel, titânio): ")
    monitor = CorrosaoMonitoramento(metal=metal_escolhido)

    # Adicionar dados interativamente
    monitor.adicionar_dados_interativo()

    # Gerar gráfico de monitoramento
    monitor.gerar_grafico()

    # Imprimir os dados com a classificação de corrosão e sugestões de solução
    monitor.imprimir_dados()

except ValueError as ve:
    print(ve)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
