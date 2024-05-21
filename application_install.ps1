'Activating Software A'
Start-Process \\path\to\software\installation\file\a -Verb RunAs -Wait

'INSTALLING REQUIRED IT SOFTWARE.'
'Activating Software B'
Start-Process \\path\to\software\installation\file\b -Wait

'Activating Software C'
Start-Process \\path\to\software\installation\file\c -Wait

'Activating Software D'
Start-Process \\path\to\software\installation\file\d -Wait

'Activating Software E'
Start-Process \\path\to\software\installation\file\e -Wait

'Activating Software F'
Start-Process \\path\to\software\installation\file\f -ArgumentList -silent -Wait

'Activating Software G'
Copy-Item -Path \\path\to\software\installation\file\g -Destination C:\Users\$env:USERNAME\Documents -Recurse
Start-Process \\path\to\software\installation\file\g -Wait

'Activating Software H'
Start-Process \\path\to\software\installation\file\h -Wait

'Activating Software I'
Start-Process \\path\to\software\installation\file\i -Wait

'Activating Software J'
Start-Process \\path\to\software\installation\file\j -Verb RunAs