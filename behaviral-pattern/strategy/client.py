from concreteStrategy import CreditCardPayment, PaypalPayment, BitcoinPayment
from context import ShoppingCart

cart = ShoppingCart()
cart.addItem("Book", 10)
cart.addItem("Pen", 2)

creditCardPayment = CreditCardPayment("12345678", "12123", "123")
paypalPayment = PaypalPayment("test@email.com")
bitcoinPayment = BitcoinPayment("0xc5faw4grg335h5hfgasfsdfas")

cart.pay(creditCardPayment)
cart.pay(paypalPayment)
cart.pay(bitcoinPayment)
