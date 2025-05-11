from ldap3 import Server, Connection, ALL
from config import LDAP_URL, LDAP_BASE_DN

# def authenticate_ldap_user(username: str, password: str) -> bool:
#     try:
#         user_dn = f"uid={username},{LDAP_BASE_DN}"
#         server = Server(LDAP_URL, get_info=ALL)
#         conn = Connection(server, user=user_dn, password=password, auto_bind=True)
#         return conn.bind()
#     except Exception as e:
#         print(f"LDAP error: {e}")
#         return False


def authenticate_ldap_user(username: str, password: str):
    try:
        user_dn = f"uid={username},{LDAP_BASE_DN}"
        server = Server(LDAP_URL, get_info=ALL)
        conn = Connection(
            server,
            user=user_dn,
            password=password,
            authentication="SIMPLE",
            auto_bind=False
        )

        if not conn.bind():
            print(f"Bind failed: {conn.result}")
            return False, []

        conn.search(
            search_base=user_dn,
            search_filter="(objectClass=*)",
            attributes=["memberof"]
        )

        groups = conn.entries[0]["memberof"].values if conn.entries else []
        return True, groups

    except Exception as e:
        print(f"LDAP error: {e}")
        return False, []
