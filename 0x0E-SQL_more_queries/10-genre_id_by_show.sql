-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title - tv_show_genres.genre_id
from tv_shows, tv_show_genres
ORDER BY tv_shows.titles, tv_show_genres.genre_id ;