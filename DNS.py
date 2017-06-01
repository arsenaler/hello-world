from scapy.all import *
domain = "target.ch"
dns_server = "10.190.202.200"
server =[ "www", "www1" , "www2", "ns", "ns1" , "ns2" ,"dns" , "dns1", "dns2", "dns3", "pop", "mail", "smtp" , 
	"pop3",  "test", "dev" , "ads", "adserver", "adsl", "agent", "channel", "dmz", "sz" , "client", "imap" ,
	"http" , "https", "ftp", "ftpserver", "tftp", "ntp" , "ids" , "ips" , "snort" , "imail" , "pops" , 
        "imaps" , "irc" , "linux" , "windows", "log" , "install", "blog" , "host", "printer", "public" , "sql",
        "mysql", "router" , "cisco" , "switch", "telnet", "voip", "webmin" , "ssh", "delevlop" , "pub" , "root" ,
        "user", "xml", "ww" , "telnet", "extern", "intranet" , "extranet", "testing" , "default", "gateway" ,
        "radius" , "noc" , "mobile", "customer" , "chat" , "siprouter" , "sip" , "nms" , "noc", "office" , 
        "voice" , "support" , "spare" , "owa" , "exchange" ]
serverans=[]
cnt=len(server)

for i in range(0, cnt):
    q = server[i]+"."+domain
    ans=sr1(IP(dst=dns_server)/UDP(sport=RandShort())/DNS(rd=1,qd=DNSQR(qname=q)))
    if ans[DNS].ancount == 0:
        print q, "unkown"
        serverans.insert(i,"unkown")
    else:
        print q, ans[DNSRR].rdata
        serverans.insert(i,ans[DNSRR].rdata)

for i in range(0, cnt):
    print server[i]+"."+domain, serverans[i]

for i in range(0, 10000):
    s = RandString(RandNum(1,50))
    s1 =s.lower()
    d = RandString(RandNum(1,20))
    d1 = d.lower()
    t = RandString(RandNum(2,3))
    t1 = t.lower()
    q = s1+"."+d1+"."+t1
    print i ,q
    send(IP(dst="10.190.202.200")/UDP(sport=RandShort())/DNS(rd=1,qd=DNSQR(qname=q)))
else:
    print 'The for loop is over'