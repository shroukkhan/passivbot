# Control variable to show or hide output
$showOutput = $true

# Define the python commands to be executed
$commands = @(
    "python backtest.py -s 1000BONKUSDT -le y -se n -lw 0.1222 -sw 0.06667 C:/AgodaGit/passivbot/downloaded_configs/scud2/longs/1000BONKUSDT15477.json",
    "python backtest.py -s 1000BONKUSDT -le y -se n -lw 0.1222 -sw 0.06667 C:/AgodaGit/passivbot/downloaded_configs/scud2/longs/1000BONKUSDT15478.json",
    "python backtest.py -s 1000BONKUSDT -le y -se n -lw 0.1222 -sw 0.06667 C:/AgodaGit/passivbot/downloaded_configs/scud2/longs/1000BONKUSDT15479.json",
    "python backtest.py -s 1000BONKUSDT -le y -se n -lw 0.1222 -sw 0.06667 C:/AgodaGit/passivbot/downloaded_configs/scud2/longs/1000BONKUSDT15480.json",
    "python backtest.py -s 1000BONKUSDT -le y -se n -lw 0.1222 -sw 0.06667 C:/AgodaGit/passivbot/downloaded_configs/scud2/longs/1000BONKUSDT15481.json"
)

# Initialize timing and progress variables
$startTime = [System.Diagnostics.Stopwatch]::StartNew()
$runTimes = New-Object System.Collections.Generic.List[System.TimeSpan]

$totalCommands = $commands.Count

for ($i = 0; $i -lt $totalCommands; $i++) {
    $command = $commands[$i]

    # Output the current command being executed
    $currentCommandNumber = $i + 1
    Write-Host "Executing command $currentCommandNumber of $totalCommands... ($command)"

    # Start the timer for the current command
    $commandTime = [System.Diagnostics.Stopwatch]::StartNew()

    if ($showOutput) {
        # Execute the command and show output
        Invoke-Expression $command
    } else {
        # Execute the command in the background without showing any output
        Start-Job -ScriptBlock { param($cmd) Invoke-Expression $cmd } -ArgumentList $command | Out-Null

        # Wait for the job to complete
        while (Get-Job -State "Running") {
            Start-Sleep -Seconds 1
        }

        # Clean up the completed job
        Get-Job | Remove-Job
    }

    # Stop the timer for the current command and record its duration
    $commandTime.Stop()
    $runTimes.Add($commandTime.Elapsed)

    # Calculate the average duration based on all previous runs
    $averageDuration = ($runTimes | Measure-Object -Property TotalSeconds -Average).Average

    # Estimate time remaining
    $timeRemaining = [TimeSpan]::FromSeconds($averageDuration * ($totalCommands - $completedCommands))

    # Update progress report
    Write-Host "Command $currentCommandNumber complete. Estimated time remaining for remaining commands: $($timeRemaining.ToString("g"))"
}

$startTime.Stop()
Write-Host "All commands executed. Total execution time: $($startTime.Elapsed.ToString("g"))"