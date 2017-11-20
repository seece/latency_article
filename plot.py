import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt


files = [
        ('Sublime.csv', 'Sublime Text'),
        ('gvim.csv', 'GVim'),
        #('Notepad.csv', 'Notepad'),
        #('emacs.csv', 'Emacs'),
        #('WordPad.csv', 'WordPad'),
        #('PowerShell.csv', 'PowerShell'),
        #('IDEA.csv', 'IDEA'),
        #('Notepad++.csv', 'Notepad++'),
        ('Microsoft.csv', 'VS 2013'),
        #('MSVC_vsvim.csv', 'VS 2013 & VSvim'),
        ('Writer.csv', 'LibreOffice Writer'),
        #('putty_local_ssh.csv', 'PuttyTray SSH'),
        #('Counter-Strike_smallwindow.csv', 'CS 1.6 chat'),
        ('Slack.csv', 'Slack (Firefox 57)'),
        ('MINGW64.csv', 'Git Bash (Mintty)'),
        ]


sets = []
prefix="win10"

for path, title in files:
    data = genfromtxt(prefix+"/"+path, delimiter=',')
    sets.append(data)

"""
typodata = genfromtxt("typometer/results.csv", delimiter=',')
sets = []
for i in range(typodata.shape[1]):
    sets.append(typodata[1:, i])


files = [
    ("", "gvim"),
    ("", "emacs"),
    ("", "git bash"),
    ("", "notepad"),
    ("", "vbox_terminal"),
    ("", "vs2013"),
    ("", "powershell"),
    ("", "sublime"),
    ("", "notepad++"),
]
"""

#plt.subplot(211)
#plt.figure(figsize=(50,100))
#n, bins, patches = plt.hist(data, 100, facecolor='g', alpha=0.75)
#plt.hist(data, len(data), alpha=0.75)

plt.style.use('ggplot')

fig, ax = plt.subplots(len(sets), sharex=True, figsize=(8, 3))
#fig.set_size_inches(10, 5.5)

#plt.rcParams["figure.figsize"] = (5, 10)

#plt.yticks([])

for i, x in enumerate(sets):
    path, title = files[i]

    ax[i].scatter(x, np.random.rand(len(x)), facecolor='r', alpha=0.5, s=3)
    ax[i].set_yticklabels([])
    ax[i].set_title(title, rotation='horizontal', loc='left', x=-0.2, y=0.0, fontsize=10)
    ax[i].tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left='off',
    right='off') # labels along the bottom edge are off
    ax[i].set_xlim([0, 120])
    #ax[i].margins(x=0)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)

fig.tight_layout(w_pad=0, h_pad=0)
plt.subplots_adjust(top=0.90, bottom=0.2)
#plt.subplot(212)
#n, bins, patches = plt.hist(data, 100, facecolor='g', alpha=0.75)
plt.xlabel("Latency (ms)", fontsize=10)
plt.suptitle("Measured input latency on Windows 10")

fig.savefig('img/plot.svg')
plt.show()

