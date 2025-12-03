

#!/bin/bash

# --- 設定 ---
ENV_NAME="kaggle_local_env"
# Kaggle Notebookで一般的に使われるライブラリ群
LIBRARIES="pandas numpy matplotlib scikit-learn ipykernel jupyterlab"
PYTHON_VERSION="3.11"

# 1. 仮想環境の作成 (Condaを使用)
echo "🚀 Python $PYTHON_VERSION の仮想環境 '$ENV_NAME' を作成中..."
# Condaで指定したバージョンのPython環境を作成
conda create -n $ENV_NAME python=$PYTHON_VERSION -y || { echo "🔴 エラー: Conda環境の作成に失敗しました。Condaがインストールされているか確認してください。"; exit 1; }

# 2. 仮想環境の**アクティベート**
echo "✅ 仮想環境 '$ENV_NAME' をアクティベート中..."
# Conda環境をアクティベート
source "$(conda info --base)/etc/profile.d/conda.sh" # Condaアクティベートに必要な初期設定
conda activate $ENV_NAME || { echo "🔴 エラー: 仮想環境のアクティベートに失敗しました。"; exit 1; }

# 3. 依存ライブラリのインストール
echo "📦 依存ライブラリをインストール中..."
# pipのアップグレードはインストール前に実行するのが望ましい
pip install --upgrade pip

# 必要なライブラリを一括インストール
# もし requirements.txt があればこちらを使用: pip install -r requirements.txt
pip install $LIBRARIES || { echo "🔴 エラー: ライブラリのインストールに失敗しました。"; deactivate; exit 1; }

# 4. 完了メッセージと次のステップ
echo ""
echo "=================================================="
echo "✅ セットアップが完了しました！"
echo "=================================================="
echo ""

echo "--- 次のステップ ---"
echo "1. **VS Code**でNotebookを開き、右上のカーネルセレクターで **'$ENV_NAME'** を選択してください。"
echo "2. ローカル環境を終了し、ベース環境に戻るには 'deactivate' を実行してください。"

# スクリプト実行後、ユーザーが環境を利用できるようにアクティベートコマンドを提案
echo ""
echo "💡 今すぐこのターミナルで環境を有効にするには、以下を実行してください:"
echo "conda activate $ENV_NAME"

//////////////////////////////

chmod +x setup.sh

./setup.sh

conda activate kaggle_local_env

////////////////////////

💡 今すぐこのターミナルで環境を有効にするには、以下を実行してください:
conda activate kaggle_local_env
(base) shun_ishii@shun-ishiinoMacBook-Pro 11_kaggle % conda activate kaggle_local_env
(kaggle_local_env) shun_ishii@shun-ishiinoMacBook-Pro 11_kaggle % source /Users/shun_ishii/Projects/11_kaggl
e/kaggle_local_env/bin/activate
(kaggle_local_env) (kaggle_local_env) shun_ishii@shun-ishiinoMacBook-Pro 11_kaggle % python --version
Python 3.11.14

////////////////////////

deactivate

rm -rf kaggle_local_env
