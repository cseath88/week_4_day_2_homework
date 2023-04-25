from db.run_sql import run_sql

from models.artist import Artist

from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all_albums():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_album(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['artist_id'], result['genre'], result['id'])
    return album

def select_all_albums():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['artist_id'], row['genre'], row['id'])
        albums.append(album)
    return albums