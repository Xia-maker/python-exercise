import sqlite3

# Read the content of the file into a list
stephen_king_adaptations_list = []
with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

# Establish a connection with the SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create the table in the database
cursor.execute("CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (movieID INTEGER PRIMARY KEY AUTOINCREMENT, movieName TEXT, movieYear INTEGER, imdbRating REAL)")

# Insert the content into the table
for line in stephen_king_adaptations_list:
    movie_data = line.split(",")
    try:
        movie_year = int(movie_data[2])
        imdb_rating = float(movie_data[3])
        cursor.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
                       (movie_data[1], movie_year, imdb_rating))
    except ValueError:
        print("Invalid data for line:", line)
        continue

# Save the changes
conn.commit()

def search_by_movie_name(movie_name):
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
    result = cursor.fetchone()
    if result:
        print("Movie Details:")
        print("Movie Name:", result[1])
        print("Movie Year:", result[2])
        print("IMDB Rating:", result[3])
    else:
        print("No such movie exists in our database.")


def search_by_movie_year(movie_year):
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
    results = cursor.fetchall()
    if results:
        print("Movie Details:")
        for result in results:
            print("Movie Name:", result[1])
            print("Movie Year:", result[2])
            print("IMDB Rating:", result[3])
    else:
        print("No movies were found for that year in our database.")


def search_by_movie_rating(min_rating):
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (min_rating,))
    results = cursor.fetchall()
    if results:
        print("Movie Details:")
        for result in results:
            print("Movie Name:", result[1])
            print("Movie Year:", result[2])
            print("IMDB Rating:", result[3])
    else:
        print("No movies at or above that rating were found in the database.")


# Search movies in the database based on user input
while True:
    print("Please select the search option:")
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")
    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        movie_name = input("Enter the name of the movie: ")
        search_by_movie_name(movie_name)

    elif user_choice == "2":
        movie_year = int(input("Enter the year of the movie: "))
        search_by_movie_year(movie_year)

    elif user_choice == "3":
        movie_rating = float(input("Enter the minimum rating: "))
        search_by_movie_rating(movie_rating)

    elif user_choice == "4":
        break

    else:
        print("Invalid option. Please try again.")

# Close the database connection
conn.close()