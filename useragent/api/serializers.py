from rest_framework import serializers

from api.models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['agent_id', 'name', 'description', 'prompt_template', 'prompt_template2', 'prompt_template3',
                  'prompt_template4']
