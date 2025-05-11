from dotenv import load_dotenv
import os

load_dotenv()

# LDAP Config
LDAP_URL = os.getenv("LDAP_URL")
LDAP_BASE_DN = os.getenv("LDAP_BASE_DN")

# JWT Config
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")