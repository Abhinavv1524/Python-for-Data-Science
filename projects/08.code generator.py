import pyqrcode

s = 'https://youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB&si=ctxuiRwW0oJ1UItY'

url = pyqrcode.create(s)

url.svg("08.QRcode.svg",scale=8)