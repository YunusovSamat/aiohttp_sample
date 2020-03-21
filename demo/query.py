SLT_USER = """
SELECT email, password FROM users 
  WHERE email = $1;
"""

INS_USER = """
INSERT INTO users (email, name, surname, password) 
  VALUES ($1, $2, $3, $4);
"""