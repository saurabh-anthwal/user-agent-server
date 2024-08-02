from rest_framework import serializers

from api.models import Agent, AgentMetadata


class AgentMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentMetadata
        fields = ['key', 'value']


class AgentSerializer(serializers.ModelSerializer):
    formData = AgentMetaDataSerializer(many=True)

    class Meta:
        model = Agent
        fields = ['agent_id', 'name', 'description', "imageUrl", "redirectUrl", 'formData']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        formData = {}
        for item in representation['formData']:
            formData[item['key']] = item['value']

        custom_representation = {
            "id": representation['agent_id'],
            "name": representation['name'],
            "description": representation['description'],
            "imageUrl": representation['imageUrl'],
            "url": representation['redirectUrl'],
            "formData": [formData] if formData else None
        }

        return custom_representation
