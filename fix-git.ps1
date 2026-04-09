# Fix Git push - Remove large video files from git tracking

$site = "C:\Users\18574\.qclaw\workspace\earthinghealth-website"
$video = "$site\video"

Write-Host "=== Step 1: Remove videos from git tracking (keep local files) ==="
Set-Location $site
git rm -r --cached video/factory-tour.mp4 2>&1
git rm -r --cached video/bedsheet-promo.mov 2>&1

Write-Host ""
Write-Host "=== Step 2: Update .gitignore ==="
$gitignorePath = "$site\.gitignore"
$newLine = [Environment]::NewLine + "# Large video files - managed externally" + [Environment]::NewLine + "*.mp4" + [Environment]::NewLine + "*.mov" + [Environment]::NewLine + "*.avi" + [Environment]::NewLine + "*.mkv"
if (Test-Path $gitignorePath) {
    Add-Content -Path $gitignorePath -Value $newLine -Encoding utf8
} else {
    $content = "# Large video files - managed externally" + [Environment]::NewLine + "*.mp4" + [Environment]::NewLine + "*.mov" + [Environment]::NewLine + "*.avi" + [Environment]::NewLine + "*.mkv"
    Set-Content -Path $gitignorePath -Value $content -Encoding utf8
}

Write-Host ""
Write-Host "=== Step 3: Commit changes ==="
git add .gitignore 2>&1
git status --short 2>&1 | Select-Object -First 20

Write-Host ""
Write-Host "Committing..."
$msg = "chore: remove large video files from git (use CDN instead)"
git commit -m $msg 2>&1

Write-Host ""
Write-Host "=== Step 4: Push to GitHub ==="
git push https://github.com/earthinghann-boop/earthing-health-website.git master -v 2>&1

Write-Host ""
Write-Host "=== DONE ==="