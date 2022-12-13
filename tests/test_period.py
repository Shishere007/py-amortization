from py_amortization import AmortizationPeriod
from py_amortization.payment_frequency import PaymentFrequency as PF
from tests.base import Base


class TestAmortizationPeriod(Base):

    def setUp(self) -> None:
        self.principal = 1000
        self.apr = 3/100
        self.instance = AmortizationPeriod(self.principal, self.apr)
        
        self.result_map = {
            PF.MONHTLY: 84.69,
            PF.SEMI_MONHTLY: 42.32,
            PF.BI_WEEKLY: 39.06,
            PF.WEEKLY: 19.53,
            PF.DAILY: 2.78,
            PF.BI_MONTHLY: 169.60,
            PF.QUARTERLY: 254.71,
            PF.SEMI_ANNUAL: 511.28,
            PF.ANNUAL: 1030.0,
        }

    def get_instance(self) -> AmortizationPeriod:
        return self.instance
    
    def get_params(self, param: int) -> dict:
        return {'amount': self.result_map[param]}

    def get_result(self, param: int):
        return param

