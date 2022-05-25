import http.server
from pythonping import ping
from prometheus_client import start_http_server
from prometheus_client import Gauge


Printer1 = Gauge('status1', 'Is target online or not (1/0)')
Printer2 = Gauge('status2', 'Is target online or not (1/0)')
Printer3 = Gauge('status3', 'Is target online or not (1/0)')
Printer4 = Gauge('status4', 'Is target online or not (1/0)')
Printer5 = Gauge('status5', 'Is target online or not (1/0)')


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ##
        # the following bit is ugly as fuck
        # but it works for its intended purpose
        #
        # it will be reworked as a part of
        # learning gitops / CI/CD and docker
        ##
        p = ping('192.168.1.1', count=1)
        if p.success():
            Printer1.set(1)
        else:
            Printer1.set(0)

        p = ping('192.168.1.2', count=1)
        if p.success():
            Printer2.set(1)
        else:
            Printer2.set(0)

        p = ping('192.168.1.3', count=1)
        if p.success():
            Printer3.set(1)
        else:
            Printer3.set(0)

        p = ping('192.168.1.4', count=1)
        if p.success():
            Printer4.set(1)
        else:
            Printer4.set(0)

        p = ping('192.168.1.5', count=1)
        if p.success():
            Printer5.set(1)
        else:
            Printer5.set(0)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World')


def send_ping(ip):
    p = ping(ip, count=1)
    return p


a = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10', '192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15', '192.168.1.16']

status = []
for i in a:
    ans = send_ping(i)
    for j in ans:
        if j.success == True:
            status.append([i, 1])
        else:
            status.append([i, 0])

#print(status)

if __name__ == '__main__':
    start_http_server(8000)
    server = http.server.HTTPServer(('',8001), ServerHandler)
    print('Prometheus metrics available on port 8000 /metrics')
    print('HTTP server available on port 8001')
    server.serve_forever()
