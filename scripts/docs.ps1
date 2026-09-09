param(
    [ValidateSet('Pack', 'Preflight', 'Publish')][string]$Action = 'Pack',
    [string]$Collection = 'yotta',
    [string]$Base = 'https://docs.yuelili.com'
)
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path $PSScriptRoot -Parent
$taskArchive = Join-Path $taskRoot 'artifacts/docs.zip'
$taskPublisher = Join-Path $PSScriptRoot 'yueli_docs_publish.py'
New-Item -ItemType Directory -Force (Split-Path $taskArchive -Parent) | Out-Null
python (Join-Path $PSScriptRoot 'check-user-docs.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python $taskPublisher pack (Join-Path $taskRoot 'content') --output $taskArchive
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
if ($Action -ne 'Pack') {
    python $taskPublisher $Action.ToLowerInvariant() $taskArchive --base $Base --collection $Collection --locale zh-CN
    exit $LASTEXITCODE
}
