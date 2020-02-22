from rest_framework import serializers
from .models import MurrCard, EditorImageForMurrCard, EditorDataForMurrCard


class MurrCardSerializers(serializers.ModelSerializer):

    class Meta:
        model = MurrCard
        fields = ('title', 'description', 'owner', 'cover', 'content')


# # class EditorImageForMurrCardSerializers(serializers.ModelSerializer):
# class EditorImageForMurrCardSerializers(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = EditorImageForMurrCard
#         fields = ('id', 'editor_image')


class EditorImageForMurrCardSerializers(serializers.ModelSerializer):

    class Meta:

        model = EditorImageForMurrCard
        fields = ('murr_editor_image',)


class EditorDataForMurrSerializers(serializers.ModelSerializer):

    class Meta:

        model = EditorDataForMurrCard
        fields = ('data_for_murr',)
