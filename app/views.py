from flask import jsonify, request
from app.models import Movie

def index():
    return '<h1>Api de Peliculas</h1>'

def get_all_movies():
    movies = Movie.get_all()
    list_movies = [movie.serialize() for movie in movies]
    return jsonify(list_movies)

def create_movie():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_movie = Movie(
        id_user=data['id_user'],
        title=data['title'],
        gender=data['gender'],
        director=data['director'],
        actors=data['actors'],
        rating=data['rating'],
        release_date=data['release_date'],
        banner=data['banner']
    )
    
    new_movie.save()
    return jsonify({'message':'Pelicula creada con exito'}), 201
    
def update_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    movie.id_user = data['id_user']
    movie.title = data['title']
    movie.gender = data['gender']
    movie.director = data['director']
    movie.actors = data['actors']
    movie.rating = data['rating']
    movie.release_date = data['release_date']
    movie.banner = data['banner']
    movie.save()
    return jsonify({'message': 'Movie updated successfully'})

def get_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    return jsonify(movie.serialize())

def delete_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    movie.delete()
    return jsonify({'message': 'Movie deleted successfully'})