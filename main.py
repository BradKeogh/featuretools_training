from IPython import get_ipython
ipython = get_ipython()

ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

import pandas as pd
import numpy as np

from create_data import make_attendances_dataframe, make_timeindex_dataframe, make_HourlyTimeAttenNum_dataframe

df = make_attendances_dataframe(11)

days = make_timeindex_dataframe(df,'day')

hours = make_timeindex_dataframe(df,'hour','h')

active_visits = make_HourlyTimeAttenNum_dataframe(df,'arrival_datetime','departure_datetime')