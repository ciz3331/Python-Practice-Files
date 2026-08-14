# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(artist,album_title,songs_num=None):
    album = {
        'artist' : artist,
        'album_title' : album_title,
    }
    if songs_num:
        album['number of songs'] = songs_num
    
    return album

#without songs_num value
taylor_album = make_album('Taylor Swift', '1989')
beatles_album = make_album('The beatles', 'Abbey Road')
adele_album = make_album('Adele', '21')

#with songs_num value
kendrick_album = make_album('Kendrick Lamar', 'Good Kid, M.A.A.D City', 12)

# print(taylor_album)
# print(beatles_album)
# print(adele_album)
# print(kendrick_album)
albums = [taylor_album,beatles_album,adele_album,kendrick_album]
#optional: function to print albums in a nice format
def nice_format_print(album_list):
    for album in album_list:
        for k, v in album.items():
            k = k.replace("_", " ") #convert underscores to space
            v = str(v) #convert all values to string
            if k == 'artist':
                print(f"{k.title()}: {v.title()}")
            else:
                print(f"\t*{k.title()}: {v.title()}")

nice_format_print(albums)