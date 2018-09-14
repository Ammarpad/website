from .views import OrganizersContactFormView, OrganizersTemplateView, MentorsContactFormView, MentorsTemplateView, ApplicantHelpContactFormView, ApplicantHelpTemplateView, ContactTemplateView
from django.conf.urls import url

urlpatterns = [
    url(r'^organizers/$', OrganizersContactFormView.as_view(), name='contact-organizers'),
    url(r'^organizers/sent/$', OrganizersTemplateView.as_view(), name='contacted-organizers'),
    url(r'^mentors/$', MentorsContactFormView.as_view(), name='contact-mentors'),
    url(r'^mentors/sent/$', MentorsTemplateView.as_view(), name='contacted-mentors'),
    url(r'^applicant-help/$', ApplicantHelpContactFormView.as_view(), name='contact-applicant-help'),
    url(r'^applicant-help/sent/$', ApplicantHelpTemplateView.as_view(), name='contacted-applicant-help'),
    url(r'^contact-us/$', ContactTemplateView.as_view(), name='contact-us'),
]
