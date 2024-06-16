import metal_potenciais
import math

class Metal:
    def __init__(self, metal, corrente, area, aquoso):
        self.metal = metal
        self.corrente = corrente
        self.area = area
        self.aquoso = aquoso
        self.F = 96485  # Constante de Faraday em C/mol

    def calcular_taxa_corrosao(self):
        E_padrao, massa_molar, n = metal_potenciais.obter_propriedades_metal(self.metal)
        
        if E_padrao is None:
            print("Metal não encontrado na tabela de potenciais padrão.")
            return None
        
        # Taxa de oxidação em g/s por unidade de área
        taxa_ox = (self.corrente * massa_molar) / (n * self.F * self.area)
        
        return taxa_ox

    def classificar_corrosao(self, taxa):
        if taxa > 1e-4:
            return "Alto"
        elif taxa > 1e-6:
            return "Moderado"
        else:
            return "Baixo"

class Agua:
    @staticmethod
    def calcular_pHS(temperatura, STD, Ca_CaCO3, alcalinidade_CaCO3):
        A = (math.log10(STD) - 1) / 10
        B = -13.12 * math.log10(temperatura + 273) + 34.55
        C = math.log10(Ca_CaCO3) - 0.4
        D = math.log10(alcalinidade_CaCO3)
        pHS = (9.3 + A + B) - (C + D)
        return pHS

    @staticmethod
    def calcular_IER(pHS, pH_real):
        return 2 * pHS - pH_real

    @staticmethod
    def classificar_agua(IER):
        if IER < 6.5:
            return "Água não incrustante, água agressiva"
        elif 6.5 <= IER <= 7:
            return "Água não incrustante, ligeiramente agressiva"
        elif 7 < IER <= 8:
            return "Água incrustante, ligeiramente agressiva"
        else:
            return "Água incrustante"

# Solicitando entrada do usuário
metal_input = input("Digite o metal (ex: Zn, Cu): ")
corrente_input = float(input("Digite a corrente de corrosão observada (em amperes): "))
area_input = float(input("Digite a área do eletrodo (em cm^2): "))
aquoso_input = input("O metal está em meio aquoso? (sim/não): ").strip().lower() == 'sim'

# Entradas para a análise da água
temperatura_input = float(input("Digite a temperatura da água (em °C): "))
STD_input = float(input("Digite o STD da água: "))
Ca_CaCO3_input = float(input("Digite a concentração de Ca²⁺ de CaCO₃ (em mg/L): "))
alcalinidade_CaCO3_input = float(input("Digite a alcalinidade do CaCO₃ (em mg/L): "))
pH_real_input = float(input("Digite o pH real da água: "))

# Instanciando a classe Metal
metal_obj = Metal(metal_input, corrente_input, area_input, aquoso_input)

# Calculando a taxa de corrosão
taxa_de_corrosao = metal_obj.calcular_taxa_corrosao()

if taxa_de_corrosao is not None:
    nivel_corrosao = metal_obj.classificar_corrosao(taxa_de_corrosao)
    meio = 'meio aquoso' if aquoso_input else 'meio não aquoso'
    print(f"A taxa de corrosão para {metal_input} em {meio} é {taxa_de_corrosao:.6e} g/s por cm^2.")
    print(f"O nível de corrosão é {nivel_corrosao}.")

# Calculando pHS e IER
pHS = Agua.calcular_pHS(temperatura_input, STD_input, Ca_CaCO3_input, alcalinidade_CaCO3_input)
IER = Agua.calcular_IER(pHS, pH_real_input)
classificacao_agua = Agua.classificar_agua(IER)

print(f"O pH de saturação (pHS) é: {pHS:.2f}")
print(f"O Índice de Estabilidade de Ryznar (IER) é: {IER:.2f}")
print(f"A classificação da água é: {classificacao_agua}")


