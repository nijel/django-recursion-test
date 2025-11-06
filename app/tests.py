from django.test import TestCase
from .models import Unit, Project
from django.db.models import Prefetch


class DebugTestCase(TestCase):
    def test_unit(self):
        project = Project.objects.create(name="Test", slug="test")
        Unit.objects.create(project=project, slug="unit")

        units = Unit.objects.prefetch_related(
            Prefetch("project", queryset=Project.objects.only("descriptions", "notes"))
        )
        self.assertEqual(units[0].get_absolute_url(), "test/unit")
