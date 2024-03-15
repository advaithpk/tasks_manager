from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField()
    desc = serializers.CharField()
    date = serializers.DateField()
    remind = serializers.BooleanField()
    priority = serializers.ChoiceField(choices=['Low', 'Medium', 'High'])
    status = serializers.ChoiceField(choices=['Pending', 'Completed'])
