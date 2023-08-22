from django import forms
from .models import WorkGroup, Review, Analysis, Sample

class WorkGroupForm(forms.ModelForm):
    class Meta:
        model = WorkGroup
        fields = ['work_group_id']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['written_by', 'reviewed_by', 'approved_by', 'date_implemented']

class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ['analysis_type', 'date', 'work_group', 'prep', 'dilution', 'analysis']

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['sample_id', 'weight', 'solvent', 'solvent_volume', 'spike_volume', 'notes', 'analysis_dilution']
