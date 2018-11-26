# ImDB review and metdata

- 총 여섯 개의 파일로 구성
- 2016년 10월에 수집한 데이터
- 장르나 제작 국가가 포함되지 않은 영화가 존재

## Column info

모든 column 은 tap separated 로 구분되어 있으며, headless 임

| file | column |
| --- | --- |
| genre.txt | movie_id, genre |
| movie_countries.txt | movie_id, country |
| movie.txt | movie_id, title, created_year |
| people_acting.txt |  actor_id, movie_id, actor_name, character_name, credit_order |
| people_directing.txt | director_id, movie_id, director_name |
| reviews.txt | movie_id, title, text |

reviews.txt 의 text 에는 tap 이 포함되어 있지 않으며, 텍스트에 존재하는 줄바꿈 기호 \n 은 두 칸 띄어쓰기 '  ' 로 대체되었음

## reviews (directory)

영화 리뷰는 각 영화별 파일로 분할되어 저장되어 있으며, reviews.txt 는 reviews 디렉토리의 모든 파일이 하나로 합쳐진 버전. 각 영화별 리뷰 파일은 tap separated 인 두 개의 columns 으로 구성되어 있으며, headless 임

| column | note |
| --- | --- |
| title | 영화 제목 |
| text | 영화 리뷰이며, tap 이 포함되어 있지 않으며 텍스트에 존재하는 줄바꿈 기호 \n 은 두 칸 띄어쓰기 '  ' 로 대체되었음 |