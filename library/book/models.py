from django.db import models
from django.urls import reverse


class Book(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=8192)
    count = models.IntegerField(default=10)
    image = models.ImageField(upload_to='images/%Y/%m/%d', default=None, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    date_of_issue = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return f"'id': {self.id}, 'name': '{self.name}', 'description': '{self.description}', 'count': {self.count}, 'authors': {[author.id for author in self.authors.all()]}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        """
        :param book_id: SERIAL: the id of a Book to be found in the DB
        :return: book object or None if a book with such ID does not exist
        """
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id) else None

    @staticmethod
    def delete_by_id(book_id):
        """
        :param book_id: an id of a book to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if Book.get_by_id(book_id) is None:
            return False
        Book.objects.get(id=book_id).delete()
        return True

    @staticmethod
    def create(name, description, publication_year=None, count=10, authors_=None, image=None, genres_=None,
               date_of_issue=None):
        """
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
        :return: a new book object which is also written into the DB
        """
        if len(name) > 128:
            return None

        book = Book(name=name, description=description, count=count, image=image, publication_year=publication_year,
                    date_of_issue=date_of_issue)
        book.save()
        if authors_:
            for author in authors_:
                book.authors.add(author)
        if genres_:
            for genre in genres_:
                book.genres.add(genre)
        return book

    def to_dict(self):
        """
        :return: book id, book name, book description, book count, book authors
        :Example:
        | {
        |   'id': 8,
        |   'name': 'django book',
        |   'description': 'bla bla bla',
        |   'count': 10',
        |   'authors': []
        | }
        """

    def update(self, name=None, description=None, count=None):
        """
        Updates book in the database with the specified parameters.\n
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        :return: None
        """
        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if count is not None:
            self.count = count

        self.save()

    def add_authors(self, authors_):
        """
        Add  authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        if authors_ is not None:
            self.authors.add(*authors_)

    def add_genres(self, genres_):
        if genres_ is not None:
            self.genres.add(*genres_)

    def remove_authors(self, authors):
        """
        Remove authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for elem in self.authors.values():
            self.authors.remove(elem['id'])

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return list(Book.objects.all())

    def get_absolute_url(self):
        return reverse('books:single_book', kwargs={'id_book': self.pk})

    class Meta:
        db_table = 'Book'


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Genre(id={self.id}, name='{self.name}')"

    @staticmethod
    def get_by_id(genre_id):
        return Genre.objects.get(id=genre_id) if Genre.objects.filter(id=genre_id) else None

    @staticmethod
    def delete_by_id(genre_id):
        if Genre.get_by_id(genre_id) is None:
            return False
        Genre.objects.get(id=genre_id).delete()
        return True

    @staticmethod
    def get_all():
        return list(Genre.objects.all())

    class Meta:
        db_table = 'Genre'
