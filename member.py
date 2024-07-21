from datetime import date
from user import User

class Member(User):
    def __init__(self, name):
        super().__init__(name)
        self.browsed_article = None
        self.browse_date = None

    def test_and_mark(self, article):
        if article.free:
            return True
        
        if self.browse_date == date.today():
            return self.browsed_article == article 

        self.browsed_article = article
        self.browse_date = date.today()

        return True

