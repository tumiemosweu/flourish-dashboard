"""flourish_dashboard URL Configuration
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from edc_dashboard import UrlConfig

from .patterns import subject_identifier
from .views import (
    MaternalScreeningListBoardView, MaternalSubjectListboardView,
    MaternalLocatorListBoardView)

app_name = 'flourish_dashboard'

maternal_screening_listboard_url_config = UrlConfig(
    url_name='maternal_screening_listboard_url',
    view_class=MaternalScreeningListBoardView,
    label='maternal_screening_listboard',
    identifier_label='identifier',
    identifier_pattern=subject_identifier)

maternal_locator_listboard_url_config = UrlConfig(
    url_name='maternal_locator_listboard_url',
    view_class=MaternalLocatorListBoardView,
    label='maternal_locator_listboard',
    identifier_label='identifier',
    identifier_pattern=subject_identifier)

subject_listboard_url_config = UrlConfig(
    url_name='subject_listboard_url',
    view_class=MaternalSubjectListboardView,
    label='maternal_subject_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)

urlpatterns = [
]

urlpatterns += subject_listboard_url_config.listboard_urls
urlpatterns += maternal_locator_listboard_url_config.listboard_urls
urlpatterns += maternal_screening_listboard_url_config.listboard_urls