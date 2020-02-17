#!/usr/bin/env python3

import re


text = """1331901000.000000	CHEt7z3AzG4gyCNgci	10.10.110.110	50465	1.1.1.1	80	1	HEAD	192.168.229.251	/DEASLog02.nsf	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.010000	CKnDAp2ohlvN6rpiXl	10.10.110.110	50467	1.1.1.1	80	1	GET	cantStopWontStop.com	/believing	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.030000	CNTrjn42F3LB58MZH6	10.10.110.110	50469	1.1.1.1	80	1	PROPFIND	rasberryPI.org	/help	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.040000	C1D7mK1PlzKEnEyG03	10.10.110.110	50471	1.1.1.1	80	1	OPTIONS	pewPew.gov	/	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.050000	CGF1bVMyl9ALKI32l	10.10.110.110	50473	1.1.1.1	80	1	POST	what.org.cn	/nothingToSeehere.exe.png.jpeg	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.070000	CQ7uZu2HtGNngGZl5c	10.10.110.110	50475	1.1.1.1	80	1	PUT	panicATtheDisco.com.in.top	/contactus	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.080000	COdckp4ZoGPteMJ2E4	10.10.110.110	50477	1.1.1.1	80	1	DELETE	mnm.biz	/mockingbird -	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.090000	CzhIEIizmxUoN6gP7	10.10.110.110	50479	1.1.1.1	80	1	HEAD	8.8.8.8	/adminLogin.jsp	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.110000	CkzNrm1sDTsMMEeh9k	10.10.110.110	50481	1.1.1.1	80	1	GET	differentia.mx	/notAmaliciousEXE.exe	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.120000	CyOt6C4vWuJE2n5pDb	10.10.110.110	50483	1.1.1.1	80	1	POST	192.168.229.251	/doladmin.nsf	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.130000	C7tneL2opYeE6W20U6	10.10.110.110	50485	1.1.1.1	80	1	PROPFIND	blackhills.org	/SOC2Report.pdf	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.150000	CIuYWb1zOaIDFu8Dg5	10.10.110.110	50487	1.1.1.1	80	1	PATCH	abc.xyz	/citrixADC.poc	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.160000	ClcI7f3q6nDc0GJTLd	10.10.110.110	50489	1.1.1.1	80	1	PUT	emotet.com	/en/us/Invoice.rtf	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.170000	CeavT14dVasu4fqaDh	10.10.110.110	50491	1.1.1.1	80	1	PUT	princessBride.onion	/domlog.csv	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.190000	CfIUAd6iXq2sUE4i2	10.10.110.110	50493	1.1.1.1	80	1	GET	youGotIt.com	/tryThis	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.200000	CWQnUo4bRUUd8TaOU6	10.10.110.110	50495	1.1.1.1	80	1	PATCH	noNoNO	/events4.top	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.210000	CQ7wGc1ISKHeHWuzi5	10.10.110.110	50497	1.1.1.1	80	1	DELETE	192.168.229.251	/events5.nsf	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.230000	CkTGn021IjmxsCaaIa	10.10.110.110	50499	1.1.1.1	80	1	HEAD	pantomOPBrowasHere.com	/notMalware.exe	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.240000	C1ELOca1D4lcjvx1	10.10.110.110	50501	1.1.1.1	80	1	GET	permOnThatAttitude.org	/brunomars	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-
1331901000.250000	CksTEo6ztvFkHWzq	10.10.110.110	50503	1.1.1.1	80	1	GET	cowsANDpigs.farm	/test	-	Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)	0	0	404	Not Found	-	-	-	(empty)	-	-	-	-	-	-	-"""

def main():
    
    for line in text.split("\n"):
        src_ip, src_port, dst_ip, dst_port, domain, uri = re.search(r"^\S+\s+\S+\s+([\d.]+)\s+(\d+)\s+([\d.]+)\s+(\d+)\s+\S+\s+\S+\s+(\S+)\s+(\S+)\s+.*$", line).groups()
        print(f"{src_ip} // {dst_ip} // {domain}:{dst_port}{uri}") 


main()
