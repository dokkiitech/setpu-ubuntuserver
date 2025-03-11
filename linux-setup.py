import os
import subprocess

def run_command(command):
    print(f"Executing: {command}")
    process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    if process.stdout:
        print(process.stdout)
    if process.stderr:
        print(process.stderr)

def install_dependencies():
    print("Installing required dependencies...")
    run_command("sudo yum update -y")
    run_command("sudo yum groupinstall -y 'Development Tools'")
    run_command("sudo yum install -y curl tar git gcc gcc-c++ make")

def install_nvm():
    print("Installing NVM (Node Version Manager)...")
    run_command("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash")
    run_command("export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\ . \"$NVM_DIR/nvm.sh\" && nvm install --lts")

def configure_node():
    print("Setting up Node.js environment...")
    run_command("export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\ . \"$NVM_DIR/nvm.sh\" && nvm use --lts")
    run_command("node -v")
    run_command("npm -v")
    run_command("npm install -g npm")
    run_command("npm install -g yarn")
    run_command("npm install -g pm2")

def main():
    install_dependencies()
    install_nvm()
    configure_node()
    print("Node.js setup is complete!")

if __name__ == "__main__":
    main()
