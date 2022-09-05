import requests

from .exception import Custom_exception

from globant.commons import artist_info_url, album_info_url


def artis_info(name:str) -> dict:
    """
    Get the first part of the artist info.
    """
    data={}

    try:
        general_info  = requests.get(artist_info_url+name)
        general_info = general_info.json()

        for info in general_info["artists"]: 
            id = info["idArtist"]
            style = info["strStyle"]
            mood = info["strMood"]
            country = info["strCountry"]
            data = {
                "id": id,
                "artist":name, 
                "style": style,
                "mood": mood,
                "country": country
            }
    except TypeError:
        raise Custom_exception
    return data


def artist_album_info(id:str) -> list:
    """
    Get the album info from the artist id.
    """
    album_list = []
    album_info_detail = requests.get(album_info_url+id)
    album_info_detail = album_info_detail.json()

    for album_info in album_info_detail["album"]:
        album_list.append({"albug":album_info["strAlbum"], "year": album_info["intYearReleased"]})

    return album_list


def get_info(name:str)-> dict:
    """
    Create the response info dict.
    """

    data_artist_info = artis_info(name=name)
    data_album_info = artist_album_info(id=data_artist_info["id"])
    data_artist_info.update({"discography":data_album_info})

    return data_artist_info