class Book:
    def __init__(self, title, genre, description, author, rating = 0, id = None):
        self.title = title
        self.genre = genre
        self.description = description
        self.author = author
        self.rating = rating
        self.id = id

    def update_rating(self, user_rating):
        self.rating = user_rating
