# PortXplorer
PortXplorer is a Python-based port scanning tool designed to perform deep scans on a target machine, identifying open ports and determining if they are associated with common services like HTTP or HTTPS.

## Installation
### Clone the repository:
  ```
  git clone https://github.com/deep-sengupta/PortXplorer.git
  cd PortXplorer
  ```
### Run the script:
  ```
  python3 portxplorer.py TARGET
  ```
    
### Example:
  ```
  python3 portxplorer.py 93.184.216.34
  ```
### Output Example:
  ```
     ___           _  __  __      _                     
    / _ \___  _ __| |_\ \/ /_ __ | | ___  _ __ ___ _ __ 
   / /_)/ _ \| '__| __|\  /| '_ \| |/ _ \| '__/ _ \ '__|
  / ___/ (_) | |  | |_ /  \| |_) | | (_) | | |  __/ |   
  \/    \___/|_|   \__/_/\_\ .__/|_|\___/|_|  \___|_|   
                           |_|      

  Scanning target 93.184.216.34
  Port 80 is OPEN (HTTP)
  Port 443 is OPEN (HTTPS)
  Time elapsed: 1m 20s
  ```