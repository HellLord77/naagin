$content = Get-Content -Path "winhttp.cpp" -Raw
$content = $content.Replace("real_winhttp.dll", "C:\\Windows\\System32\\winhttp.dll")
$content | Set-Content -Path "winhttp.cpp"

cmake -B build
cmake --build build --config=Release
