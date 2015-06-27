import sqlite3 class Database:
  def __init__(self,name):
    self.db_name=name
    self.connection=sqlite3.connect(self.db_name)
    
  def sql_commit(self,command):
    cursor=self.connection.cursor()
    cursor.execute(command)
    self.connection.commit()
    
  def add_table(self,table_name,schema):
    if table_name not in self.tables():
      self.sql_commit('CREATE TABLE %s(%s)' % (table_name,schema))
    else:
      False#print('table already exists')
  
  def insert_row(self,table_name,row_of_data):
    self.sql_commit('INSERT INTO %s VALUES (%s)' % (table_name,row_of_data))
  
  def dump(self):
    out=[]
    for lines in self.connection.iterdump():
      out.append(lines)
    return out
  
  def get_row(self,table,data_point,index):
    cursor = self.connection.cursor()
    cursor.execute("SELECT %s FROM %s WHERE key='%s';" % (data_point,table,index))
    return cursor.fetchone()[0]
  
  def rows_in_table(self,table_name):
    cursor = self.connection.cursor()
    cursor.execute("SELECT COUNT(*) from %s" % table_name)
    return cursor.fetchone()[0]
  
  def tables(self):
    out=[]
    for i in self.dump():
      if 'TABLE' in i:
        out.append(i[:i.find('(')].split(' ')[-1])
    return(out)
    
  def close(self):
    self.connection.close() files = Database('files.db') files.add_table("images","key 
INTEGER PRIMARY KEY, raw_data TEXT") def download_file(link):
  import urllib2
  import base64
  response = urllib2.urlopen(link)
  return base64.b64encode(response.read())
#test_file=download_file('LINKTOSOMEIMAGE') files.insert_row('images',"'1','%s'" % 
#test_file)
print 'data:image/png;base64,'+files.get_row('images','raw_data','1') files.close()
