import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from happyforms import forms

from remo.profiles.models import UserProfile

class InviteUserForm(forms.Form):
    email = forms.EmailField(label='Email')


class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def _clean_names(self, data):
        """ Ensure that data is valid

        Variabel data can contain only latin letters (both capital and
        lower case), spaces and the character '.
        """
        if not re.match(r'(^[A-Za-z\' ]+$)', data):
            raise ValidationError("Please use only latin characters.")

        return data

    def clean_first_name(self):
        """ Ensure that first_name is valid. """

        data = self.cleaned_data['first_name']
        return self._clean_names(data)

    def clean_last_name(self):
        """ Ensure that last_name is valid."""

        data = self.cleaned_data['last_name']
        return self._clean_names(data)


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('local_name', 'birth_date',
                  'city', 'region', 'country',
                  'lon', 'lat', 'display_name',
                  'private_email', 'mozillians_profile_url',
                  'twitter_account', 'jabber_id', 'irc_name',
                  'irc_channels', 'facebook_url', 'diaspora_url',
                  'personal_website_url', 'personal_blog_feed',
                  'bio', 'gender', 'mentor')


    def clean_twitter_account(self):
        """ Make sure that twitter_account does not start with a '@' """
        twitter_account = self.cleaned_data['twitter_account']
        return twitter_account.strip('@')
