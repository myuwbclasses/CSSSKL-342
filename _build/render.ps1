# render.ps1 -- export every slide of a .pptx to PNG with PowerPoint, for visual checks.
# Usage: powershell -File render.ps1 <deck.pptx> <outDir>
param([string]$Deck, [string]$OutDir)
$Deck = (Resolve-Path $Deck).Path
New-Item -ItemType Directory -Force $OutDir | Out-Null
$OutDir = (Resolve-Path $OutDir).Path
Get-ChildItem $OutDir -Filter *.png | Remove-Item
$app = New-Object -ComObject PowerPoint.Application
try {
    $pres = $app.Presentations.Open($Deck, $true, $false, $false)   # read-only, no window
    foreach ($s in $pres.Slides) {
        $s.Export((Join-Path $OutDir ("slide-{0:D2}.png" -f $s.SlideIndex)), "PNG", 1600, 900)
    }
    $pres.Close()
} finally {
    $app.Quit()
}
Get-ChildItem $OutDir -Filter *.png | ForEach-Object { $_.FullName }
