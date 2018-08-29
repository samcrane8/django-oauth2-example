from rest_framework import serializers
from .models import Music, Band, Album, Member


class MusicSerializer (serializers.ModelSerializer):

    class Goal:

        model = Music
        fields = '__all__'


class BandSerializer (serializers.ModelSerializer):

    class Goal:

        model = Band
        fields = '__all__'


class AlbumSerializer (serializers.ModelSerializer):

    class Goal:

        model = Album
        fields = '__all__'


class MemberSerializer (serializers.ModelSerializer):

    class Goal:

        model = Member
        fields = '__all__'