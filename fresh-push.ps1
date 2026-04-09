# Create fresh orphan branch without large file history
Set-Location "C:\Users\18574\.qclaw\workspace\earthinghealth-website"

Write-Host "Creating orphan branch (no history)..."
git checkout --orphan fresh-master 2>&1

Write-Host "Adding all current files..."
git add -A 2>&1

Write-Host "Committing..."
git commit -m "Initial commit - website without large videos" 2>&1

Write-Host "Deleting old master branch..."
git branch -D master 2>&1

Write-Host "Renaming fresh-master to master..."
git branch -m fresh-master master 2>&1

Write-Host "Checking new pack size..."
git count-objects -v 2>&1

Write-Host "Force push to GitHub..."
git push -f origin master 2>&1

Write-Host "DONE!"