import json

def load_movies():
    return {
        "Inception": {
            "reviews": [
                {"user": "Alice", "rating": 5, "comment": "Amazing!"},
                {"user": "Bob", "rating": 4, "comment": "Great plot, but a bit confusing."}
            ]
        },
        "The Matrix": {
            "reviews": [
                {"user": "Charlie", "rating": 5, "comment": "A classic!"},
                {"user": "Dana", "rating": 5, "comment": "Loved it!"}
            ]
        }
    }

def save_database_to_file(database, filename="movies.json"):
    with open(filename, "w") as file:
        json.dump(database, file, indent=4)

def load_database_from_file(filename="movies.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return load_movies()

def calculate_average_rating(reviews):
    if not reviews:
        return 0
    return round(sum(review["rating"] for review in reviews) / len(reviews), 2)

def display_movies(database):
    for movie, data in database.items():
        avg_rating = calculate_average_rating(data["reviews"])
        print(f"{movie} (Average Rating: {avg_rating})")
        for review in data["reviews"]:
            print(f"  - {review['user']}: {review['rating']} stars - {review['comment']}")

def add_movie(database):
    movie = input("Enter the name of the movie: ")
    if movie in database:
        print("Movie already exists.")
        return

    database[movie] = {"reviews": []}
    print("Movie added successfully!")

def add_review(database):
    movie = input("Enter the name of the movie: ")
    if movie not in database:
        print("Movie not found.")
        return

    user = input("Enter your name: ")
    rating = int(input("Enter your rating (1-5): "))
    comment = input("Enter your comment: ")

    database[movie]["reviews"].append({"user": user, "rating": rating, "comment": comment})
    print("Review added successfully!")

def delete_review(database):
    movie = input("Enter the name of the movie: ")
    if movie not in database:
        print("Movie not found.")
        return

    user = input("Enter the name of the reviewer: ")
    reviews = database[movie]["reviews"]

    for i, review in enumerate(reviews):
        if review["user"] == user:
            del reviews[i]
            print("Review deleted successfully!")
            return

    print("Review not found.")

def modify_review(database):
    movie = input("Enter the name of the movie: ")
    if movie not in database:
        print("Movie not found.")
        return

    user = input("Enter the name of the reviewer: ")
    reviews = database[movie]["reviews"]

    for review in reviews:
        if review["user"] == user:
            print(f"Current Rating: {review['rating']}, Current Comment: {review['comment']}")
            new_rating = int(input("Enter new rating (1-5): "))
            new_comment = input("Enter new comment: ")
            review["rating"] = new_rating
            review["comment"] = new_comment
            print("Review updated successfully!")
            return

    print("Review not found.")

def main():
    database = load_database_from_file()

    while True:
        print("\nMovie Review System")
        print("1. View all movies")
        print("2. Add a movie")
        print("3. Add a review")
        print("4. Delete a review")
        print("5. Modify a review")
        print("6. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(database)
        elif choice == "2":
            add_movie(database)
        elif choice == "3":
            add_review(database)
        elif choice == "4":
            delete_review(database)
        elif choice == "5":
            modify_review(database)
        elif choice == "6":
            save_database_to_file(database)
            print("Database saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
