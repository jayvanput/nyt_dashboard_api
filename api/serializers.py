from rest_framework import serializers
from api.models import Entry
from datetime import date

class EntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # type: ignore

    puzzle_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d')) # type: ignore
    solve_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d')) # type: ignore

    checked = serializers.BooleanField(initial=True) # type: ignore
    revealed = serializers.BooleanField(initial=True) # type: ignore
    streak = serializers.BooleanField(initial=True) # type: ignore

    class Meta:
        model = Entry
        fields = ['id', 'puzzle_date', 'solve_date', 'elapsed_seconds', 'checked', 'revealed', 'streak', 'owner']