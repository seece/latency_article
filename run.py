import subprocess
from time import sleep

def run(cmdlist, outfile):
    f = open(outfile, "w")
    res = subprocess.call(cmdlist, stdout=f)
    f.close()
    return res


def run_async(cmdlist):
    return subprocess.Popen(cmdlist)

lagbin = r"C:\dev\vs\lag\Release\lagmeasure.exe"

# steam.exe -applaunch 10 -window -width 640 -height 480 +map cs_assault
# C:\dev\vs\lag\Release\lagmeasure.exe Strike 3 100 10 0 30

# command to run, window title, sleep, possible cleanup
cmds = [
        ("notepad.exe", "Notepad", 2.0, ""),
        (r"C:\Program Files (x86)\Notepad++\notepad++.exe", "Notepad++", 2.0, ""),
        ([r"C:\Program Files (x86)\Vim\vim80\gvim.exe", "-c", "startinsert", r"C:\dev\measurements\gvim"], "gvim", 0.5, ""),
        ([r"C:\Program Files\Git\git-bash.exe", "--cd-to-home"], "MINGW64", 5.0, ["taskkill", "/IM", "mintty.exe"]),
        ([r"C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.exe", "msvc.txt"], "msvc", 15.0, ""),
        #([r"C:\Users\user\AppData\Local\atom\atom.exe", "atom.txt"], "app-1", 15.0, ["taskkill", "/F", "/IM", "atom.exe"]),
        #([r"C:\tools\emacs\bin\emacs.exe", r"C:\dev\measurements\emacs.txt"], "emacs", 2.0, ""),
        ([r"C:\Program Files\Sublime Text 3\sublime_text.exe"], "Sublime", 5.0, ""),
        #([r"C:\Program Files\Mozilla Firefox\firefox.exe", r"https://someslack.slack.com/messages/D6BRDD9EC/"], "Slack", 30.0, ""),
        ([r"C:\Program Files\Windows NT\Accessories\wordpad.exe"], "WordPad", 5.0, ""),
    (r"C:\Program Files\LibreOffice 5\program\swriter.exe", "Writer", 15.0, ["taskkill", "/F", "/IM", "soffice.bin"]),
        ]

for c in cmds:
    print(c)
    p = run_async(c[0])
    sleep(c[2])
    result = run([lagbin, c[1], "100", "100", "30"], c[1]+".out")
    if result != 0:
        print("Failed: " + str(result))
    p.kill()
    # cleanup command
    if len(c[3]) > 0:
        run(c[3], "temp.log")
