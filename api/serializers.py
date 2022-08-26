from rest_framework import serializers
from api.models import Entry
from datetime import date

class EntrySerializer(serializers.ModelSerializer):

    WEEKDAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    owner = serializers.ReadOnlyField(source='owner.username')  # type: ignore

    puzzle_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d')) # type: ignore
    solve_date = serializers.DateField(initial=date.today().strftime('%Y-%m-%d')) # type: ignore

    used_help = serializers.BooleanField(initial=True) # type: ignore
    streak = serializers.BooleanField(initial=True) # type: ignore

    day = serializers.ChoiceField(choices=WEEKDAYS) #type: ignore
    class Meta:
        model = Entry
        fields = ['id', 'puzzle_date', 'solve_date', 'elapsed_seconds', 'used_help', 'streak', 'day','owner']