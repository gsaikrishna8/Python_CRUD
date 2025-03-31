from database import  cursor, conn

cursor.execute("""
IF NOT EXISTS(SELECT *  FROM sysobjects WHERE name='Users' AND xtype='U')
CREATE TABLE Users(
   id INT IDENTITY(1,1) PRIMARY KEY,
   name VARCHAR(100),
   email VARCHAR(100)
               
     )
"""
)
conn.commit()