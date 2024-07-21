class Article:
    articles = {}

    def __init__(self, id, headline, body, free):
        self.id = id
        self.headline = headline
        self.body = body
        self.free = free

    @classmethod
    def create(cls, id, headline, body, free):
        article = cls(id, headline, body, free)
        cls.articles[id] = article
        return article

    @classmethod
    def get_article(cls, id):
        return cls.articles.get(id)

    @classmethod
    def get_ids(cls):
        return cls.articles.keys()
