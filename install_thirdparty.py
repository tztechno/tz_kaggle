import sys
from pathlib import Path

# 親リポジトリの root から見た thirdparty フォルダを自動追加
ROOT = Path(__file__).parent
THIRD_PARTY = ROOT / "thirdparty"

# thirdparty 配下のすべてのディレクトリを sys.path に追加
for child in THIRD_PARTY.iterdir():
    if child.is_dir():
        sys.path.insert(0, str(child))

# これで child_lib1 や child_lib2 を import 可能
import child_lib1
import child_lib2

# 例: child_lib1 の関数を使う
child_lib1.some_function()
