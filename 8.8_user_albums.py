# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist,album_title,songs_num=None):
    album = {
        'artist' : artist,
        'album_title' : album_title,
    }
    if songs_num:
        album['number of songs'] = songs_num
    
    return album

#list to store user albums dictionary created by user inputs
stored_albums = [ ]

no_quit = False
while not no_quit:
    artist_name = input("Enter name of artist: ")
    if artist_name == 'quit':
        no_quit = True
    else:
        album_title = input("Enter name of album: ")
        if(album_title == 'quit'):
            no_quit = True
        else:
            #store user inputs into dictionary:
            stored_albums.append(make_album(artist_name, album_title))
            
#print all albums in stored_albums
for album in stored_albums:
    print(album)
    