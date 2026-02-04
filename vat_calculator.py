# ==========================================
# VAT CALCULATOR - OPTIMISEZ VERSION
# ==========================================

def calculate_vat(net_amount, vat_rate=20.0):
    """
    Calcule la TVA et le prix total.
    net_amount : montant net
    vat_rate : taux de TVA (par défaut 20%)
    Retourne : (tax_to_pay, total_price)
    """
    tax_to_pay = net_amount * (vat_rate / 100)
    total_price = net_amount + tax_to_pay
    return tax_to_pay, total_price


# --- 1. USER INPUT ---
raw_amount = input("Enter the net amount (e.g. 100): ")
raw_rate = input("Enter the VAT rate % (press Enter for 20%): ")

# --- 2. LOGIC AND CALCULATION ---
try:
    net_value = float(raw_amount)
    tax_rate = float(raw_rate) if raw_rate else 20.0

    tax_to_pay, total_price = calculate_vat(net_value, tax_rate)

    # --- 3. DISPLAY RESULTS ---
    print("\n" + "*"*25)
    print("   TAX CALCULATOR")
    print("*"*25)
    print("\nCALCULATION SUMMARY:")
    print(f"- Net Amount:   ${net_value:.2f}")
