class Item(object):
    def __init__(self,item_name,item_price,item_quantity):
        self.__item_name = item_name
        self.__item_price = item_price
        self.__item_quantity = item_quantity

    def GetItemName(self):
        return self.__item_name

    def GetItemPrice(self):
        return self.__item_price

    def GetItemQuantity(self):
        return self.__item_quantity

    def ChangeItemPrice(self,newprice):
        self.__item_price
class Cart:
    {item_name:[price,number]}

    def ShowCart(self):
        return self

class User(object):
    def __init__(self, name):
        self.name = name
        self.__cartlist = {}
        self.__cartlist[0] = Cart()

    def AddCart(self):
        self.__cartlist[len(self.__cartlist)] = Cart()

    def GetCart(self,cartindex = 0):
        return self.__cartlist[cartindex]

    def BuyItem(self, item, itemnum, cartindex = 0):
        try:
            self.__cartlist[cartindex][item.getItemName()][1] += itemnum
        except:
            self.__cartlist[cartindex].update({item.GetItemName():[item.getItemPrice(),itemnum]})
    def BuyCancle(self,item_name,itemnum,cartindex = 0):
        pass

    if __name__ == '__main__':

        item1 = Item('apple', 7.8, 10)
        item2 = Item('pear', 5, 1)
        user1 = User('John')

        user1.BuyItem(item1, 5)
        print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())
        user1.BuyItem(item2, 6)
        print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())

        user1.AddCart()
        user1.BuyItem(item1, 5, 1)
        print("user1 cart1 have: %s" % user1.GetCart(1).ShowCart())
        
    
    
