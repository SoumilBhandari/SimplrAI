"""Generate the quiz pre/post improvement figure for the SimplrAI paper."""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Bitstream Vera Serif', 'Liberation Serif'],
    'font.size': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.edgecolor': '#2B2B2B',
    'axes.labelcolor': '#2B2B2B',
    'xtick.color': '#2B2B2B',
    'ytick.color': '#2B2B2B',
})

NAVY = '#1F3A68'
TEAL = '#2A9D8F'
CORAL = '#E76F51'
GOLD = '#E9C46A'
GRAY = '#6E7A86'
LIGHT_GRAY = '#D9DEE3'

# ============================================================
# FIGURE 3: Quiz Score Improvements (Pre/Post)
# ============================================================
fig, ax = plt.subplots(figsize=(7.5, 4.2))
conditions = ['SimplrAI', 'ChatGPT', 'Control']
pre_scores = [62.4, 63.1, 61.8]
post_scores = [78.6, 71.2, 65.4]
pre_err = [3.1, 3.4, 3.2]
post_err = [2.8, 3.3, 3.1]
gains = [16.2, 8.1, 3.6]

x = np.arange(len(conditions)); width = 0.36
ax.bar(x - width/2, pre_scores, width, yerr=pre_err, label='Pre-Test',
       color=LIGHT_GRAY, capsize=5, edgecolor='white', linewidth=1.2)
ax.bar(x + width/2, post_scores, width, yerr=post_err, label='Post-Test',
       color=[NAVY, CORAL, GRAY], capsize=5, edgecolor='white', linewidth=1.2)

for i, g in enumerate(gains):
    ax.annotate(f'+{g:.1f} pp',
                xy=(i + width/2, post_scores[i] + post_err[i] + 1.8),
                ha='center', fontsize=9.5, weight='bold',
                color=[NAVY, CORAL, GRAY][i])

ax.set_ylabel('Quiz score (% correct)', fontsize=10.5)
ax.set_xticks(x); ax.set_xticklabels(conditions, fontsize=10.5)
ax.set_ylim(0, 95)
ax.legend(loc='upper right', frameon=False, fontsize=9.5)
ax.grid(axis='y', alpha=0.18, zorder=0); ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('fig3_quiz.pdf', bbox_inches='tight', facecolor='white')
plt.close()
print("fig3_quiz.pdf generated.")
