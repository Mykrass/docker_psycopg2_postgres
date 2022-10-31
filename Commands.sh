!cat docker-compose.yml

!docker-compose -p dq_de up -d

# check if postgres docker instance is alive
!docker ps

# retrieve the ip address of the container, seen from the host
#!docker inspect dq_de_db_1 | grep "IPAddress"
