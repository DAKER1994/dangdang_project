from xmapp import views
from xmapp.models import TBook


class Cartitem():
    def __init__(self,book,amount):
        self.amount = amount
        self.book = book
        self.status = 1

class Cart():
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cartitem = []

    def sums(self):
        self.total_price = 0
        self.save_price = 0
        print(self.cartitem)
        for i in self.cartitem:
            self.total_price += i.book.dd_pricing * i.amount
            self.save_price += (i.book.pricing - i.book.dd_pricing) * i.amount

    # 向购物车中添加书籍
    def add_book_toCart(self, book,num):
        for i in self.cartitem:
            if i.book.id == int(book):
                i.amount += int(num)
                self.sums()
                return
        book = TBook.objects.filter(id=book)[0]
        self.cartitem.append(Cartitem(book, num))
        self.sums()

    # 修改购物车的商品信息
    def modify_cart(self, book, amount,bookid):
        bookid =TBook.objects.all(pk=id)
        for i in self.cartitem:
            if i.book.id == bookid:
                i.amount = amount
        self.sums()


    # 删除购物车
    def delete_book(self, bookid):
        for i in self.cartitem:
            if i.book.id == int(bookid):
                # 修改书的状态
                self.cartitem.remove(i)
        self.sums()


