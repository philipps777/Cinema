from admin import Admin


user = User("username", "userpassword", "admin")
user1 = User("username", "userpassword", "user")

admin = Admin(user)

cinema = Cinema("Multiplex","adress road 1")
admin.create_movie("The Guilty", "Антуан Фукуа", 2021, "Джейк Джилленхол", ["Джейк Джилленхол", "Райли Кио"], "триллер-фильм", cinema)


movie = Movie("Tom and Jerry", "Darrell Van Citters", 2021, "Ashley Postelwaite", ["Tom", "Jerry"], "Comedy", cinema)
admin.update_movie("The Guilty", movie)


admin.delete_movie(movie)
cinema = Cinema("Cinema Name", "Cinema Address")
admin.update_cinema(cinema)
admin.delete_cinema()

# admin.create_cinema("Cinema Name", "Cinema Address", "Cinema Schedule")















# purchase = MoviePurchase("username", "Movie Title", "Purchase Date")
# purchase.purchase_movie()