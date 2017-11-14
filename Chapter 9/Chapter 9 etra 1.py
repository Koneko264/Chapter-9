class Cell:

    def __init__(self):
        self.manufact = ''
        self.model = ''
        self.retail_price = ''

    def set_manufact(self, manufact):
        self.manufact = manufact
        

    def set_model(self, model):
        self.model = model

    def set_retail_price(slef, retail_price):
        self.retail_price = retail_price
    def get_manufact(self):
        return self.manufact
    def get_model(self):
        return self.model
    def get_retial_price(self):
        return self.retail_price


        
Cell = Cell()
Cell.manufact = str(input('Enter the manufacturer:'))
Cell.model = str(input('Enter the model number:'))
Cell.retail_price = str(input('Enter the retail price:'))

print('Here is the data that you entered:')
print('Manufacturer:',Cell.manufact)
print('Model Number:',Cell.model)
print('Retail Price:',Cell.retail_price)


