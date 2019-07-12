#!/usr/bin/env python
import sys
from ingest.utils.s2s_token_client import S2STokenClient
from ingest.utils.token_manager import TokenManager

if __name__ == '__main__':

    key_file = sys.argv[1]
    client = S2STokenClient()
    client.setup_from_file(key_file)
    token_manager = TokenManager(client)
    token = token_manager.get_token()
    print(f'Bearer {token}')
