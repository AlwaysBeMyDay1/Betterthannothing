
def calculate_savings(recyclelist):
    product = {
        '알루미늄 캔': [0.0000143, 'aluminumcan'],
        '양철캔': [0.0000650, 'steelcan'],
        '옷걸이': [0.0000700, 'steelcan'],
        '유리병': [0.0002650, 'glass'],
        '와인병': [0.0005400, 'glass'],
        '플라스틱 우유병': [0.0001025, 'HDPE'],
        '플라스틱 세제통': [0.0001650, 'HDPE'],
        '비닐봉지': [0.0000039, 'HDPE'],
        '500ml 페트병': [0.0000257, 'PET'],
        '2L 페트병': [0.0000650, 'PET'],
        '박스': [0.0011000, 'cardboard'],
        '잡지': [0.0001500, 'magazine'],
        '카탈로그': [0.0005000, 'magazine'],
        '신문': [0.0002222, 'newspaper'],
        'A4 용지': [0.0000050, 'officepaper'],
        '책': [0.000551156, 'textbook'],
    }
    energy_consumed_or_avoided_compared_to_landfilling = {
        'aluminumcan': 206.95,
        'steelcan': 20.49,
        'copperwire': 83.12,
        'glass': 2.65,
        'HDPE': 51.43,
        'LDPE': 56.54,
        'PET': 53.36,
        'cardboard': 15.63,
        'magazine': 1.09,
        'newspaper': 16.9,
        'officepaper': 10.08,
        'phonebook': 11.84,
        'textbook': 0.53,
        # 'dimensionallumber': -0.22,
        # 'mdf': -0.49,
        # 'mixedmetal': 74.84,
        # 'mixedplastic': 53.21,
        # 'mixedrecyclables': 16.99,
        # 'carpet': 106.11,
        # 'PC': 43.96,
        # 'tire': 52.49
    }
    sum = 0
    for items, nums in recyclelist:
        sum += ((product[items][0] * nums) * energy_consumed_or_avoided_compared_to_landfilling[product[items][1]] * 1000)
    return sum


def calculate_kwh(net_energy_saving):
    upstream_electricity_efficiency = 0.41
    transmission_and_distribution_losses = 0.0354
    mmbtu_to_kwh = 0.003412
    delivered_electricity_equivalent_thousand_mmbtu_to_kwh = (mmbtu_to_kwh / upstream_electricity_efficiency) / (1 - transmission_and_distribution_losses)
    delivered_electricity_equivalent_thousand_btu_to_kwh = delivered_electricity_equivalent_thousand_mmbtu_to_kwh * 1000
    return net_energy_saving / delivered_electricity_equivalent_thousand_btu_to_kwh


def calculate(recyclelist):
    return calculate_kwh(net_energy_saving=calculate_savings(recyclelist))


if __name__ == "__main__":
    li = [('알루미늄캔', 2), ('양철캔', 2)]
    print(calculate_savings(li))
    print(calculate(li))
