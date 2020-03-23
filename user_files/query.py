SLT_FILES = """
SELECT f.id_file, f.file, url, url_download
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
INSERT INTO files (id_user, file, url, url_download)
  VALUES ($1, $2, $3, $4);
"""

DLT_FILE = """
DELETE FROM files 
  WHERE id_file = $1 AND id_user = $2; 
"""

