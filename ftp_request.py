import ftplib
import os

#connection parameters
ftpHost = 'test.rebex.net'
ftpPort = 21
ftpUname = 'demo'
ftpPass = 'password'

#create an FTP client instance, use the timeout (seconds) parameter for slow connections only
ftp = ftplib.FTP(timeout=30)

ftp.connect(ftpHost, ftpPort)

ftp.login(ftpUname, ftpPass)

#change working directory
ftp.cwd("/pub/example/")

#list of file names in ftp cwd folder
fnames = ftp.nlst()
# print(fnames)

local_path = '/Users/kariukiupande/Documents/susteq-api-post'

for fname in fnames:
    filename = fname
    local_fn = os.path.join(local_path, os.path.basename(filename))

    with open(local_fn, 'wb') as file:
        retCode = ftp.retrbinary(f"RETR " + filename, file.write)

    if retCode.startswith("226"):
        print("download success!")
    else:
        print("download unsuccessful...")  

#send QUIT command to the FTP server and close the connection
ftp.quit()


print("execution complete...")