class Article:
    all = []

    def __init__(self, headline, body, free):
        self.headline = headline
        self.body = body
        self.free = free

    @classmethod
    def create(cls, headline, body, free):
        a = cls(headline, body, free)
        cls.all.append(a)
        return a
