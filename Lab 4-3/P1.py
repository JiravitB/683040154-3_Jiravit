"""
Jiravit Boonyaritchaikit
683040154-3
P1
"""

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self.__checked_out = False
    
    def get_status(self):
        return "Checked out" if self.__checked_out else "Available"
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self.__checked_out:
            self.__checked_out = True
            return True
        # can't check out if item not in lib
        return False
    
    def return_item(self):
        if self.__checked_out:
            return True
        return False

# implement 3 classes here
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0

    def set_pages_count(self, pages):
        self.pages_count = pages

    def display_info (self):
        return f"Titie: {self.title}Author: {self.author}pages: {self.pages_count}checkout status: {self.get_status()}" 
        

class Textbook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author,)
        self.subject = subject
        self.grade_level  = grade_level 

    def display_course_info(self):
        return f"Titie: {self.title}\nAuthor: {self.author}\nPages: {self.pages_count}\nSubject: {self.subject}\nacademic_Level: {self.grade_level}\ncheckout status: {self.get_status()}" 


class Magazine(LibraryItem): 
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.month = 1
        self.year = 2026
    
    def display_issue(self):
        return f"Title: {self.title}\nIssue_number: {self.issue_number}\nMonth: {self.month}\nYear: {self.year}\ncheckout_status: {self.get_status()}"


# Test your code:
print("-------book------")
book0 = Book("best","000", "best")
book0.set_pages_count(1000)
print(book0.display_info())

print("-------textbook------")
textbook1 = Textbook("kkk", "111", "klao", "math", "A+")
print(textbook1.display_course_info())

print("-------magazine------")
magazine1 = Magazine("MSG", "222", "01")
print(magazine1.display_issue())


book0.check_out()
textbook1.check_out()
magazine1.check_out()
print("-------CheckOut------")
print(book0.display_info())
print(textbook1.display_course_info())
print(magazine1.display_issue())


print("-------Retrun------")
book0.return_item()
print(book0.display_info())
print("---------------------")
# This is just an example. You should test a lot more than this.

book = Book("Harry Potter", "B001", "J.K. Rowling")
print(book.get_status())  # Should print: Available
book.check_out()
print(book.get_status())  # Should print: Checked out
