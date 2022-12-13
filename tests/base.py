from unittest import TestCase

from py_amortization.base import AmortizationBase
from py_amortization.payment_frequency import PaymentFrequency as PF


class Base(TestCase):

    def get_params(self, param: int) -> dict: ...
    def get_instance(self) -> AmortizationBase: ...
    def get_result(self, param: int): ...

    def test_monthly(self) -> None:
        self.assertEqual(
            self.get_instance().monthly(**self.get_params(PF.MONHTLY)),
            self.get_result(PF.MONHTLY)
        )

    def test_semi_monthly(self) -> None:
        self.assertEqual(
            self.get_instance().semi_monthly(**self.get_params(PF.SEMI_MONHTLY)),
            self.get_result(PF.SEMI_MONHTLY)
        )

    def test_bi_weekly(self) -> None:
        self.assertEqual(
            self.get_instance().bi_weekly(**self.get_params(PF.BI_WEEKLY)),
            self.get_result(PF.BI_WEEKLY)
        )

    def test_weekly(self) -> None:
        self.assertEqual(
            self.get_instance().weekly(**self.get_params(PF.WEEKLY)),
            self.get_result(PF.WEEKLY)
        )

    def test_daily(self) -> None:
        self.assertEqual(
            self.get_instance().daily(**self.get_params(PF.DAILY)),
            self.get_result(PF.DAILY)
        )

    def test_bi_monthly(self) -> None:
        self.assertEqual(
            self.get_instance().bi_monthly(**self.get_params(PF.BI_MONTHLY)),
            self.get_result(PF.BI_MONTHLY)
        )

    def test_quarterly(self) -> None:
        self.assertEqual(
            self.get_instance().quarterly(**self.get_params(PF.QUARTERLY)),
            self.get_result(PF.QUARTERLY)
        )

    def test_semi_annual(self) -> None:
        self.assertEqual(
            self.get_instance().semi_annual(**self.get_params(PF.SEMI_ANNUAL)),
            self.get_result(PF.SEMI_ANNUAL)
        )

    def test_annual(self) -> None:
        self.assertEqual(
            self.get_instance().annual(**self.get_params(PF.ANNUAL)),
            self.get_result(PF.ANNUAL)
        )
