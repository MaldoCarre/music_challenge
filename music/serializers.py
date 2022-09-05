from rest_framework import serializers


class Band_or_artist_name(serializers.Serializer):
    name = serializers.CharField(help_text="Name of the band or artist")


class Band_or_artist_response_data(serializers.Serializer):
    """
    Response data structure example:
    Response: {
        artist: "" \\ str
        style: "" \\ str
        mood: "" \\ str
        country: "" \\ str
        discography: [
            {
                album: "",
                year: ""
            },
            {
                album: "",
                year: ""
            }, ...
        ]
    }
    """
    artist = serializers.CharField(help_text="Name of the band or artist")
    style = serializers.CharField(help_text="Music style")
    mood = serializers.CharField(help_text="Music mood")
    country = serializers.CharField(help_text="Band or artist country")
    discography = serializers.ListField(help_text="Discography info")