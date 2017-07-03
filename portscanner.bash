# This is a simple TCP portscanner

for i in {1..65535};    \
  do nc -r -v -z -w 2 {SERVER} $i; \
  sleep 4 ; \ 
  done \
  | tee [SERVER}.openport
