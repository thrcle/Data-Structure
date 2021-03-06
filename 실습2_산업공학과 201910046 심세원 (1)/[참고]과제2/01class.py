class Bag:
    def __init__(self):
        self.items = [] 

# 구현 해야할 멤버 함수 
    def contains(self, e):
        return e in self.items

    def insert(self, e):
        self.items.append(e)

    def remove(self, e):
        self.items.remove(e)

    def count(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

myBag = Bag()
myBag.insert("휴대폰")
myBag.insert("지갑")
myBag.insert("손수건")
myBag.insert('빗')
myBag.insert('연필')
print("가방속 물건: ", myBag)

myBag.insert('빗')
myBag.remove('손수건')
myBag.insert('자료 구조 책')
print("가방속 물건: ", myBag)
print("가방속 물건 갯수: %d" %myBag.count())
print("가방속 지갑 유무: %s" %myBag.contains('지갑'))
print("가방속 손수건 유무: %s" %myBag.contains('손수건'))