```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/_quick_tcp_nmap.txt" -oX "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/xml/_quick_tcp_nmap.xml" 192.168.217.194

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/_full_tcp_nmap.txt" -oX "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/xml/_full_tcp_nmap.xml" 192.168.217.194

feroxbuster -u http://192.168.217.194:80/ -t 10 -w /home/dotwut/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.217.194:80/.well-known/security.txt

curl -sSikf http://192.168.217.194:80/robots.txt

curl -sSik http://192.168.217.194:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://192.168.217.194:80 2>&1 | tee "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.217.194

whatweb --color=never --no-errors -a 3 -v http://192.168.217.194:80 2>&1

wkhtmltoimage --format png http://192.168.217.194:80/ /home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp80/tcp_80_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 7744 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp7744/tcp_7744_ssh_nmap.txt" -oX "/home/dotwut/Labs/dc-2/results/192.168.217.194/scans/tcp7744/xml/tcp_7744_ssh_nmap.xml" 192.168.217.194


```