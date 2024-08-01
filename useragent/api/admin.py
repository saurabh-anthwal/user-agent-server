from django.contrib import admin

from api.models import AgentRun, Agent, AgentMetadata

admin.site.register(AgentMetadata)
admin.site.register(Agent)
admin.site.register(AgentRun)
