from rest_framework import serializers
from api.models import Entry
from datetime import date

class EntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    puzzle_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d'))
    solve_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d'))

    checked = serializers.BooleanField(initial=True)
    revealed = serializers.BooleanField(initial=True)
    streak = serializers.BooleanField(initial=True)

    class Meta:
        model = Entry
        fields = ['id', 'puzzle_date', 'solve_date', 'elapsed_seconds', 'checked', 'revealed', 'streak', 'owner']