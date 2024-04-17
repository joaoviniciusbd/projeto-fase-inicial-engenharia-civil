  #algorítimo que calcula a taxa de corrosão de estruturas metálicas
  
import corrosao_time

unidade = input("digite a unidade de tempo (horas,dias ou anos): ")

def calcular_taxa_corrosao(W, D, A, T, unidade) :
 
    if unidade == 'horas':
        taxa = corrosao_time.calcular_taxa_corrosao_horas(W, D, A, T)
        nivel_corrosao = corrosao_time.determinar_nivel_corrosao_horas(taxa)
    elif unidade == 'dias':
        taxa = corrosao_time.calcular_taxa_corrosao_dias(W, D, A, T)
        nivel_corrosao = corrosao_time.determinar_nivel_corrosao_dias(taxa)
    elif unidade == 'anos':
        taxa = corrosao_time.calcular_taxa_corrosao_anos(W, D, A, T)
        nivel_corrosao = corrosao_time.determinar_nivel_corrosao_anos(taxa)
    else:
        raise ValueError("Unidade de tempo inválida. Use 'horas', 'dias' ou 'anos'.")

    return taxa, nivel_corrosao

W = float(input("Digite o peso da perda de metal em gramas: "))
D = float(input("Digite a densidade do metal em g/cm³: "))
A = float(input("Digite a área da superfície do metal em cm²: "))
T = float(input("Digite o tempo de exposição na unidade escolhida: "))

  
taxa_corrosao, nivel_corrosao = calcular_taxa_corrosao(W, D, A, T, unidade)

print(f"A taxa de corrosão é de {taxa_corrosao:.5f} mm/{unidade}.")
print(f"O nível de corrosão é: {nivel_corrosao}")
  
  
  