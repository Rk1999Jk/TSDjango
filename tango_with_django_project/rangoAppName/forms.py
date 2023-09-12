from django import forms

class FeedbackForm(forms.Form):
    CHOICES = [
        (5.0, 'Strongly Agree'),
        (4.0, 'Agree'),
        (2.5, 'Neutral'),
        (2, 'Disagree'),
        (1,'Strongly Disagree')
    ]
    s1m1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
class MyForm(forms.Form):
    CHOICES = [
        ('5', 'Strongly Agree'),
        ('4', 'Agree'),
        ('2.5', 'Neutral'),
        ('2', 'Disagree'),
        ('1', 'Strongly Disagree'),
    ]
    OPPOSITE_CHOICES = [
        ('1', 'Strongly Agree'),
        ('2', 'Agree'),
        ('2.5', 'Neutral'),
        ('4', 'Disagree'),
        ('5', 'Strongly Disagree'),
    ]

    S1M1 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S1M2 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S1M3 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S2M1 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S2M2 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S2M3 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S3M1 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S3M2 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S3M3 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    S4M1 = forms.ChoiceField(
        choices=OPPOSITE_CHOICES,
        widget=forms.RadioSelect
    )
    S4M2 = forms.ChoiceField(
        choices=OPPOSITE_CHOICES,
        widget=forms.RadioSelect
    )
    S4M3 = forms.ChoiceField(
        choices=OPPOSITE_CHOICES,
        widget=forms.RadioSelect
    )
    RANK_CHOICES = [
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        
    ]
    M1Rank = forms.ChoiceField(
        choices=RANK_CHOICES,
        widget=forms.RadioSelect
    )
    M2Rank = forms.ChoiceField(
        choices=RANK_CHOICES,
        widget=forms.RadioSelect
    )
    M3Rank = forms.ChoiceField(
        choices=RANK_CHOICES,
        widget=forms.RadioSelect
    )

    
    