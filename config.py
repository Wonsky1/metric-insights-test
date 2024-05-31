import datetime

import numpy as np

YEAR = 2023

START_MONTH = 1
START_DAY = 1
END_MONTH = 12
END_DAY = 31

START_DATE = datetime.date(YEAR, START_MONTH, START_DAY)
END_DATE = datetime.date(YEAR, END_MONTH, END_DAY)

DEFAULT_SALE_QUANTITY = np.random.normal(loc=300, scale=75)
