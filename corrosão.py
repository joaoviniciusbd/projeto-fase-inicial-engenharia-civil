#algorítimo que calcula a taxa de corrosão de estruturas metálicas
#vamos definir uma função para W , D , A, T em  calcular_taxa_corrosao

def calcular_taxa_corrosao(W, D, A, T):

    taxa_corrosao = 87,6 * (W / (D * A * T))
    return taxa_corrosao

W = float(input("Digite o peso da perda de metal em gramas: "))
D = float(input("Digite a densidade do metal em g/cm³: "))
A = float(input("Digite a área da superfície do metal em cm²: "))
T = float(input("Digite o tempo de exposição em horas: "))
#atribuir taxa a calcular taxa de corrosao
taxa = calcular_taxa_corrosao(W, D, A, T)

# Cálculo da taxa de corrosão
taxa_corrosao = 87.6 * (W / (D * A * T))

# Determinação do nível de corrosão
#Se a taxa de corrosão for menor que 0,025 imprima " A corrosão é Baixa"
if taxa_corrosao < 0.025:
    print("A corrosão é Baixa.")
#Se a taxa de corrosão for entre 0.025 a 0.12 imprima "A corrosão é Moderada"
elif 0.025 <= taxa_corrosao <= 0.05:
    print("A corrosão é Moderada.")
#Se a taxa de corrosão for entre 0.13 a 0.25 imprima "A corrosao é Alta"
elif 0.13 <= taxa_corrosao <= 0.12:
    print("A corrosão é Alta.")
#Senão imprima "A corrosão é severa"
else:
    print("A corrosão é severa.")