def shipping_fee(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    return 0 if subtotal >= 300_000 else 30_000
