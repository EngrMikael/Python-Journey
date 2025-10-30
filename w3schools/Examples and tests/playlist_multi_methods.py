class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
    def show_songs(self):
        print(f"Playlsit '{self.name}' : ")
        for song in self.songs:
            print(f"- {song}")
# this is the one from the site 

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()

# now i want the user to add songs

my_playlist = input("Enter Playlist name: ")
my_playlist_name = Playlist(my_playlist)
choice = 'y'
while choice == 'y':
    choice = input("Do you want to add a song? (y/n): ").strip().lower()
    if choice == 'y':
        input_song = input("Enter a song name: ")
        my_playlist_name.add_song(input_song)
    elif choice == 'n':
        my_playlist_name.show_songs()
        break
    else:
        print("Invalid input")