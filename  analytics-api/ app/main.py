from fastapi import FastAPI
from connection import *
from dal import *


app = FastAPI()

@app.get("/analytics/top-customers")
def analytics_top_customers():
    
    cursor.execute(analytics_top_customers_function())
    rows = cursor.fetchall()

    cursor.close()
    mysql.close()
    return rows



@app.get("/analytics/customers-without-orders")
def analytics_customers_without_orders():
    cursor.execute(analytics_customers_without_orders_function())
    rows = cursor.fetchall()

    cursor.close()
    mysql.close()
    return rows



@app.get("/analytics/zero-credit-active-customers")
def analytics_zero_credit_active_customers():
    cursor.execute(analytics_zero_credit_active_customers_function())
    rows = cursor.fetchall()

    cursor.close()
    mysql.close()
    return rows

