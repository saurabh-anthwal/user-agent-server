from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Agent
from api.serializers import AgentSerializer


class AgentView(ListCreateAPIView, RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    lookup_field = 'agent_id'

    def get(self, request, *args, **kwargs):
        agent_id = self.kwargs.get('agent_id', None)
        if agent_id:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
