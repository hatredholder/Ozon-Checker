import pytest

from links.models import Link


@pytest.mark.django_db
def test_link_str_method():
    link_object = Link.objects.create(name="Testname", url="www.testurl.com")
    assert link_object.__str__() == "Testname"