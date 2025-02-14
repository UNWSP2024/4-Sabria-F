#By: Sabria Fafach
#Date: Febuary, 2 2025
#Title: program_2.py


movie_inp=input("Do you want to get tickets for a movie(s)? (Enter y for yes):")
tot_tix=0
while movie_inp=="y":
    movie=input("Enter the name of a movie you want to get tickets for:")
    tot_tix=int(input(f"Enter the number of tickets you want for {movie}:"))+tot_tix
    movie_inp=input("Do you want to get tickets for anoter movie? (Enter y for yes):")
print(f"The total of all your movie tickets is {tot_tix} tickets.")