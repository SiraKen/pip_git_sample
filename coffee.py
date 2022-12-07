def japanese(amount):
    return f'コーヒーを{amount}杯ください'


def german(amount):
    if amount < 2:
        return 'Ich möchte einen Kaffee bitte.'
    return f'Ich möchte {amount} Kaffee bitte.'
