SLT_USER_DATA = """
SELECT email, password FROM users 
  WHERE email = $1;
"""

INS_USER = """
INSERT INTO users (email, name, surname, password) 
  VALUES ($1, $2, $3, $4);
"""

UPD_PASSW = """
UPDATE users SET password = $2
  WHERE email = $1;
"""

DLT_USER = """
DELETE FROM users WHERE email = $1;
"""