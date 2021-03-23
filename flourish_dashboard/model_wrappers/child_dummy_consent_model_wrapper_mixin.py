from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow


class ChildDummyConsentModelWrapperMixin:

    @property
    def screening_identifier(self):
        subject_consent = self.subject_consent_cls.objects.get(
            subject_identifier=self.subject_identifier)
        return subject_consent.screening_identifier

    @property
    def assent_options(self):
        """Returns a dictionary of options to get an existing
         child assent model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier,
            version=self.version)
        return options

    @property
    def consent_options(self):
        """Returns a dictionary of options to get an existing
        consent model instance.
        """
        options = dict(
            subject_identifier=self.subject_identifier,
            version=self.consent_version)
        return options

    @property
    def subject_identifier(self):
        subject_identifier = self.object.subject_identifier.split('-')
        subject_identifier.pop()
        caregiver_subject_identifier = '-'.join(subject_identifier)
        return caregiver_subject_identifier

    @property
    def child_name_initial(self):
        if getattr(self, 'assent_model_obj'):
            name = self.assent_model_obj.first_name
            initials = self.assent_model_obj.initials
            return f'{name} {initials}'
        elif getattr(self, 'consent_model_obj'):
            caregiverchildconsent_objs = self.consent_model_obj.caregiverchildconsent_set.all()
            for caregiverchildconsent_obj in caregiverchildconsent_objs:
                first_name = caregiverchildconsent_obj.first_name
                last_name = caregiverchildconsent_obj.first_name
                return f'{first_name} {first_name[0]}{last_name[0]}'
        return None

    @property
    def child_age(self):
        if getattr(self, 'assent_model_obj'):
            birth_date = self.assent_model_obj.dob
            difference = relativedelta(get_utcnow().date(), birth_date)
            months = 0
            if difference.years > 0:
                months = difference.years * 12
            years = round((months + difference.months) / 12, 2)
            return years
        elif getattr(self, 'consent_model_obj'):
            caregiverchildconsent_objs = self.consent_model_obj.caregiverchildconsent_set.all()
            for caregiverchildconsent_obj in caregiverchildconsent_objs:
                birth_date = caregiverchildconsent_obj.child_dob
                difference = relativedelta(get_utcnow().date(), birth_date)
                months = 0
                if difference.years > 0:
                    months = difference.years * 12
                years = round((months + difference.months) / 12, 2)
                return years
        return 0

    @property
    def assent_date(self):
        if getattr(self, 'assent_model_obj'):
            return self.assent_model_obj.consent_datetime.date()
        elif getattr(self, 'consent_model_obj'):
            caregiverchildconsent_objs = self.consent_model_obj.caregiverchildconsent_set.all()
            for caregiverchildconsent_obj in caregiverchildconsent_objs:
                consent_date = caregiverchildconsent_obj.consent_datetime.date()
                return consent_date
        return 'N/A'