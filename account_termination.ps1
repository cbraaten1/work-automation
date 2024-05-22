$users=Get-Content C:\file\path\to\a\file\a_text_file.txt # Text file for a username.

'Disabling user profile.'
ForEach ($user in $users)
{
Disable-ADAccount -Identity $users
Write-Host ${users} 'has been disabled.'
}

'Moving user to the Old Items OU.'
Get-ADUser -Identity $users | Move-ADObject -TargetPath OU=Old Items,OU=Company_name,DC=A_Domain_controller,DC=com
$date=Get-Date -Format "MM/dd/yyyy"
Set-ADUser -Identity $users -Description "Disabled" ${date}
Write-Host ${users} 'has been moved to Old Items.'

'Removing Fax & Office Phone Number.'
Set-ADUser -Identify $users -Clear telephoneNumber, ipPhone, facsimileTelephoneNumber
Write-Host "Office, IP Phone, and Fax Number have been removed."

'Saving Member Of attributes.'
(Get-ADUser -Identity $users -Properties MemberOf).MemberOf | Out-File -FilePath C:\file\path\to\a\file\${users}.txt # Saving text file to move to specific folder on drive.
Write-Host 'Member Of attribute has been saved.'

'Removing Member Of attributes.'
foreach($user in $users) {
	$userADObject=Get-ADUser $user -properties MemberOf, DistinguishedName
	foreach($group in $userADObject.MemberOf) {
		$groupDN=(Get-ADGroup $group).DistinguishedName
		$group=New-Object System.DirectoryServices.DirectoryEntry("LDAP://$groupDN");
		if ($group.cn -ne "Domain Users") {
			$group.Properties["member"].Remove($userADObject.DistinguishedName);
			$group.CommitChanges();
			$group.Close();
		}
	}
}