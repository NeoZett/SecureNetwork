"""
NET.PY - A simple way to authorize and share internet connections.

Ever wanted a easy, secure, and efficient way to share data between 
one device and the other? Well, now you can! In fact, it's super 
easy with our server and client architectures. Give it a try!

VERSION 1.0.0
BY Neo Zetterberg (From sweden)
"""

from .authenticator import SERVER, CLIENT, AuthSocket
from .network import SecureMessage, simple_socket, Server, Client, generate_key, generate_hmac_key