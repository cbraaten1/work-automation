'Activating operating system.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Verb RunAs -Wait

'INSTALLING REQUIRED IT SOFTWARE.'
'Setting Default Printers.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Mapping users network drives.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing inventory management tool.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing vulnerability management tool.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing docking station client.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -ArgumentList -silent -Wait

'Installing VPN client.'
Copy-Item -Path \\path\to\the\installer\(bat,exe,msi) -Destination C:\Users\$env:USERNAME\Documents -Recurse
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing security tool.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing bios update.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait

'Installing Microsoft program.'
Start-Process \\path\to\the\installer\(bat,exe,msi,txt)
Start-Process \\path\to\the\installer\(bat,exe,msi) -Verb RunAs -Wait
Start-Sleep -Seconds 60
Start-Process \\path\to\the\installer\(bat,exe,msi)

'Uninstalling Microsoft program.'
Start-Process \\path\to\the\installer\(bat,exe,msi) -Verb RunAs

'NEW EMPLOYEE PHONE INFORMATION.'
$new_employee = Read-Host -Prompt 'Is this user a new employee? '
if(($new_employee -eq 'y') -or ($new_employee -eq 'yes')){
    $desk_phone = Read-Host -Prompt 'Does the user need a desk phone? '
    if(($desk_phone -eq 'y') -or ($desk_phone -eq 'yes')){
        $phone_number = Read-Host 'Please enter the users phone number: '
        $fax_number = Read-Host 'Please enter the users fax number: '
        $forced_auth = Read-Host 'Please enter the Forced Authentication Code: '
        $voicemail_pin = Read-Host 'Please enter the Voicemail PIN: '
        $extension_mobility = Read-Host 'Please enter the Extension Mobility PIN: '
        'Writing text file for phone information.'
        Add-Content -Path "\\path\to\the\installer\(bat,exe,msi,txt)" -Value "Your company phone number is: $phone_number`nYour fax number is: $fax_number`nYour forced authentication code is: $forced_auth`nYour voicemail pin is: $voicemail_pin`nYour extension mobility pin is: $extension_mobility"
        'Copy Onboarding Documentation.'
        Copy-Item -Path \\path\to\the\installer\(bat,exe,msi) -Destination C:\Users\$env:USERNAME\Desktop -Recurse
        'Removing phone information text file from Onboarding Instructions Folder.'
        Remove-Item -Path "\\path\to\the\installer\(bat,exe,msi,txt)"
    }else{        
    'Copy Onboarding Documentation.'
    Copy-Item -Path \\path\to\the\installer\(bat,exe,msi) -Destination C:\Users\$env:USERNAME\Desktop -Recurse
    }
}else{
    'Please continue with the requested applications.'
}

'PLEASE SELECT THE APPLICATIONS REQUESTED FOR THE USER.'
$program_a = Read-Host -Prompt 'Does the user need Program A?: '
if(($program_a -eq 'y') -or ($program_a -eq 'yes')){
    'Installing Program A.'
    Invoke-Item \\path\to\the\installer\(bat,exe,msi,txt)
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'Installing Program A.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}

$program_b = Read-Host -Prompt 'Does the user need Program B?: '
if(($program_b -eq 'y') -or ($program_b -eq 'yes')){
    'Copying Program B Sessions to Users Documents Folder.'
    Copy-Item -Path \\path\to\the\installer\(bat,exe,msi) -Destination C:\Users\$env:USERNAME\Documents -Recurse
    'Installing Program B.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
    'Installing Program B.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'Program B was declined.'
}

$program_c = Read-Host -Prompt 'Does the user need Program C Client?: '
if(($program_c -eq 'y') -or ($program_c -eq 'yes')){
   'Opening Text File for Program C Client.'
    Start-Process \\path\to\the\installer\(bat,exe,msi,txt)
}else{
    'Program C was declined.'
}

$program_d = Read-Host -Prompt 'Does the user need Program D?: '
if(($program_d -eq 'y') -or ($program_d -eq 'yes')){
    'Installing Program D.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'Program D was declined.'
}

$program_e = Read-Host -Prompt 'Does the user need Program E?: '
if(($program_e -eq 'y') -or ($program_e -eq 'yes')){
    'Installing Program E.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'Program E was declined.'
}

$program_f = Read-Host -Prompt 'Have you moved the users computer into the correct AD Group? '
if(($program_f -eq 'y') -or ($program_f -eq 'yes')){
    'Running Program F.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Verb RunAs
}else{
    'Please move users computer into the correct AD Group and run the Program F file manually as Administrator.'
}

Start-Process \\path\to\the\installer\(bat,exe,msi)

$program_g = Read-Host -Prompt 'Does the user use Program G?: '
if(($program_g -eq 'y') -or ($program_g -eq 'yes')){
    'Installing Program G.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'User does not use Program G was declined'
}

$program_h = Read-Host -Prompt 'Does the user use Program H?: '
if(($program_h -eq 'y') -or ($program_h -eq 'yes')){
    'Installing Program H.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'User does not use Program H.'
}

$program_i = Read-Host -Prompt 'Does the user use Program I?: '
if(($program_i -eq 'y') -or ($program_i -eq 'yes')){
    'Installing Program I.'
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'User does not use Program I'
}

$program_j = Read-Host -Prompt 'Does the user need Program J?: '
if(($program_j -eq 'y') -or ($program_j -eq 'yes')){
    'Installing Program J.'
    Invoke-Item \\path\to\the\installer\(bat,exe,msi,txt)
    Start-Process \\path\to\the\installer\(bat,exe,msi) -Wait
}else{
    'Program J was declined.'
}

Pause
