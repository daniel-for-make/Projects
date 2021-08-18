from datetime import datetime as dt

end_time = dt() #end time, if the time does not come, the site will continue to be blocked

sites_to_block = ['facebook.com', 'https://www.facebook.com/'] #block any site you want

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
 
redirect = "127.0.0.1"

def blocksites():
    if dt.now() < end_time:
        print("BLOCK SITES") 
        with open(hosts_path, 'r+') as host_file:
            host_content = host_file.read()
            for site in sites_to_block:
                if site not in host_content:
                    host_file.write(redirect + " " + site + "\n")
    else:
        print("UnBLOCK SITES")
        with open(hosts_path, 'r+') as host_file:
            lines = host_file.readlines()
            host_file.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block): 
                    host_file.write(line)
            host_file.truncate()




if __name__ == "__main__":
    #run manually
    #cron job
    #background
          blocksites()              
