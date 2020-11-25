from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'Name',
            'Username',
            'Email',
            'Department',
            'Project',
            'Manager',
            'Justification',
            'StartDate',
            'AccessDuration',
            'S3Bucket',
            'Permission'
        ]
