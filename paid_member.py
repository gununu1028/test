from member import Member

class PaidMember(Member):
    def __init__(self, name):
        super().__init__(name)

    def test_and_mark(self, article):
        return True

