from app.database import get_db

class Movie:

    #constuctor
    def __init__(self,id_movie=None,id_user=None,title=None,gender=None,director=None,actors=None,rating=None,release_date=None,banner=None):
        self.id_movie=id_movie
        self.id_user=id_user
        self.title=title
        self.gender=gender
        self.director=director
        self.actors=actors
        self.rating=rating
        self.release_date=release_date
        self.banner=banner

    def serialize(self):
        return {
            'id_movie': self.id_movie,
            'id_user': self.id_user,
            'title': self.title,
            'gender': self.gender,
            'director': self.director,
            'actors': self.actors,
            'rating': self.rating,            
            'release_date': self.release_date,
            'banner': self.banner
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM movies"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        movies = [Movie(id_movie=row[0], id_user=row[1], title=row[2], release_date=row[3], gender=row[4], director=row[5], actors=row[6], rating=row[7], banner=row[8]) for row in rows]

        cursor.close()
        return movies

    @staticmethod
    def get_by_id(movie_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies WHERE id_movie = %s", (movie_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Movie(id_movie=row[0], id_user=row[1], title=row[2], release_date=row[3], gender=row[4], director=row[5], actors=row[6], rating=row[7], banner=row[8])
        return None
    
    """
    Insertar un registro si no existe el atributo id_movie
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_movie:
            cursor.execute("""
                UPDATE movies SET id_user = %s, title = %s, gender = %s, director = %s, actors = %s, rating = %s, release_date = %s, banner = %s
                WHERE id_movie = %s
            """, (self.id_user, self.title, self.gender, self.director, self.actors, self.rating, self.release_date, self.banner, self.id_movie))
        else:
            cursor.execute("""
                INSERT INTO movies (id_user, title, gender, director, actors, rating, release_date, banner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.id_user, self.title, self.gender, self.director, self.actors, self.rating, self.release_date, self.banner))
            self.id_movie = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM movies WHERE id_movie = %s", (self.id_movie,))
        db.commit()
        cursor.close()
