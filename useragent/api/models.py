import uuid

from django.db import models

from accounts.models import User


class Agent(models.Model):
    agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    prompt_template = models.TextField(null=False)
    prompt_template2 = models.TextField(null=False)
    prompt_template3 = models.TextField(null=False)
    prompt_template4 = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AgentRun(models.Model):
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Run {self.run_id} by User {self.user_id}"


class AgentMetadata(models.Model):
    metadata_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, null=False)
    value = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Metadata {self.metadata_id} for Agent {self.agent_id}"
