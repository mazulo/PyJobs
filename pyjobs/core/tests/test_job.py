from django.test import TestCase

from pyjobs.core.models import Job


class TestGetPremiumJobs(TestCase):

    def test_when_there_is_premium_job_return_it(self):
        Job.objects.create(
            title="Vaga 1",
            workplace="Sao Paulo",
            company_name="XPTO",
            company_email="vm@xpto.com",
            description="Job bem maneiro",
            premium=True,
            public=True,
        )

        count = Job.objects.premium().count()

        self.assertEqual(count, 1)
