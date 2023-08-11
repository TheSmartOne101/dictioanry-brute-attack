Dictionary & Brute-Force Attack Tool
The Dictionary & Brute-Force Attack Tool is a Python script that allows you to perform dictionary and brute-force attacks on a specified target URL. Customize the attack type, password complexity, and other settings.

Getting Started:
To download and use the tool, just copy these commands in your Linux Terminal:
------------------------------------------------------------------------------
# Clone the repository
git clone https://github.com/bestkaliuser69/dictioanry-brute-attack

# Navigate to the tool's directory
cd dictioanry-brute-attack

# Make the script executable
chmod +x attack.py

# View options and help
./attack.py -h
------------------------------------------------------------------------------

Example Usage
To perform a dictionary attack on a target URL https://example.com/login with the username john.doe, run:

./attack.py -url https://example.com/login -u john.doe -a
This will perform a brute-force attack using letters (both cases), digits, and special characters.

DISCLAIMER:
Use this tool responsibly and with proper authorization. The author of this tool is not liable for any misuse or illegal activities conducted using this tool.

