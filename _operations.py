import os, sys

base = r'd:\Homepage\juntaoyou.github.io\_publications'

# Step 1: Delete old placeholder files
files_to_delete = [
    '2009-10-01-paper-title-number-1.md',
    '2010-10-01-paper-title-number-2.md',
    '2015-10-01-paper-title-number-3.md',
    '2024-02-17-paper-title-number-4.md',
    '2025-06-08-paper-title-number-5.md',
]

results = []
deleted = []
not_found = []
for f in files_to_delete:
    path = os.path.join(base, f)
    if os.path.exists(path):
        os.remove(path)
        deleted.append(f)
    else:
        not_found.append(f)

results.append('=== Deleted files ===')
for f in deleted:
    results.append(f'  DELETED: {f}')
for f in not_found:
    results.append(f'  NOT FOUND: {f} (the file did not exist)')

# Step 2: Create ICLR 2026 paper
iclr_content = """---
title: "NextQuill: Causal Preference Modeling for Enhancing LLM Personalization"
collection: publications
category: conferences
permalink: /publication/2026-04-01-nextquill
excerpt: 'Proposes NextQuill, a novel causal preference modeling-based alignment method for LLM personalization.'
date: 2026-04-01
venue: 'International Conference on Learning Representations (ICLR)'
paperurl: 'https://iclr.cc/virtual/2026/poster/10006635'
citation: 'Zhao, X., You, J., Zhang, Y., Wang, W., Cheng, H., Feng, F., Ng, S.-K., Chua, T.-S. (2026). &quot;NextQuill: Causal Preference Modeling for Enhancing LLM Personalization.&quot; <i>ICLR</i>.'
---
"""

p1 = os.path.join(base, '2026-04-01-nextquill.md')
with open(p1, 'w', encoding='utf-8') as f:
    f.write(iclr_content)

# Step 3: Create arXiv paper (CFT)
arxiv_content = """---
title: "Causality-Enhanced Behavior Sequence Modeling in LLMs for Personalized Recommendation"
collection: publications
category: manuscripts
permalink: /publication/2024-10-30-causality-enhanced-behavior
excerpt: 'Proposes Counterfactual Fine-Tuning (CFT), a fine-tuning method that leverages counterfactual information to better model user behavior sequences for personalized recommendation.'
date: 2024-10-30
venue: 'Under Review'
paperurl: 'https://arxiv.org/abs/2410.22809'
citation: 'Zhang, Y., You, J., Bai, Y., Zhang, J., Bao, K., Wang, W., Chua, T.-S. (2024). &quot;Causality-Enhanced Behavior Sequence Modeling in LLMs for Personalized Recommendation.&quot; <i>Under Review</i>.'
---
"""

p2 = os.path.join(base, '2024-10-30-causality-enhanced-behavior.md')
with open(p2, 'w', encoding='utf-8') as f:
    f.write(arxiv_content)

results.append('')
results.append('=== Created files ===')
for f in ['2026-04-01-nextquill.md', '2024-10-30-causality-enhanced-behavior.md']:
    path = os.path.join(base, f)
    if os.path.exists(path):
        size = os.path.getsize(path)
        results.append(f'  CREATED: {f} ({size} bytes)')
    else:
        results.append(f'  FAILED: {f}')

results.append('')
results.append('=== Final directory listing ===')
for f in sorted(os.listdir(base)):
    fpath = os.path.join(base, f)
    if os.path.isfile(fpath):
        results.append(f'  {f} ({os.path.getsize(fpath)} bytes)')

# Write report to a file so we can read it
report = '\n'.join(results)
report_path = r'd:\Homepage\juntaoyou.github.io\_operations_report.txt'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(report)
