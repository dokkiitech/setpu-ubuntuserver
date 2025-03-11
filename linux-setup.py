import subprocess

def run_command(command):
    """指定したコマンドを実行し、出力を表示する"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def setup_node():
    print("[1/5] システムをアップデート中...")
    run_command("sudo yum update -y")
    
    print("[2/5] 必要なパッケージをインストール中...")
    run_command("sudo yum install -y curl tar git gcc gcc-c++ make")
    
    print("[3/5] Node.js (LTS) をインストール中...")
    run_command("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash")
    run_command("export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\ . \"$NVM_DIR/nvm.sh\" && nvm install --lts")
    run_command("export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\ . \"$NVM_DIR/nvm.sh\" && nvm use --lts")
    
    print("[4/5] npm のバージョン確認...")
    run_command("npm -v")
    
    print("[5/5] pm2 をインストール（オプション）...")
    run_command("npm install -g pm2")
    
    print("Node.js のバージョンを確認...")
    run_command("node -v")
    
    print("✅ Node.js 環境のセットアップが完了しました！")

if __name__ == "__main__":
    setup_node()
