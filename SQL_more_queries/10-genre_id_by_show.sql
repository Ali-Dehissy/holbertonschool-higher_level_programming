-- Listing all tvshows contained in the server that has at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
  RIGHT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
  ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
