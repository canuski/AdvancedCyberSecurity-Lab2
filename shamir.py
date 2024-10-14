# op linux!
from sslib import shamir
required_shares = 2
distributed_shares = 2
shamir.to_base64(shamir.split_secret("this is my secret".encode('ascii'), required_shares, distributed_shares))
