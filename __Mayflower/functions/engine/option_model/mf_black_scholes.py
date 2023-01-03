import math
import scipy.optimize
import scipy.stats

from math import exp

from functions.market.instrument import mf_option
from functions.utility import mf_data_type


class black_scholes:

    def __init__(self, **kwargs):

        # pass on all kwargs into __init__, use as black_scholes(**dictionary)
        self.__dict__.update(kwargs)
        return None

    def option_value(self):
        '''
        Take in option inputs and return option price and greeks
        '''

        assert self.__dict__.get('exerise_type') == mf_option.Exerise_type.European, \
            "Black-Scholes does not support early exercise"
        assert (self.__dict__.get('yield_') is None) or mf_data_type.is_number(self.__dict__.get('yield_')), \
            "Black-Scholes does not support discrete dividends"

        squared_maturity = self.__dict__.get('maturity') ** 2
        d1 = (math.log(float(self.__dict__.get('maturity'))))/self.__dict__.get('strike') + (
            self.__dict__.get('riskless_rate') - self.__dict__.get('yield_') +
            0.5 * (self.__dict__.get('vol') ** 2) * self.__dict__.get('maturity') / (
                self.__dict__.get('vol') * squared_maturity
            )
        )
        d2 = d1 - self.__dict__.get('vol') * \
            (self.__dict__.get('maturity') ** 0.5)
        d1_pdf = scipy.stats.norm.pdf(d1)
        riskless_disc = exp(self.__dict__.get('riskless_rate')
                            * self.__dict__.get('maturity'))
        yield_disc = exp(self.__dict__.get('yield_') *
                         self.__dict__.get('maturity'))

        if self.__dict__.get('option_type') == mf_option.Option_type.Call:
            d1_cdf = scipy.stats.norm.cdf(d1)
            d2_cdf = scipy.stats.norm.cdf(d2)
            delta = yield_disc * d1_cdf
            self.val = self.__dict__.get(
                'spot_rate') * delta - riskless_disc * self.__dict__.get('strike') * d2_cdf
            self.theta = -yield_disc * (self.__dict__.get('spot_rate') * d1_pdf * self.__dict__.get('vol')) / (
                2 * squared_maturity) - self.__dict__.get('riskless_rate') * self.__dict__.get(
                    'strike') * riskless_disc * d2_cdf + self.__dict__.get('yield_') * self.__dict__.get(
                        'spot_rate') * yield_disc * d1_cdf
            self.rho = self.__dict__.get(
                'strike') * self.__dict__.get('maturity') * riskless_disc * d2_cdf

        elif self.__dict__.get('option_type') == mf_option.Option_type.Put:
            neg_d1_cdf = scipy.stats.norm.cdf(-d1)
            neg_d2_cdf = scipy.stats.norm.cdf(-d2)
            self.delta = -yield_disc * neg_d1_cdf
            self.val = self.__dict__.get('strike') * riskless_disc * neg_d2_cdf + self.__dict__.get(
                'spot_rate') * delta
            self.theta = -yield_disc * (self.__dict__.get('spot_rate') * d1_pdf * self.__dict__.get('vol')) / (
                2 * squared_maturity) + self.__dict__.get('riskless_rate') * self.__dict__.get(
                    'strike') * riskless_disc * neg_d2_cdf - self.__dict__.get(
                    'yield_') * self.__dict__.get('spot_rate') * yield_disc * neg_d1_cdf
            self.rho = - self.__dict__.get(
                'strike') * self.__dict__.get('maturity') * riskless_disc * neg_d2_cdf

        else:
            raise KeyError("Wrong option type")

        self.vega = self.__dict__.get(
            'spot_rate') * yield_disc * d1_pdf * squared_maturity
        self.gamma = yield_disc * \
            (d1_pdf / (self.__dict__.get('spot_rate') *
             self.__dict__.get('vol') * squared_maturity))

        return {
            "VALUE": self.val,
            "DELTA": self.delta,
            "THETA": self.theta,
            "RHO": self.rho,
            "VEGA": self.vega,
            "GAMMA": self.gamma,
        }
