#!/bin/bash
set -e
COLOR="echo -e \\E[1;32m"
COLOR1="echo -e \\E[1;31m"
END="\\E[0m"


node_exporter_install() {
#[ -f ${install_dir} ] || mkdir -p $install_dir
#cd $install_dir
#url=$(curl -ks https://github.com/prometheus/node_exporter/releases|grep linux-amd64.tar.gz|head -1|sed -nr 's#^[^"]*"([^"]+)".*$#https://github.com\1#p')
#wget https://github.com/prometheus/node_exporter/releases/download/v1.2.0/node_exporter-1.2.0.linux-amd64.tar.gz &> /dev/null
#tar xf node_exporter-1.2.0.linux-amd64.tar.gz
#ln -sv /root/node_exporter-1.0.0-rc.0.linux-amd64 edc_node_exporter &> /dev/null
cat > /usr/lib/systemd/system/node-exporter.service <<EOF
[Unit]
Description=This is prometheus node exporter

[Service]
Type=simple
ExecStart=/root/node_exporter-1.3.1.linux-amd64/node_exporter
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl start node-exporter.service
systemctl enable node-exporter.service &> /dev/null
}

node_exporter_install

node_exporter_port=`ss -ntlp | grep -o 9100`
if [ $node_exporter_port == "9100" ];then
    ${COLOR}node-exporter successed${END}
else
    ${COLOR1}node-exporter failed${END}
fi  
