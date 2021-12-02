class Payment:
    def __init__(self):
        pass

    def setPayment(self, payment):
        Payment.payment = payment

    def getPayment(self):
        print("Total yang harus dibayarkan Rp. ", Payment.payment)
