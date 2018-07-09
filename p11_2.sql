.mode column
.headers on
SELECT bookCreator.bookId, creator.name FROM bookCreator
INNER JOIN creator
ON bookCreator.creatorId=creator.id
WHERE bookId=4;
