
def get_tables_list_query():

        """
        Description
        -> get_tables_list_query (method): Function that returns the query used for extracting the list of tables from a Postgres table
     
        
        Pseudo-Code
        -> Create and object containing the query in string type
        -> return the query object       
        """

        
        query="select table_schema || '.' || table_name as table_name from information_schema.tables where table_schema not like 'pg_catalog' and table_schema not like 'information_schema'; "
        return query

def get_table_data_query(schema_name, table_name):

        """
        Description
        -> get_table_data_query (method): Function that returns the query used for extracting the content of a Postgres table

        Pseudo-Code
        
        -> Create and object containing the query in string type
        -> query inludes selecting all columns from the inputted <schema_name> and <table_name> 
        -> return the query object
        """


        query =f"""
        SELECT * FROM {schema_name}.{table_name}
        """
                
        return query
            
                
    


def get_table_schema_query(schema_name, table_name):



        """

        Description
        -> get_table_schema_query (method): Function that returns the query used for extracting the list of columns from a Postgres table and their information

        Pseudo-Code
    
        -> Create and object containing the query in string type with f string to input the function's argument to the string
        -> query inludes selecting all columns from the inputted <schema_name> and <table_name> 
        -> return the query object
        
        """


        query= f"""
        select  
        ic.table_name ,
        ic.column_name,
        ic.data_type,
        ccu.constraint_name as primary_key,
        ic.is_nullable ,
        ic.character_maximum_length ,
        ic.numeric_precision 
        from information_schema.columns ic 
        left join information_schema.constraint_column_usage ccu 
        on ccu.table_schema = ic.table_schema 
        and ccu.table_name = ic.table_name 
        and ccu.column_name = ic.column_name 
        where ic.table_schema = '{schema_name}'
        and ic.table_name = '{table_name}'
        """
        return query
