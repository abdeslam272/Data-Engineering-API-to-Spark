import psycopg2
from typing import List, Dict, Tuple, Union
import pandas as pd
import numpy as np
import datetime
import time
import random


class API_data_generator():
  def __init__() -> None:
    pass

  def connect_to_postgres(self, host='192.168.1.193', port = 5432, 
                            user='postgres', password='1365', database='API_data'):
    try:
      conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
      cur = conn.cursor()
      print("Connection Succesful")
      return conn, cur
    except Exception as e:
      print(e)
      raise Exception("Connection Failed")
      
