#!/bin/bash
set -e

echo `service mysql status`

echo 'start mysql....'

service mysql start
sleep 3
echo `service mysql status`

echo 'import data....'
mysql < /mysql/schema.sql
echo 'import data finished....'

sleep 3
echo `service mysql status`

echo 'modify password....'
mysql < /mysql/privileges.sql
echo 'modify password done....'

#sleep 3
echo `service mysql status`
echo `mysql setup finished`
tail -f /dev/null
