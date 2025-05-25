class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
          raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
          raise ValueError("Title must be between 5 and 50 characters.")
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than o characters.")

        if not hasattr(self, '_name'):
           self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

       # pass

    def magazines(self):
        return list({article.magazine for article in self.articles()})
        # pass

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        # pass

    def topic_areas(self):
        articles_list = self.articles()
        if not articles_list:
            return None
        return list({article.magazine.category for article in articles_list})

        # pass


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be between 2 and 16 characters.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than  0 characters.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

        # pass

    def contributors(self):
        return list({article.author for article in self.articles()})
        # pass

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

       # pass
    
    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        contributors = [author for author,
                        count in author_counts.items() if count > 2]
        return contributors if contributors else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_count = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_count[magazine] = magazine_count.get(magazine, 0) + 1
        return max(magazine_count, key=magazine_count.get)



