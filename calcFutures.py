def get_tick_value(symbol):
    tick_values = {
        'MNQ': 0.50,
        'MES': 1.25,
        'MCL': 1.00
    }
    return tick_values.get(symbol, 0)

def calculate_risk(symbol, ticks, contracts):
    tick_value = get_tick_value(symbol)
    risk_per_contract = tick_value * ticks
    total_risk = risk_per_contract * contracts
    return total_risk

def main():
    print("Futures Risiko-Berechnung")

    symbols = ['MNQ', 'MES', 'MCL']
    symbol = None

    while True:
        user_input = input("'change' um den Future zu wechseln: ").strip().lower()

        if user_input == 'exit':
            break
        elif user_input == 'change' or symbol is None:
            print("Futures: MNQ, MES, MCL")
            symbol = input("Dein Future zu Handeln: ").strip().upper()
            if symbol not in symbols:
                print("Ungültiges Symbol.")
                symbol = None
                continue

        ticks = float(input(f"Ticks {symbol}? "))
        contracts = int(input(f"Kontrakte {symbol}? "))
        
        risk = calculate_risk(symbol, ticks, contracts)
        print(f"Das Risiko für {symbol} ist: ${risk:.2f}\n")

if __name__ == "__main__":
    main()
