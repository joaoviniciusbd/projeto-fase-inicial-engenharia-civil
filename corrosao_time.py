

def calcular_taxa_corrosao_horas(W, D, A, T_horas):

    
    return 87.6 * (W / (D * A * T_horas))

def calcular_taxa_corrosao_dias(W, D, A, T_dias):
    
    return 87.6 * (W / (D * A * T_dias))

def calcular_taxa_corrosao_anos(W, D, A, T_anos):
    
    return 87.6 * (W / (D * A * (365 * T_anos)))


def determinar_nivel_corrosao_horas(taxa_corrosao):
    if taxa_corrosao < 0.025:
        return "Baixo"
    elif 0.025 <= taxa_corrosao <= 0.12:
        return "Moderado"
    elif 0.13 <= taxa_corrosao <= 0.25:
        return "Alto"
    else:
        return "Severo"


def determinar_nivel_corrosao_dias(taxa_corrosao):
    if taxa_corrosao < 0.6:
        return "Baixo"
    elif 0.6 <= taxa_corrosao <= 2.4:
        return "Moderado"
    elif 2.5 <= taxa_corrosao <= 12:
        return "Alto"
    else:
        return "Severo"


def determinar_nivel_corrosao_anos(taxa_corrosao):
    if taxa_corrosao < 0.0025:
        return "Baixo"
    elif 0.0025 <= taxa_corrosao <= 0.012:
        return "Moderado"
    elif 0.013 <= taxa_corrosao <= 0.025:
        return "Alto"
    else:
        return "Severo"
