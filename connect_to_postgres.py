import psycopg2
import pandas as pd

hostname="localhost"
database="dvdrental"
username="postgres"
pwd="-----"
port_id = 1234
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password=pwd,
        port = port_id
    )


    cur = conn.cursor()
    print("Connection Succesful")


    select_script = '''SELECT * FROM actor LIMIT 10'''
    cur.execute(select_script)
    actor_data = cur.fetchall()
    df = pd.DataFrame(actor_data,columns=['actor_id','first_name','last_name','last_update'])
    print(df)

    # Query payment data
    query = '''
        select 
            p.*,
            r.inventory_id
        from payment as p
        join rental as r on
            p.rental_id = r.rental_id
        ''' 
    cur.execute(query)
    payment_data = cur.fetchall()
    df = pd.DataFrame(payment_data, columns=['payment_id', 'customer_id', 'staff_id', 'rental_id', 'amount', 'payment_date', 'inventory_id'])
    print(df)

except Exception as e:
    print(e)
    raise Exception("Connection Failed")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()