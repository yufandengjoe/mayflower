import abc
import math
import numbers
import numpy as np
import scipy.optimize
import scipy.stats
import time

from math import exp

from functions.market.instrument import mf_option
from functions.utility import mf_data_type


class binomial_tree:

    def __init__(self, **kwargs):

        # pass on all kwargs into __init__, use as binomial_tree(**dictionary)
        self.__dict__.update(kwargs)
        return None

    def _dividend_pv(self, steps, starting_step, unit_time_interval):
        '''
        calculate the PV of dividend
            - if yield is not a function, pv = 0
            - if yield is a function and function output is number,
                dividend pv is sum of dividends 
                discounted at mid-point time of every time interval
        '''
        if not hasattr(self.__dict__.get('yield_'), '__call__'):
            return 0
        else:
            dividend_pv = 0
            for step in range(starting_step, steps):
                time_previous = step * unit_time_interval
                time_next = time_previous + unit_time_interval
                dividend = self.__dict__.get('yield_')(
                    time_previous, time_next)
                if mf_data_type.is_number(dividend):
                    time_mid = 0.5 * (time_previous + time_next)
                    dividend_pv += exp(-self.__dict__.get(
                        'riskless_rate') * time_mid) * dividend
            return dividend_pv

    def _spot_price(self,
                    spot_rate_setup,
                    steps,
                    starting_step,
                    unit_time_interval,
                    up_multiplier,
                    num_ups,
                    num_downs):
        '''
        calculate spot price as baseline spot + dividend pv
        '''
        return spot_rate_setup + self._dividend_pv(
            steps=steps,
            starting_step=starting_step,
            unit_time_interval=unit_time_interval
        ) * (up_multiplier ** (num_ups - num_downs))

    def _node_value(self,
                    spot_rate_setup,
                    steps,
                    starting_step,
                    unit_time_interval,
                    up_multiplier,
                    up_probability,
                    num_ups,
                    num_downs,
                    value_cache
                    ):
        '''
        calculate the node value at step = starting_step
        '''
        value_cache_key = (starting_step, num_ups, num_downs)
        if value_cache_key not in value_cache:
            spot = self._spot_price(
                spot_rate_setup=spot_rate_setup,
                steps=steps,
                starting_step=starting_step,
                unit_time_interval=unit_time_interval,
                up_multiplier=up_multiplier,
                num_ups=num_ups,
                num_downs=num_downs
            )
            if self.__dict__.get('option_type') == mf_option.Option_type.Call:
                payoff = max(0, spot - self.__dict__.get('strike'))
            if self.__dict__.get('option_type') == mf_option.Option_type.Put:
                payoff = max(0, self.__dict__.get('strike') - spot)

            if starting_step >= steps:
                pv = payoff
            else:
                future_value = up_probability * self._node_value(
                    spot_rate_setup=spot_rate_setup,
                    steps=steps,
                    starting_step=starting_step + 1,
                    unit_time_interval=unit_time_interval,
                    up_multiplier=up_multiplier,
                    up_probability=up_probability,
                    num_ups=num_ups + 1,
                    num_downs=num_downs,
                    value_cache=value_cache
                ) + (1 - up_probability) * self._node_value(
                    spot_rate_setup=spot_rate_setup,
                    steps=steps,
                    starting_step=starting_step + 1,
                    unit_time_interval=unit_time_interval,
                    up_multiplier=up_multiplier,
                    up_probability=up_probability,
                    num_ups=num_ups,
                    num_downs=num_downs + 1,
                    value_cache=value_cache
                )
                pv = exp(self.__dict__.get(
                    'riskless_rate') * unit_time_interval) * future_value

    def option_value(self,
                     steps=25,
                     sensitivity_degree=2
                     ):
        '''
        take in option inputs and return option price and greeks
            - sensitivity_degree controls for greeks calculation
            - 0 to turn off greek calculation
            - 1 to turn off rho and vega
            - 2 calculates all greeks
        '''

        value_cache = {}
        unit_time_interval = float(self.__dict__.get('maturity'))/steps
        up_multiplier = exp(self.__dict__.get('vol') *
                            (unit_time_interval ** 0.5))
        down_multiplier = 1.0 / up_multiplier
        up_probability = (exp((self.__dict__.get('riskless_rate') - self.__dict__.get(
            'yield_')) * unit_time_interval) - down_multiplier) / (
                up_multiplier - down_multiplier)

        # if yield is a function, reset the starting value to be 0
        # if yield is a constant, use constant as yield
        yield_ = 0 if hasattr(self.__dict__.get('yield_'),
                              '__call__') else self.__dict__.get('yield_')

        spot_rate_setup = self.__dict__.get('spot_rate') - self._dividend_pv(
            steps=steps,
            starting_step=0,
            unit_time_interval=unit_time_interval
        )
