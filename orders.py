def shipping_fee(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    return 0 if subtotal >= 300_000 else 30_000


def apply_coupon(subtotal, code):
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if code == "SAVE10":
        discount = min(subtotal // 10, 50_000)
        return subtotal - discount
    return subtotal
