from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_model_wrapper import ModelWrapper

from .caregiver_child_consent_model_wrapper_mixin import \
    CaregiverChildConsentModelWrapperMixin
from .child_assent_model_wrapper_mixin import ChildAssentModelWrapperMixin
from .child_birth_model_wrapper_mixin import ChildBirthModelWrapperMixin
from .child_continued_consent_model_wrapper_mixin import \
    ChildContinuedConsentModelWrapperMixin
from .child_death_report_model_wrapper_mixin import ChildDeathReportModelWrapperMixin
from .child_offstudy_model_wrapper_mixin import ChildOffstudyModelWrapperMixin
from .consent_model_wrapper_mixin import ConsentModelWrapperMixin
from .maternal_delivery_wrapper_mixin import MaternalDeliveryModelWrapperMixin


class CaregiverChildConsentModelWrapper(CaregiverChildConsentModelWrapperMixin,
                                        ConsentModelWrapperMixin,
                                        ChildAssentModelWrapperMixin,
                                        ChildContinuedConsentModelWrapperMixin,
                                        ChildBirthModelWrapperMixin,
                                        MaternalDeliveryModelWrapperMixin,
                                        ChildDeathReportModelWrapperMixin,
                                        ChildOffstudyModelWrapperMixin,
                                        ModelWrapper):
    model = 'flourish_caregiver.caregiverchildconsent'
    querystring_attrs = ['subject_consent', 'subject_identifier']
    next_url_attrs = ['subject_consent', 'subject_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'subject_listboard_url')

    @property
    def consent_options(self):
        """Returns a dictionary of options to get an existing
        consent model instance.
        """
        options = dict(
            screening_identifier=self.screening_identifier,
            version=self.consent_version)
        return options

    @property
    def screening_identifier(self):
        return self.object.subject_consent.screening_identifier

    @property
    def maternal_delivery_model_obj(self):
        """Returns a maternal delivery model instance or None.
        """
        try:
            return self.maternal_delivery_cls.objects.get(
                subject_identifier=self.object.subject_consent.subject_identifier)
        except ObjectDoesNotExist:
            return None
