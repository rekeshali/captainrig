# Kill captainrig processes
PID_CAPTAINRIG=$(pgrep -f captainrig.py)

if [ $PID_CAPTAINRIG ]
then
      kill $PID_CAPTAINRIG
      echo $(date) CAPTAINRIG STOPPED
fi

# Start anew
nohup python3 /home/pi/captainrig/captainrig.py 1>/home/pi/captainrig/log.captainrig 2>&1 &
echo $(date) CAPTAINRIG STARTED
