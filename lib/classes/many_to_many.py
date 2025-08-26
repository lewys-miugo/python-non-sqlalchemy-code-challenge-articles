class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        # Title is immutable, so we don't allow setting it
        pass
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        # Name is immutable, so we don't allow setting it
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set([magazine.category for magazine in magazines]))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set([article.author for article in articles]))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
            
        author_count = {}
        for article in articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
                
        contributing = [author for author, count in author_count.items() if count > 2]
        return contributing if contributing else None