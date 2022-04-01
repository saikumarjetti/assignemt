Identify latest released movies let's say top 25 from the imdb and store it in DB as latest shows (use python imdb package)
Create list API to fetch latest shows
Provide the booking api for the the shows

Create a API which can show latest booking for the users

1.API to get latest booking of the user

METHOD : POST
http://0.0.0.0:3030/get_latest_booking

input:
{
    "user":"sai kumar",
    "show":"The Godfather"
}

result :

{
  "data": [
    {
      "_id": {
        "$oid": "6246dcb7f6a8e10e4331556d"
      },
      "show": "The Godfather",
      "status": "success",
      "user": "sai kumar"
    },
    {
      "_id": {
        "$oid": "6246dcda20d94bbeee430c3d"
      },
      "show": "The Godfather",
      "status": "success",
      "user": "sai kumar"
    }
  ]
}


2.API to get latest shows
METHOD : GET
http://0.0.0.0:3030/list


result:

{
  "latest shows": [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "The Godfather: Part II",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Good, the Bad and the Ugly",
    "Forrest Gump",
    "Fight Club",
    "Inception",
    "The Lord of the Rings: The Two Towers",
    "Star Wars: Episode V - The Empire Strikes Back",
    "The Matrix",
    "Goodfellas",
    "One Flew Over the Cuckoo's Nest",
    "Se7en",
    "Seven Samurai",
    "It's a Wonderful Life",
    "The Silence of the Lambs",
    "Saving Private Ryan",
    "City of God",
    "Life Is Beautiful"
  ]
}

3.API for booking shows

METHOD : POST
http://0.0.0.0:3030/booking

input:

{
    "user":"sai kumar",
    "show":"The Godfather"
}

result:
{
  "message": "Booking"
}