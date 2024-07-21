class User():
    def __init__(self, name):
        self.name = name
    
    def test_and_mark(self, article):
        return False

    def read(self,article):
        if self.test_and_mark(article):
            b = article.body
        else:
            b = "<閲覧不可>"
        print(f"{self.name}: [{article.headline}] {b}")
