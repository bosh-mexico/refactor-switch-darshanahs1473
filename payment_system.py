from enum import Enum

class PaymentMode(Enum):
    PAYPAL = "PayPal"
    GOOGLEPAY = "GooglePay"
    CREDITCARD = "CreditCard"

def checkout(payment_mode, amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Error: Invalid payment amount."
    if not isinstance(payment_mode, PaymentMode):
        return "Error: Unsupported payment mode."

    print(f"Processing {payment_mode.value} payment of ${amount:.2f}...")

    if payment_mode == PaymentMode.PAYPAL:
        return f"Payment of ${amount:.2f} processed via PayPal."
    elif payment_mode == PaymentMode.GOOGLEPAY:
        return f"Payment of ${amount:.2f} processed via GooglePay."
    elif payment_mode == PaymentMode.CREDITCARD:
        return f"Payment of ${amount:.2f} processed via CreditCard."
    else:
        return "Error: Unsupported payment mode."
