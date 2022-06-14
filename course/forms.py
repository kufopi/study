from django.forms import ModelForm
from .models import ConasReg,CourseReg

class ConasRegForm(ModelForm):
    """Form definition for ConasReg."""

    class Meta:
        """Meta definition for ConasRegform."""

        model = ConasReg
        fields = '__all__'
        exclude = ['created']


class CourseRegForm(ModelForm):
    """Form definition for CourseReg."""

    class Meta:
        """Meta definition for CourseRegform."""

        model = CourseReg
        fields = '__all__'
        exclude = ['created']


