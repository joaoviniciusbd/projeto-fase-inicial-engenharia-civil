# metal_potenciais.py

# Definindo os dados de potenciais padrão e outras propriedades
dados_potenciais = {
    'Li': {'E° (V)': 3.04, 'Massa Molar (g/mol)': 6.94, 'n': 1},
    'K': {'E° (V)': 2.92, 'Massa Molar (g/mol)': 39.10, 'n': 1},
    'Ca': {'E° (V)': 2.87, 'Massa Molar (g/mol)': 40.08, 'n': 2},
    'Na': {'E° (V)': 2.71, 'Massa Molar (g/mol)': 22.99, 'n': 1},
    'Mg': {'E° (V)': 2.37, 'Massa Molar (g/mol)': 24.31, 'n': 2},
    'Al': {'E° (V)': 1.66, 'Massa Molar (g/mol)': 26.98, 'n': 3},
    'Zn': {'E° (V)': 0.76, 'Massa Molar (g/mol)': 65.38, 'n': 2},
    'Cr': {'E° (V)': 0.74, 'Massa Molar (g/mol)': 52.00, 'n': 3},
    'Fe': {'E° (V)': 0.44, 'Massa Molar (g/mol)': 55.85, 'n': 2},
    'Ni': {'E° (V)': 0.25, 'Massa Molar (g/mol)': 58.69, 'n': 2},
    'Pb': {'E° (V)': 0.13, 'Massa Molar (g/mol)': 207.2, 'n': 2},
    'H2': {'E° (V)': 0.00, 'Massa Molar (g/mol)': 2.02, 'n': 2},
    'Cu': {'E° (V)': -0.34, 'Massa Molar (g/mol)': 63.55, 'n': 2},
    'Ag': {'E° (V)': -0.80, 'Massa Molar (g/mol)': 107.87, 'n': 1},
    'Au': {'E° (V)': -1.50, 'Massa Molar (g/mol)': 196.97, 'n': 1}
}

def obter_propriedades_metal(metal):
    """
    Função para obter o potencial padrão de oxidação, massa molar e n de um metal.
    
    Args:
    metal (str): Símbolo do metal (ex: Zn, Cu).
    
    Returns:
    tuple: (E° (V), Massa Molar (g/mol), n) se o metal for encontrado, caso contrário (None, None, None).
    """
    propriedades = dados_potenciais.get(metal)
    if propriedades:
        return propriedades['E° (V)'], propriedades['Massa Molar (g/mol)'], propriedades['n']
    else:
        return None, None, None
