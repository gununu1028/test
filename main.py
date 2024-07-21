# 平成26年度春期

from article import Article
from member import Member
from paid_member import PaidMember

readers = [Member("A"), PaidMember("B")]

# 記事の作成
Article.create("PC入門", "PC初心者...", False)
Article.create("スマホ特集", "最新のスマホ...", False)
Article.create("アプリガイド", "使えるアプリ...", False)

# ユーザーごとに記事をテストして表示
for reader in readers:
    for a in Article.all:
        reader.read(a)
    reader.read(Article.all[0])