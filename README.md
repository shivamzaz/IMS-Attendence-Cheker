# Check your Attendence without open internet browser(Semester 7, IMSEC, CSE), Just on Terminal or system notif—
  >> Set your rollno. and rest of details in the script(.py file) as mentioned in couples of above lines
  >> Then open the crontab list by crontab -l in Terminal and edit file by crontab -e
      For every time reminder when sysem will be gooing to  reboot
        add this on the crontab file "@reboot python file_path_name.py" (w/o colon)
