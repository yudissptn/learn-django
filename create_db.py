import psycopg

with psycopg.connect("dbname=postgres user=postgres host=db port=5432 password=postgres", autocommit=True) as conn:

        with conn.cursor() as cur:
            cur.execute("""
                CREATE DATABASE test_db
                        """)
        conn.commit()
    
print("Created suceessfully!!!")