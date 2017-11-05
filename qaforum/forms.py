from django import forms
from django.conf import settings
from qaforum.models import QaQuestion


class QaQuestionForm(forms.ModelForm):
    class Meta:
        model = QaQuestion
        fields = ['title', 'description', 'tags']

    def __init__(self, *args, **kwargs):
        super(QaQuestionForm, self).__init__(*args, **kwargs)

        try:
            settings.QAFORUM_SETTINGS['qaforum_description_optional']
            self.fields['description'].required = not settings.QAFORUM_SETTINGS[
                'qaforum_description_optional']

        except KeyError:
            pass
