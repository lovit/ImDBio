# ImDBio: data reader

Reader yields three columns as tuple format (idx, title, text)

File reader.

```python
from imdbio import ReviewsReader

review_path = 'reviews.txt'
reviews_reader = ReviewsReader(review_path, num_review=10)

for idx, title, text in reviews_reader:
    print((idx, title, text[:100]))
```

    ('1482', 'It is not a very cheerful picture', 'This picture lingers on the sordid miseries in the home of a man who drinks and is brutal when drunk'),
    ('1587', ;A Very Important Spanish Pioneer Film Director', 'Many times an entire life once filled with merit and achievement quickly becomes forgotten after jus'),    
    ...

Change yield format

```python
reviews_reader.yield_idx = False
reviews_reader.yield_title = False
for text in reviews_reader:
    print(text[:100])
```

    This picture lingers on the sordid miseries in the home of a man who drinks and is brutal when drunk
    Many times an entire life once filled with merit and achievement quickly becomes forgotten after jus
    ...

Directory reader.

```python
directory_reader = ReviewDirectoryReader(directory, num_review=10)
```