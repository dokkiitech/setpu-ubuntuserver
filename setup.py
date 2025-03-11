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
    run_command("sudo apt update && sudo apt upgrade -y")
    
    print("[2/5] 必要なパッケージをインストール中...")
    run_command("sudo apt install -y curl")
    
    print("[3/5] Node.js (LTS) をインストール中...")
    run_command("curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -")
    run_command("sudo apt install -y nodejs")
    
    print("[4/5] npm のバージョン確認...")
    run_command("npm -v")
    
    print("[5/5] pm2 をインストール（オプション）...")
    run_command("sudo npm install -g pm2")
    
    print("Node.js のバージョンを確認...")
    run_command("node -v")
    
    print("✅ Node.js 環境のセットアップが完了しました！")

if __name__ == "__main__":
    setup_node()
