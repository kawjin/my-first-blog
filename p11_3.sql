.mode column
.headers on
SELECT book.title, creator.name FROM bookCreator
INNER JOIN creator
ON bookCreator.creatorId=creator.id
INNER JOIN book
ON bookCreator.bookId=book.id
WHERE title='プログラミング作法';
