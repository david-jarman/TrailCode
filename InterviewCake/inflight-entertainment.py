# 100
# [50, 30, 20, 10, 70]
# 

def can_user_watch_two_movies(flight_length, movie_lengths):
    movie_lengths_map = {}
    for movie in movie_lengths:
        if movie in movie_lengths_map:
            movie_lengths_map[movie] += 1
        else:
            movie_lengths_map[movie] = 1

    # determine if there are two movies to watch
    for movie in movie_lengths:
        proposed_other_movie = flight_length - movie
        if proposed_other_movie > 0:
            if proposed_other_movie == movie:
                #see if there exists another movie with the same length
                num_movies = movie_lengths_map[movie]
                if num_movies > 1:
                    return True
            else:
                if proposed_other_movie in movie_lengths_map:
                    return True
        else:
            continue

    return False

def can_user_watch_two_movies_one_pass(flight_length, movie_lengths):
    movie_lengths_visited = {}

    for movie in movie_lengths:
        second_movie = flight_length - movie
        if second_movie > 0 and second_movie in movie_lengths_visited:
            return True
        
        movie_lengths_visited[movie] = True

    return False

flight_length = 100
movies = [50, 30]

print can_user_watch_two_movies_one_pass(100, [50, 30])
print can_user_watch_two_movies_one_pass(100, [50, 30, 70])
print can_user_watch_two_movies_one_pass(100, [50, 30, 50])
print can_user_watch_two_movies_one_pass(20, [50, 30])
print can_user_watch_two_movies_one_pass(100, [])
print can_user_watch_two_movies_one_pass(100, [100])


