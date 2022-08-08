from rest_framework import serializers
from api.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'puzzle_date', 'solve_date', 'elapsed_seconds', 'checked', 'revealed', 'streak', 'owner']