set EXE=C:\dev\vs\lag\Release\lagmeasure.exe
start C:\Users\user\AppData\Local\atom\atom.exe atom.txt
timeout 5
%EXE% app-1 100 100 > Atom.out
taskkill /F /IM atom.exe
pause

rem start C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2017.2.5\bin\idea64.exe C:\dev\measurements\idea.txt
rem C:\dev\vs\lag\Release\lagmeasure.exe IDEA 100 100 > IDEA.out

rem C:\dev\vs\lag\Release\lagmeasure.exe PowerShell 100 100 > PowerShell.out
rem C:\dev\vs\lag\Release\lagmeasure.exe Counter-Strike 100 100 > Counter-Strike.out

rem Visual Studio
rem C:\dev\vs\lag\Release\lagmeasure.exe Microsoft 100 100 30 > Microsoft.out