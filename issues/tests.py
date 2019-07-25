from django.test import TestCase
from .models import Issue

# Create your tests here.
class IssueTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Issue model
    """

    def test_str(self):
        test_name = Issue(name='An issue')
        self.assertEqual(str(test_name), 'An issue')