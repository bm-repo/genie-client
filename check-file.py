def fun_func(ip: str) -> str:
  # addding a comment1
  if ip == 'input':
    return 'output'
  else:
    return 'something'
 
def define_fun(time: str) -> str:
  #celebrate this
  if time == 'morning':
    return 'having morning tea'
  elif time == 'afternoon':
    return 'black cofee'
  else:
    return 'long walk and workout session'
 
class FunDefHandler():
    def __init__(self, conn_str: str):
      #define connection object
      self.conn = None
    
    def get_conn():
      return self.conn
  
