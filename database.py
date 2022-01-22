import mysql.connector as conn
    
def insert_Record(id,name,email,location,salary,band):
        """This function is to insert records from table"""
        try:
            connection=conn.connect(host='localhost',user='root',password='priya!08',database="emp1")
            My_Cursor=connection.cursor()
            query=""" insert into emp1.EMPLOYEE(eid,eName,Email,eLocation,eSalary,eBand) values (%s,%s,%s,%s,%s,%s)"""
            val=(id,name,email,location,salary,band)
            My_Cursor.execute(query,val)
            connection.commit()
            My_Cursor.close()
        except Exception as e:
            raise Exception (f"insert_Record():Something went on inserting the record"+str(e))
   

def select_Record():
    """This function is to select records from table"""
    try:
        connection=conn.connect(host='localhost',user='root',password='priya!08',database="emp1")
        My_Cursor=connection.cursor()
        My_Cursor.execute(" select * from EMPLOYEE ")
        posts=My_Cursor.fetchall()
        return posts
    except Exception as e:
            raise Exception (f"select_Record():Something went on Selecting the record"+str(e))

def check_ID(id):
    """This function is to check id record present in table"""
    try:
        connection=conn.connect(host='localhost',user='root',password='priya!08',database="emp1")
        My_Cursor=connection.cursor()
        query=""" select eid from EMPLOYEE  where eid=%s """
        val=(id,)
        My_Cursor.execute(query,val)
        posts=My_Cursor.fetchall()
        for (i,) in posts:
            if (i,)==id:
                pass 
            return id 
    except Exception as e:
            raise Exception (f"check_ID():Something went on checking id"+str(e))

def delete_Record(id):
    """This function is to delete records from table"""
    try:
        connection=conn.connect(host='localhost',user='root',password='priya!08',database="emp1")
        My_Cursor=connection.cursor()
        if id == check_ID(id):
            query = """ DELETE FROM EMPLOYEE WHERE eid = %s """
            val = (id,)
            My_Cursor.execute(query,val)
            connection.commit()
            My_Cursor.close()
            return id
        else:
            My_Cursor.close()
            return 0
    except Exception as e:
        raise Exception (f"(delete_Record()):- Something went on deleting the record"+str(e))        
  
def update_Location(location,id):
    """This function is to update records from table"""
    try:
        connection=conn.connect(host='localhost',user='root',password='priya!08',database="emp1")
        My_Cursor=connection.cursor()
        if id == check_ID(id):
            query = """ UPDATE EMPLOYEE SET eLocation = %s where eid = %s """
            val=(str(location),id)
            My_Cursor.execute(query,val)
            connection.commit()
            My_Cursor.close()
            return id
        else:
            My_Cursor.close()
            return 0
    except Exception as e:
        raise Exception (f"(delete_Record()):- Something went on Upadting the record"+str(e))        
