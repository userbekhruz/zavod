from rest_framework import serializers

from .models import *
from User.serializers import *


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo')


class Ish_TuriSer(serializers.ModelSerializer):
    class Meta:
        model = Ish_Turi
        fields = ('id', 'name', 'ish_id')


class BulimSer(serializers.ModelSerializer):
    class Meta:
        model = Bulim
        fields = ('id', 'name', 'bulim_id', 'user')


class MahsulotSer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ('id', 'name','mahsulot_id')


class XatolarSer(serializers.ModelSerializer):
    class Meta:
        model = Xatolar
        fields = ('id', 'name', 'xato_id')


class MissedSer(serializers.ModelSerializer):
    class Meta:
        model = Missed
        fields = ('id', 'xodim', 'user', 'xato', 'xato_soni', 'butun_soni', 'mahsulot', 'created_at', 'updated_at', 'photo', 'izoh', 'ish_vaqti', 'audio')
    
    def update(self, instance, validated_data):
        instance.xodim = validated_data.get('xodim', instance.xodim)
        instance.user = validated_data.get('user', instance.user)
        instance.xato = validated_data.get('xato', instance.xato)
        instance.xato_soni = validated_data.get('xato_soni', instance.xato_soni)
        instance.butun_soni = validated_data.get('butun_soni', instance.butun_soni)
        instance.mahsulot = validated_data.get('mahsulot', instance.mahsulot)
        # instance.photo = validated_data.pop('photo', instance.photo)
        instance.izoh = validated_data.get('izoh', instance.izoh)
        instance.ish_vaqti = validated_data.get('ish_vaqti', instance.ish_vaqti)
        instance.audio = validated_data.get('audio', instance.audio)
        instance.save()
        return instance


class MissedGetSer(serializers.ModelSerializer):
    xodim = XodimSer()
    user = UserSer()
    xato = XatolarSer()
    mahsulot = MahsulotSer()
    photo = PhotoSer(many=True)
    class Meta:
        model = Missed
        fields = ('id', 'xodim', 'user', 'xato', 'xato_soni', 'butun_soni', 'mahsulot', 'created_at', 'updated_at', 'photo', 'izoh', 'ish_vaqti', 'audio')
