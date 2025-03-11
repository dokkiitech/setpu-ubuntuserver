import subprocess

def run_commands(commands):
    """
    複数のコマンドを1つのシェルセッションで実行します。
    """
    process = subprocess.Popen(
        commands,
        shell=True,
        executable="/bin/bash",  # bash を使用する
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print(stderr.decode())

def setup_node():
    script = r"""
set -e
echo "[1/5] システムをアップデート中..."
sudo yum update -y

echo "[2/5] 必要なパッケージをインストール中..."
# --allowerasing オプションを追加してパッケージの競合を解消
sudo yum install -y --allowerasing curl tar git gcc gcc-c++ make

echo "[3/5] Node.js (LTS) をインストール中..."
# nvm が未インストールの場合のみインストール
if [ ! -d "$HOME/.nvm" ]; then
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
else
    echo "nvm は既にインストールされています"
fi

# nvm の環境変数とスクリプトを読み込む
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"

nvm install --lts
nvm use --lts
nvm alias default "$(nvm current)"

echo "[4/5] npm のバージョン確認..."
npm -v

echo "[5/5] pm2 をインストール（オプション）..."
npm install -g pm2

echo "Node.js のバージョンを確認..."
node -v

echo "✅ Node.js 環境のセットアップが完了しました！"
echo ""
echo "※ 変更を反映するために、エディター（またはターミナル）を再起動してください。"
"""
    run_commands(script)

if __name__ == "__main__":
    setup_node()
