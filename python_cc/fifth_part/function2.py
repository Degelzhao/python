def city_country(city, country):
    link = city + ',' + country
    return link

while True:
    print('please input city and country name:')
    print("(enter 'q' at any time to quit)")

    city = input('city name:')
    if city == 'q':
        break

    country = input('country name:')
    if country == 'q':
        break

    format_name = city_country(city, country)
    print(format_name)


def make_album(singer_name, album_name, song_name = ''):
    music_inf = {'singer_name':singer_name, 'album_name':album_name}

    if song_name:
        music_inf['song_name'] = song_name

    return music_inf

while True:
    print('please input singer and album name:')
    print("(enter 'q' at any time to quit)")
    singer_name = input('singer name:')
    if singer_name == 'q':
        break
    album_name = input('album name:')
    if album_name == 'q':
        break

    validation = input("Do you know this song name? please input 'Y' or 'N' ")
    if validation == 'Y':
        song_name = input('song name:')
        if song_name == 'q':
            break
        music_inf = make_album(singer_name, album_name, song_name)
        print(music_inf)

    if validation == 'N':
        music_inf = make_album(singer_name, album_name)
        print(music_inf)



