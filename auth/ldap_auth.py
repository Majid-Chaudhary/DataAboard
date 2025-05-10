from ldap3 import Server, Connection, ALL

LDAP_URL = "ldap://localhost"
BASE_DN = "dc=example,dc=org"

def authenticate_ldap_user(username: str, password: str) -> bool:
    try:
        user_dn = f"uid={username},{BASE_DN}"
        server = Server(LDAP_URL, get_info=ALL)
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        return conn.bind()
    except Exception:
        return False
