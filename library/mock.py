import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()


import argparse
import pytz
import datetime
from authentication.models import CustomUser
from author.models import Author
from book.models import Book, Genre
from order.models import Order
from itertools import cycle, islice

TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)


def _add_default_data():
    data_for_users = [
        ('root@admin.com', 'root123', 'Admin', 'Root', 'Superuser', 1, True, True, True),
        ('librarian_1@example.com', 'pasword123!@#', 'Klaudia', 'Petrivna', 'librarian_1', 0, True, True, False),
        ('librarian_2@example.com', 'pasword123!@#', 'Olga', 'Nikolaevna', 'librarian_2', 0, True, True, False),
        ('user_1@example.com', 'pasword123!@#', 'Oleksandr', 'Oleksandr', 'user_1', 0, True, False, False),
        ('user_2@example.com', 'pasword123!@#', 'Alex', 'Alex', 'user_2', 0, True, False, False),
        ('user_3@example.com', 'pasword123!@#', 'Ivan', 'Ivan', 'user_3', 0, True, False, False),
    ]
    users = []
    for email, password, first_name, middle_name, last_name, role, is_active, is_staff, is_superuser in data_for_users:
        user = CustomUser(email=email, password=password, first_name=first_name,
                          middle_name=middle_name, last_name=last_name, role=role,
                          created_at=TEST_DATE, updated_at=TEST_DATE, is_active=is_active,
                          is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save()

        print('created user -> ', user)
        users.append(user)

    data_for_authors = [
        (1, 'Eric', 'Matthes', ' '),
        (2, 'Al', 'Sweigart', ' '),
        (3, 'Mark', 'Lutz', ' '),
        (4, 'Paul', 'Barry', ' '),
        (5, 'Bill', 'Lubanovic', ' '),
        (6, 'Dan', 'Bader', ' '),
        (7, 'David', 'Amos', ' '),
        (8, 'Joanna', 'Jablonski', ' '),
        (9, 'Fletcher', 'Heisler', ' '),
        (10, 'Jamie', 'Chan', ' '),
        (11, 'Allen', 'Downey', ' '),
        (12, 'Timothy', 'Needham', 'C.'),
        (13, 'Zed', 'Shaw', ' '),
        (14, 'Patrick', 'Rothfuss', ' '),
        (15, 'Brandon', 'Sanderson', ' '),
        (16, 'George', 'R.R. Martin', ' '),
        (17, 'J.R.R.', 'Tolkien', ' '),
        (18, 'SOME', 'AUTHOR', 'DELL'),
        (19, 'Frank', 'Herbert', ' '),
        (20, 'William', 'Gibson', ' '),
        (21, 'Ursula K.', 'Le Guin', ' '),
        (22, 'Isaac', 'Asimov', ' '),
        (23, 'H.G.', 'Wells', ' ')
    ]
    authors = dict()
    for i, name, surname, patronymic in data_for_authors:
        author = Author.create(name=name, surname=surname, patronymic=patronymic)
        print('created author -> ', author)
        authors[i] = author

    data_for_genres = [
        'IT', 'Fantasy', 'Science Fiction',
    ]

    genres = []
    for g in data_for_genres:
        genre = Genre(name=g)
        genre.save()
        print('created genre -> ', genre)
        genres.append(genre)

    data_for_books = [
        ('Python Crash Course (3rd Edition)', 2023, '2023-05-15',  (authors.get(1),), (genres[0],), 'images/default/1_Crash.jpg',
         """Let’s kick off with one of the most popular Python books available, Python Crash Course, by Eric Matthes.
When I was starting out with Python, this was one of the first books I picked up, and it seems I wasn't alone!
With more than 1.5 million copies sold, this book’s clear and concise teaching has made it a firm favorite among aspiring Python developers.
The first thing I have to say is that you won't yawn through endless pages, as this Python book is more of a well-paced sprint through Python essentials.
I also appreciate that it’s split into two halves, with the first solidifying your understanding of basics like loops and classes with clear examples and exercises.
With the fundamentals of Python down, the second half is where you shine by building three Python projects to bolster your portfolio and coding chops.
What about the teaching style? It’s hands-on with a learn-by-doing approach. I love this, as there's no substitute for putting theory into practice. It’s also packed with exercises to test and build your skills.
You can also expect to get to grips with libraries like Pygame for games, Matplotlib and Plotly for data visualization, and Django for web apps.
It’s also really nice to see Matthes using Python 3.11 in the updated edition. He also embraces VS Code as the preferred Python IDE.
In my opinion, this is a no-brainer for beginners but robust enough for pros to brush up their skills.
It’s also clear in the user reviews that readers like the practical approach and clear instructions, making this an ideal Python programming launchpad.
Standout Features:
Best-seller status with an author who knows how to teach.
Real-life projects that make your resume pop
Up-to-date with Python 3.11 and modern tools."""),
        ('Automate the Boring Stuff with Python (2nd Edition)', 2019, '2019-11-12', (authors.get(2),), (genres[0],), 'images/default/2_Automate.jpg',
         """Time to dive into another popular Python book, Automate the Boring Stuff with Python by Al Sweigart.
I have to admit, this is another one that I picked up when I was starting, as I was drawn to the idea of automating.
After all, who doesn’t want to harness Python to make their life easier?!
One of the best features of this book is Sweigart's approach to teaching, as he makes it easy for beginners and those without prior coding experience. He even has a related Python course on Udemy.
This Python book walks you through each program with detailed instructions, and updated projects at the end of each chapter put your skills to the test.
This is always music to my ears, as there is no substitute for learning Python by doing, and what better way than with real-world tasks that you can relate to.
Plus, you get the fringe benefit of freeing up your time.
In general, the goal of this book is simple: to teach coding in a way that directly impacts your efficiency and productivity.
I also appreciate the fact that the updated edition offers new chapters on input validation, automating Gmail and Google Sheets, and more.
It’s also obvious from the user reviews that aspiring Pythonistas appreciate the emphasis on making coding directly applicable to everyday life.
Whether you're a Python newbie or looking to streamline your workflow, this book's a solid pick.
Standout Features:
Turns tedious tasks into Python practice.
New content on input validation and Google automation.
Step-by-step instructions that build your coding muscles.
Updated projects that challenge you to apply what you’ve learned."""),
        ('Learning Python (5th Edition)', 2013, '2013-06-24', (authors.get(3),), (genres[0],), 'images/default/3_Lutz.jpg',
         """This is no skimpy pamphlet or Python cheat sheet!
We're talking about a comprehensive deep-dive into Python that’s over 1600 pages long, and it’s another that I added to my bookshelf when starting out. 
Whether you're a newcomer or a seasoned dev looking to expand your Python prowess, this book is a real treasure trove.
And while it may be a few years old, the core material is as relevant today as it was when the book was published.
Not only does it pack a punch with quizzes, exercises, and illustrations, but Lutz's teaching style is interactive and self-paced. 
Given its truly mammoth length, it’s quite a time investment, but one that pays off if you’re serious about Python.
Expect to go deep into general syntax, Python operators, built-in object types, and classes for object-oriented programming.
I really appreciated the strong emphasis on functions to avoid code redundancy, organizing code into modules, and Python’s exception-handling model.
These are essential skills for pro developers, so it makes sense to learn them early. 
You’ll also dive into more advanced features like decorators, descriptors, metaclasses, and Unicode processing. 
The goal of this book isn’t to merely learn Python but to master Python.
That said, I also think it’s an essential reference book to have on hand whenever you need to brush up on a particular topic, whether that's finding a Python substring or creating your own OOP class.
As for user reviews, readers really like the depth of content and the clarity of explanations. 
Standout Features:
Broad and deep exploration of Python.
Interactive learning with quizzes and exercises rather than passive reading.
Insights into advanced Python features."""),
        ('Head-First Python (2nd Edition)', 2020, '2020-08-18', (authors.get(4),), (genres[0],), 'images/default/4_Head_First.jpg',
         """This is one of the most unique Python books on our list and another of my favorites.
If you’re unfamiliar with the Head-First series, the idea is to engage your brain visually and practically. 
Yep, forget slogging through dense manuals! This brain-friendly guide is all about taking a hands-on dive into Python.
You'll start with Python's fundamentals, like Python lists and functions, and then apply what you've learned by building a web application, managing databases, and handling exceptions. 
It's also packed with Pythonic tools like context managers, decorators, comprehensions, and generators.
These are some of my favorite aspects of coding in Python, so I really appreciated the fact that they try to encourage learners to use them early.
I also like the fact that it includes exercises and quizzes at the end of each chapter to test your understanding of the material.
If you want a book that makes learning Python enjoyable and less of a chore, this is definitely a solid choice that’s well-liked by existing readers. 
Standout Features:
A visual, engaging approach based on cognitive science and learning theory.
Practical, hands-on exercises building up to a complete web application.
Coverage of essential Python features for real-world programming.
A unique format that makes learning Python intuitive and fun."""),
        ('Introducing Python (2nd Edition)', 2019, '2019-10-22', (authors.get(5),), (genres[0],), 'images/default/5_Introducing.jpg',
         """This is an excellent choice for newcomers to programming who want to start with Python or are taking a Python course.
The main feature that really stands out about this Python book is the author’s methodical yet engaging approach.
Aiming at beginners, you’ll work through the basics and onto more complex subjects with a mix of tutorials and cookbook-style code recipes.
I really like this approach, as it’s ideal for hands-on learning. Which, if you haven’t guessed, is something I’m a big fan of!
I also appreciate the end-of-chapter exercises that allow you to practice what you've learned. 
Overall, this Python book stands out for its ability to teach a robust foundation in Python, including best practices for testing, debugging, and code reuse.
In my opinion, these are all critical skills for real-world programming, so kudos to the author for including them.
To round things out, it also shows you how to apply Python in various fields, such as business, science, and the arts.
This even includes sections on leveraging the vast ecosystem of Python packages. This is a nice touch, as it shows that the author appreciates Python's versatility.
Standout Features:
Blend of foundational tutorials and practical code recipes.
Engaging writing style that makes learning Python enjoyable.
Comprehensive coverage of Python with end-of-chapter exercises.
Covers Python's application in various fields with a variety of tools.
"""),
        ('Python Basics: A Practical Introduction to Python (1st Edition)', 2022, '2022-04-11', (authors.get(6), authors.get(7), authors.get(8), authors.get(9)), (genres[0],), 'images/default/6_Basics.jpg',
         """Whether you're completely new to coding or a seasoned dev who wants to learn Python, this is a well-structured and practical introduction.
I also like the sample projects the authors have included, as this ensures you're not just reading about Python but actively learning and applying it.
I’ll say it over and over: this is one of the most important things about learning Python. Code, build, and get practical!
Something that stood out to me about this Python book is the way it’s structured to build your understanding incrementally.
Expect to cover foundational topics like data structures and control flow before venturing into advanced territories like object-oriented programming (OOP).
You’ll also tackle file I/O, working with databases, and even scientific computing and data visualization with NumPy and Matplotlib.
It also covers the basics of creating and modifying PDF files, interacting with the web, and building graphical user interfaces (GUIs). 
Another strong point of this Python book is the interactive quizzes and exercises. These are ideal for reinforcing learning while also making it fun and engaging to measure progress. 
It’s also nice to see the authors include solutions to compare your approach with professional standards.
Standout Features:
Chapters dedicated to fundamental programming concepts.
Interactive quizzes and practical exercises with solutions.
Covers a broad range of applications, from web scraping to GUI creation."""),
        ('Learn Python in One Day and Learn It Well (2nd Edition)', 2020, '2020-01-17', (authors.get(10),), (genres[0],), 'images/default/7_One_day.jpg',
         """I guess the main question is, can you really learn Python in one day with this book?!
In my opinion, maybe! But you should probably be prepared to spend a lot more than one day truly mastering Python, especially if you’re totally new to programming.
That said, I appreciate that this Python book makes the learning process both swift and enjoyable!
One of this book’s main strengths is that the author breaks down complex concepts into digestible steps. This is essential for absolute beginners to grasp the nuances of Python.
Now, bear in mind that at less than 200 pages long, it’s more of a primer than a truly comprehensive guide to learning Python.
Despite the short length, you can expect a hands-on approach to learning basics like variables, data types, user inputs, iteration, errors, functions, modules, and OOP.
I also appreciate the inclusion of step-by-step instructions and practical examples to help you retain the material.
A standout feature for me is the emphasis on real-world applications, as the author has included Python concepts for data, web development, and machine learning.
Overall, if you're looking to dive into Python but are short on time, this book is for you. 
Standout Features:
Concise breakdown of Python for beginners.
Real-world examples for quick and effective learning.
Curated selection of topics to cover essential skills
Hands-on project to encapsulate concepts and reinforce learning.
"""),
        ('Think Python (2nd Edition)', 2015, '2015-03-27', (authors.get(11),), (genres[0],), 'images/default/8_Think.jpg',
         """If you're looking for a Python book that combines practical programming with essential software development principles, Think Python is a fine choice. 
This is also one of my favorite Python books, as it’s short, to the point, and practice-oriented.
I also like the author’s writing style when introducing computer science fundamentals. It really is one of the most thorough options for beginners despite its modest length.
If you want to understand programming beyond syntax and semantics, definitely give this one a try!
It's also a great way to level up your knowledge of Python concepts for interviews.
One of the main strengths of this book is the balance of practical coding exercises with fundamental software development concepts. 
Expect to start with basic programming concepts before taking on Python specifics, like functions, recursion, data structures, and object-oriented design. 
In my opinion, this book is ideal if you want to gain a solid foundation in programming with Python while also learning to think like a computer scientist. 
Standout Features:
A thorough introduction to computer science with Python.
Programming concepts are clearly defined and logically progressed.
Practical exercises in every chapter, with case studies for in-depth learning.
Covers how to think algorithmically and solve programming tasks."""),
        ('Python: For Beginners (1st Edition)', 2021, '2021-09-14', (authors.get(12),), (genres[0],), 'images/default/9_Beginners.jpg',
         """Whether you're just starting out, returning to coding after a break, or a professional who needs a quick primer, this Python book is an excellent choice.
And at only 135 pages, it’s one of the very shortest books on our list.
I also appreciate that the author takes a pragmatic approach to programming, emphasizing the importance of thinking like a programmer. 
For me, this is one of the most important skills for newcomers, so it’s great to see the author baking this in.
And while it’s not promising to teach you Python in a single day, it is designed to let beginners learn basic Python in seven days.
This is something I can believe because even if you’ve never coded in your life, you can definitely learn the core skills in one week.
Interestingly, despite its modest length, this Python book is relatively comprehensive, with chapters on loops, data types, dictionaries, and more.
You’ll also touch on advanced topics like object-oriented programming, file I/O, and regular expressions, not to mention the section on best practices for Python development.
It’s also great to see hands-on coding projects, which I think are essential for bringing new concepts to life. 
Standout Features:
Covers Python essentials such as loops, data types, and object-oriented programming.
Step-by-step guidance to take a newcomer from installation to coding their own projects.
Practical exercises cement new Python skills in a fun and engaging way."""),
        ('Learn Python 3 the Hard Way (1st Edition)', 2020, '2020-07-30', (authors.get(13),), (genres[0],), 'images/default/10_Hard_way.jpg',
         """The first thing that stood out to me about this book was the title! I mean, who wants to do things the hard way, right?
It’s probably why I picked this book up myself, as I just had to know how hard it would be?
Turns out, it's not that hard! 
If you’re not familiar with the author, Zed Shaw’s method combines discipline and persistence with 52 practical exercises ranging from basic math to web development. 
Expect to cover fundamentals like variables, data types, user input, file I/O, data structures, and advanced topics like object-oriented programming and modules.
You’ll even learn about Python packaging, automated testing, and basic game development.
But what makes this such a good Python book is that it’s designed for those who prefer to learn by doing. 
This means writing out every line of code yourself, avoiding all copy-pasting, and switching off any autocomplete features.
The idea is to truly learn Python by getting the code under your fingers. This is something I wholeheartedly agree with, as it’s all so easy to rely on your IDE to do the coding for you.
And with the growing availability of AI coding assistants, the temptation is even greater for beginners to rely on AI autocompletions when learning Python.
Overall, I'd say it's much easier to avoid common Python mistakes if you make them and then learn from them.
I also like that it goes beyond plain coding, delving into how computers work, program design, and the intricacies of Python.
You can even access more than 5 hours of complementary video content. 
Standout Features:
52 real-world exercises for hands-on learning.
Emphasis on manual coding to improve precision and understanding.
Additional video content for an enriched learning experience.
Suitable for learners of all levels, from beginners to seasoned professionals."""),

        ('The Name of the Wind', 2007, '2007-03-27', (authors.get(14),), (genres[1],), 'images/default/11_Name_of_the_Wind.jpg',
         """'The Name of the Wind' by Patrick Rothfuss is a masterpiece of modern fantasy literature. 
The novel tells the story of Kvothe, a magically gifted young man who grows up to become a legend. Rothfuss's writing is poetic, and his world-building is intricate and immersive.
The book is celebrated for its complex characters, rich lore, and compelling narrative. 
It's a must-read for any fantasy fan looking for a deep, character-driven story with a touch of magic.
Standout Features:
Intricate world-building and rich lore.
Compelling, character-driven narrative.
Beautiful, poetic prose that brings the story to life."""),
        ('The Way of Kings', 2010, '2010-08-31', (authors.get(15),), (genres[1],), 'images/default/12_Way_of_Kings.jpg',
         """'The Way of Kings' is the first book in Brandon Sanderson's epic fantasy series, 'The Stormlight Archive.' 
Sanderson is known for his meticulous world-building and complex magic systems, and this book is no exception.
The story follows multiple characters across a vast and war-torn world, each with their own unique journey and struggles. 
The book is a hefty read, but it’s packed with action, intrigue, and breathtaking world-building. 
Standout Features:
Epic world-building with a unique magic system.
Multiple intertwining character arcs.
A rich, detailed narrative that rewards patient readers."""),
        ('A Song of Ice and Fire: A Game of Thrones', 1996, '1996-08-06', (authors.get(16),), (genres[1],), 'images/default/13_Game_of_Thrones.jpg',
         """George R.R. Martin's 'A Game of Thrones' is the first book in the 'A Song of Ice and Fire' series, which has become a cultural phenomenon.
The book is known for its complex characters, political intrigue, and shocking plot twists. 
Martin's world is gritty, realistic, and morally ambiguous, making it a fascinating read for those who enjoy dark, character-driven fantasy.
The novel sets the stage for the epic saga that follows, introducing readers to the brutal and unpredictable world of Westeros.
Standout Features:
Complex characters with morally gray motivations.
Intricate political intrigue and unpredictable plot twists.
A richly detailed, gritty fantasy world."""),
        ('The Hobbit', 1937, '1937-09-21', (authors.get(17),), (genres[1],), 'images/default/14_The_Hobbit.jpg',
         """J.R.R. Tolkien's 'The Hobbit' is a timeless classic that has captivated readers of all ages for decades.
The story follows the journey of Bilbo Baggins, a reluctant hero who embarks on an adventure with a group of dwarves to reclaim their homeland from a fearsome dragon.
Tolkien's writing is charming and whimsical, and his world-building is unparalleled. 
The book is a perfect introduction to the world of Middle-earth, filled with adventure, humor, and heart.
Standout Features:
Timeless, classic storytelling.
Rich, imaginative world-building.
A light-hearted adventure with a charming protagonist."""),
        ('Mistborn: The Final Empire', 2006, '2006-07-17', (authors.get(15),), (genres[1],), 'images/default/15_Mistborn.jpg',
         """'Mistborn: The Final Empire' is the first book in Brandon Sanderson's 'Mistborn' trilogy, known for its unique magic system and intricate plot.
The story is set in a world where ash falls from the sky, and mist dominates the night, ruled by a tyrannical immortal emperor.
Sanderson's magic system, based on the ingestion of metals, is one of the most creative in fantasy literature.
The book is a fast-paced, action-packed tale of rebellion, with a strong female protagonist and plenty of twists and turns.
Standout Features:
Unique, well-defined magic system.
Engaging, fast-paced plot with strong characters.
Creative world-building with a dark, oppressive atmosphere."""),

        ('Dune', 1965, '1965-08-01', (authors.get(19),), (genres[2],), 'images/default/16_Dune.jpg',
         """Frank Herbert's 'Dune' is a science fiction epic that has influenced countless works in the genre.
Set in a distant future amidst a sprawling interstellar empire, the story follows Paul Atreides as he navigates political intrigue, betrayal, and the harsh desert planet of Arrakis.
'Dune' is known for its complex themes, including politics, religion, and ecology, as well as its intricate world-building and compelling characters.
Standout Features:
Epic, intricate world-building with complex themes.
A mix of political intrigue, science fiction, and adventure.
Influential, genre-defining work."""),
        ('Neuromancer', 1984, '1984-07-01', (authors.get(20),), (genres[2],), 'images/default/17_Neuromancer.jpg',
         """'Neuromancer' by William Gibson is a cyberpunk classic that has defined the genre.
The novel is set in a dystopian future where corporate power dominates and technology blurs the line between human and machine.
The story follows Case, a washed-up computer hacker hired for one last job, navigating a world of artificial intelligence, cybernetic implants, and virtual realities.
Gibson's vision of the future is both chilling and prescient, making 'Neuromancer' a must-read for science fiction fans.
Standout Features:
A defining work of cyberpunk literature.
Exploration of themes like artificial intelligence and the merging of man and machine.
A fast-paced, gritty narrative set in a dystopian future."""),
        ('The Left Hand of Darkness', 1969, '1969-03-01', (authors.get(21),), (genres[2],), 'images/default/18_Left_Hand.jpg',
         """Ursula K. Le Guin's 'The Left Hand of Darkness' is a groundbreaking work of science fiction that explores themes of gender, society, and human nature.
The story is set on the planet Gethen, where the inhabitants can change their gender at will, and follows an envoy from Earth as he navigates the complexities of this unique society.
Le Guin's writing is thought-provoking and poetic, making 'The Left Hand of Darkness' a profound exploration of what it means to be human.
Standout Features:
Exploration of complex themes like gender and society.
A unique, imaginative setting with rich world-building.
Poetic, thought-provoking prose."""),
        ('Foundation', 1951, '1951-06-01', (authors.get(22),), (genres[2],), 'images/default/19_Foundation.jpg',
         """Isaac Asimov's 'Foundation' is the first book in a series that has become a cornerstone of science fiction literature.
The novel follows the efforts of a group of scientists who seek to preserve knowledge and culture as the Galactic Empire collapses.
Asimov's vision of a future empire spanning the galaxy is grand in scale, and his exploration of the social sciences is both innovative and intriguing.
'Foundation' is a must-read for anyone interested in the future of human civilization.
Standout Features:
Epic in scale, with a grand vision of the future.
Exploration of social sciences in a science fiction context.
A foundational work in the genre."""),
        ('The War of the Worlds', 1898, '1898-01-01', (authors.get(23),), (genres[2],), 'images/default/20_War_of_the_Worlds.jpg',
         """H.G. Wells' 'The War of the Worlds' is a classic science fiction novel that has stood the test of time.
The story of an alien invasion of Earth and humanity's struggle for survival is both thrilling and terrifying.
Wells' writing is both engaging and thought-provoking, making this novel a timeless exploration of human nature, fear, and survival.
'The War of the Worlds' has inspired countless adaptations and remains a seminal work in the science fiction genre.
Standout Features:
A thrilling and terrifying alien invasion story.
Engaging, thought-provoking exploration of human nature.
A seminal work that has influenced countless science fiction works.""")
    ]
    books = []
    for name, publication_year, date_of_issue, authors, genres, image, description in data_for_books:
        book = Book.create(name=name, publication_year=publication_year, authors_=authors, description=description,
                           image=image, genres_=genres, date_of_issue=date_of_issue)
        books.append(book)
        print('created book -> ', book.name, ' authors ->', [x.name for x in book.authors.all()])

    casual_users = islice(cycle(users[3:]), len(books))
    for user, book in zip(casual_users, books):
        order = Order.create(user, book, TEST_DATE)
        print('created order -> ', order)


def _delete_all_data():
    for order in Order.get_all():
        print('delete order.id = ', order.pk)
        Order.delete_by_id(order.pk)

    for book in Book.get_all():
        print('delete book.id = ', book.pk)
        Book.delete_by_id(book.pk)

    for author in Author.get_all():
        print('delete author.id = ', author.pk)
        Author.delete_by_id(author.pk)

    for user in CustomUser.get_all():
        print('delete user.id = ', user.pk)
        CustomUser.delete_by_id(user.pk)

    for genre in Genre.get_all():
        print('delete genre.id = ', genre.pk)
        Genre.delete_by_id(genre.pk)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add_default_data', help='add default data', action='store_true')
    parser.add_argument('-d', '--delete_all_data', help='deletes all data', action='store_true')
    args = parser.parse_args()

    if args.add_default_data:
        _add_default_data()
    if args.delete_all_data:
        _delete_all_data()
