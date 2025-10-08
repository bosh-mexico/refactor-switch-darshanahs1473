import unittest
from payment_system import checkout, PaymentMode

class TestPaymentSystem(unittest.TestCase):
    def test_paypal_payment(self):
        self.assertEqual(checkout(PaymentMode.PAYPAL, 150.75), "Payment of $150.75 processed via PayPal.")

    def test_googlepay_payment(self):
        self.assertEqual(checkout(PaymentMode.GOOGLEPAY, 99.99), "Payment of $99.99 processed via GooglePay.")

    def test_creditcard_payment(self):
        self.assertEqual(checkout(PaymentMode.CREDITCARD, 200), "Payment of $200.00 processed via CreditCard.")

    def test_invalid_payment_mode(self):
        self.assertEqual(checkout("CASH", 100), "Error: Unsupported payment mode.")

    def test_invalid_amount(self):
        self.assertEqual(checkout(PaymentMode.PAYPAL, -50), "Error: Invalid payment amount.")

    def test_non_numeric_amount(self):
        self.assertEqual(checkout(PaymentMode.GOOGLEPAY, "Fifty"), "Error: Invalid payment amount.")

if __name__ == "__main__":
    unittest.main()
