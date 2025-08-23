# Author: Crazy Indian Developer (Vijay Mahajan)
# Date: 2025-08-23
# Description: Simple FTP server script using pyftpdlib for file sharing in local network
# Version: 1.0

import os
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_FTPShare10():
    # I KNOW IT SHOULD BE IN LOWERCASE BY THE WAY IT'S  FTPShare1.0

    # Instantiate an authorizer object to handle authentication (empty, for anonymous access)
    authorizer = DummyAuthorizer()

    # Add an anonymous user who can only read files (permissions: elr)
    # This directory is accessible by anyone without a username or password

    cwd = os.getcwd()
    # cwd - path of current directory
    # we can add custom address - r"C:\Users\Admin\Desktop"
    authorizer.add_anonymous(cwd, perm="elradfmw")

    # FTP handler object
    handler = FTPHandler
    handler.authorizer = authorizer

    ip_list = []
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if not ip.startswith("127."):
            ip_list.append(ip)
    # print(ip_list)

    # Create and configure the FTP server
    server = FTPServer(("0.0.0.0", 2121), handler)
    # Listening on port 2121

    # Start the FTP server
    print("Starting FTPShare1.0 server...")
    for ip in ip_list:
        print("FTPShare1.0 Server Started on  ftp://" + ip)
    server.serve_forever()


if __name__ == "__main__":
    run_FTPShare10()
