from keycloak import KeycloakOpenID
import os


# Configure client
keycloak_openid = KeycloakOpenID(server_url="https://oauth.ias-test.energo.net/",
                                 verify=False,  # отмена проверки сертификата https
                                 client_id="backend",
                                 realm_name="vitenergo",
                                 client_secret_key=os.environ.get('CLIENT_SECRET_KEY',)
                                 )

# Get WellKnown
config_well_known = keycloak_openid.well_known()
print(config_well_known)
print(config_well_known["userinfo_endpoint"])


# Get Code With Oauth Authorization Request
auth_url = keycloak_openid.auth_url(
    redirect_uri="http://localhost:8585/auth/",
    scope="email",
    state="your_state_info"
)
print(auth_url)


# # Get Access Token With Code
# access_token = keycloak_openid.token(
#     grant_type='authorization_code',
#     code='the_code_you_get_from_auth_url_callback',
#     redirect_uri="http://localhost:8585/auth/"
# )
#
#
# # Get Token
# token = keycloak_openid.token("user", "password")
# # token = keycloak_openid.token("user", "password", totp="012345")
#
# # Get token using Token Exchange
# token = keycloak_openid.exchange_token(token['access_token'], "my_client", "other_client", "some_user")
#
# # Get Userinfo
# userinfo = keycloak_openid.userinfo(token['access_token'])
#
# # Refresh token
# token = keycloak_openid.refresh_token(token['refresh_token'])
#
# # Logout
# keycloak_openid.logout(token['refresh_token'])
#
# # Get Certs
# certs = keycloak_openid.certs()
#
# # Get RPT (Entitlement)
# token = keycloak_openid.token("user", "password")
# rpt = keycloak_openid.entitlement(token['access_token'], "resource_id")
#
# # Instropect RPT
# token_rpt_info = keycloak_openid.introspect(
#     keycloak_openid.introspect(
#         token['access_token'],
#         rpt=rpt['rpt'],
#         token_type_hint="requesting_party_token"
#     )
# )
#
#
# # Introspect Token
# token_info = keycloak_openid.introspect(token['access_token'])
#
# # Decode Token
# KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
# options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
# token_info = keycloak_openid.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)
#
# # Get permissions by token
# token = keycloak_openid.token("user", "password")
# keycloak_openid.load_authorization_config("example-authz-config.json")
# policies = keycloak_openid.get_policies(token['access_token'], method_token_info='decode', key=KEYCLOAK_PUBLIC_KEY)
# permissions = keycloak_openid.get_permissions(token['access_token'], method_token_info='introspect')