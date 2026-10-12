# build.ps1 -- build one lab's slides and render them to PNG review sheets.
# Usage: powershell -File build.ps1 <N> <reviewDir>
# Needs python-pptx and Pillow on PYTHONPATH, and PowerPoint (for rendering).
param([int]$Lab, [string]$Review)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $here
try {
    python "lab$($Lab)_slides.py"
    if ($LASTEXITCODE -ne 0) { exit 1 }
    if ($Review) {
        & powershell -NoProfile -File render.ps1 "..\Lab$Lab\Lab$Lab-Slides.pptx" $Review | Out-Null
        python contact.py $Review
    }
} finally {
    Pop-Location
}
