

from Bio import pairwise2
from Bio.Seq import Seq

# アミノ酸配列の定義
seq1 = Seq("MNAKVLALSLVLVAPGGNKIADLMAAADVFTATGNVLGIVGLVQYG")
seq2 = Seq("MNAKVLALSLVLVAPGGNKIADLMAAADVFTATGNVLGIVGLVQY")

# シーケンスアラインメントの実行
alignments = pairwise2.align.globalxx(seq1, seq2)

# 最も類似度の高いアラインメントを選択
best_alignment = alignments[0]

# アラインメントされた配列を取得
aligned_seq1 = best_alignment[0]
aligned_seq2 = best_alignment[1]

# 類似度の計算
num_matches = 0
num_mismatches = 0
for i in range(len(aligned_seq1)):
    if aligned_seq1[i] == aligned_seq2[i]:
        num_matches += 1
    else:
        num_mismatches += 1
similarity = num_matches / (num_matches + num_mismatches)

print("類似度：", similarity)

