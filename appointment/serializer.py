import datetime

from rest_framework import serializers

from appointment.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    custom = serializers.StringRelatedField(read_only=True)
    classroom = serializers.StringRelatedField(read_only=True)

    def validate(self, data):
        data["start"] = int(data["start"])
        data["end"] = int(data["end"])
        if data["start"] > data["end"]:
            raise serializers.ValidationError("end must occur after start")
        today = datetime.date.today()
        if data["date"].__lt__(today):
            raise serializers.ValidationError("you can not choose date before today")
        appointments = Appointment.objects.filter(classroom__name=self.initial_data['classroom'],
                                                  date__exact=data['date'])
        for appoint in appointments:
            if appoint.start < data['start'] < appoint.end:
                raise serializers.ValidationError("start time unvalid!")
            if appoint.start < data['end'] < appoint.end:
                raise serializers.ValidationError("end time unvalid!")
        return data

    class Meta:
        model = Appointment
        fields = ('date', 'start', 'end', 'reason', 'desk', 'multimedia', 'custom', 'classroom')
