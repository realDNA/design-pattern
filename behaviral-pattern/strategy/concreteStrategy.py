from strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def __init__(self, cardNumber, cardExpiry, cardCvv):
        self.cardNumber = cardNumber
        self.cardExpiry = cardExpiry
        self.cardCvv = cardCvv

    def pay(self, amount):
        print(
            f"Paying {amount} using credit card ending in {self.cardNumber[-4:]}")


class PaypalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying {amount} using Paypal account {self.email}")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, walletAddress):
        self.walletAddress = walletAddress

    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin wallet {self.walletAddress}")
