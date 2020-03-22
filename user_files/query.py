SLT_FILES = """
SELECT f.id_file, f.file, f.url 
  FROM (
    SELECT id_user FROM users
      WHERE email = $1
    ) u NATURAL JOIN files f
"""

SLT_ID_USER = """
SELECT id_user FROM users
  WHERE email = $1;  
"""

INS_FILE = """
INSERT INTO files (id_user, file, url)
  VALUES ($1, $2, $3);
"""