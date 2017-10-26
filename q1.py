#!/usr/bin/python3

import pandas as pd
import numpy as np
import pprint
import time

url = 'http://www.atlantapd.org/Home/ShowDocument?id=1448'
fileName = './COBRA-YTD2017.csv'

df = pd.read_csv(fileName, encoding='ascii') #, error_bad_lines=False
pp = pprint.PrettyPrinter(indent=4)
#MI_PRINX,offense_id,rpt_date,occur_date,occur_time,poss_date,poss_time,beat,apt_office_prefix,apt_office_num,location,MinOfucr,MinOfibr_code,dispo_code,MaxOfnum_victims,Shift,
#Avg Day,loc_type,UC2 Literal,neighborhood,npu,x,y
Dictionary = {}
Dictionary['MI_PRINX'] = 'text'
Dictionary['offense_id'] = 'ordinal'
Dictionary['rpt_date'] = 'date/time'
Dictionary['occur_date'] = 'date/time'
Dictionary['occur_time'] = 'date/time'
Dictionary['poss_date'] = 'date/time'
Dictionary['poss_time'] = 'date/time'
Dictionary['beat'] = 'categorical'
Dictionary['apt_office_prefix'] = 'text'
Dictionary['apt_office_num'] = 'text'
Dictionary['location'] = 'categorical'
Dictionary['MinOfucr'] = 'text'
Dictionary['MinOfibr_code'] = 'categorical'
Dictionary['dispo_code'] = 'categorical'
Dictionary['MaxOfnum_victims'] = 'numerical'
Dictionary['Shift'] = 'date/time'
Dictionary['Avg Day'] = 'date/time'
Dictionary['loc_type'] = 'categorical'
Dictionary['UC2 Literal'] = 'categorical'
Dictionary['neighborhood'] = 'text'
Dictionary['npu'] = 'text'
Dictionary['x'] = 'numeric'
Dictionary['y'] = 'numeric'

def get_categories(dataframe):
	d = {}
	for x in dataframe:
		d[x] = Dictionary[x]
	return d

result = get_categories(df)
pp.pprint(result)
