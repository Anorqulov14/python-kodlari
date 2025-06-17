class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = {}     
        self.members = {}   

    def getName(self):
        return self.name

    def addBook(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"{quantity} ta '{title}' kitobi qo‘shildi.")

    def lendBook(self, member, title):
        if title not in self.books:
            print(f"'{title}' kitobi mavjud emas.")
            return
        if self.books[title] == 0:
            print(f"'{title}' kitobidan nusxa qolmagan.")
            return
        if member in self.members and title in self.members[member]:
            print(f"{member} allaqachon '{title}' kitobini olgan.")
            return

        self.books[title] -= 1
        if member in self.members:
            self.members[member].append(title)
        else:
            self.members[member] = [title]
        print(f"{member}ga '{title}' kitobi berildi.")

    def returnBook(self, member, title):
        if member not in self.members or title not in self.members[member]:
            print(f"{member}da '{title}' kitobi mavjud emas.")
            return

        self.books[title] += 1
        self.members[member].remove(title)
        if not self.members[member]:
            del self.members[member] 
        print(f"{member}dan '{title}' kitobi qabul qilindi.")

