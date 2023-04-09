#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install it and try again."
    exit 1
fi

# Create and activate virtual environment using venv in buildspace
python3 -m venv venv
source venv/bin/activate

# Install rumps and other dependencies
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create the app_launcher.sh file
APP_LAUNCHER="./app_launcher.sh"
cat > "$APP_LAUNCHER" <<EOL
#!/bin/bash

# Activate the virtual environment
source "$(pwd)/venv/bin/activate"

# Launch the app
python3 "$(pwd)/app.py"
EOL

# Make the app_launcher.sh file executable
chmod +x $APP_LAUNCHER

# Create a .plist file for the LaunchAgent
APP_PLIST="$HOME/Library/LaunchAgents/so.buildspace.os.plist"
cat > "$APP_PLIST" <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>so.buildspace.os</string>
    <key>ProgramArguments</key>
    <array>
        <string>$(pwd)/app_launcher.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOL

# Load the LaunchAgent
launchctl load -w "$APP_PLIST"
launchctl start so.buildspace.os
