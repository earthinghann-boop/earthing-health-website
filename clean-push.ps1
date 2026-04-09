# Clean up stale git objects and retry push
$site = "C:\Users\18574\.qclaw\workspace\earthinghealth-website"
Set-Location $site

Write-Host "Current status:"
git status --short

Write-Host ""
Write-Host "Packing loose objects..."
git pack-refs --all 2>&1

Write-Host ""
Write-Host "Checking what's being pushed..."
git count-objects -v 2>&1

Write-Host ""
Write-Host "Retrying push..."
git push --set-upstream origin master 2>&1