from django.urls import path

from api.views import AgentView

urlpatterns = [
    path('agents/', AgentView.as_view(), name='agents'),
    path('agents/', AgentView.as_view(), name='agent-list'),
    path('agents/<uuid:agent_id>/', AgentView.as_view(), name='agent-detail'),

]
