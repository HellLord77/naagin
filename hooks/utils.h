#pragma once

#include <windows.h>
#include <tchar.h>
#include <wchar.h>
#include <shlwapi.h>

#include "hook_macro.h"

#pragma comment(lib, "shlwapi.lib")

#define CONFIG_FILE TEXT("config.ini")
#define CONFIG_APP TEXT("naagin")

#define CONFIG_ENABLE_KEY TEXT("enable")
#define CONFIG_HTTPS_KEY TEXT("https")
#define CONFIG_HOST_KEY TEXT("host")
#define CONFIG_PORT_KEY TEXT("port")

#define CONFIG_ENABLE_DEFAULT TRUE
#define CONFIG_HTTPS_DEFAULT FALSE
#define CONFIG_HOST_DEFAULT TEXT("localhost")
#define CONFIG_PORT_DEFAULT 8000

TCHAR CONFIG_PATH[MAX_PATH];

LPTSTR GetCurDir()
{
  DWORD length = GetCurrentDirectory(0, NULL);
  if (!length)
  {
    return NULL;
  }

  LPTSTR value = new TCHAR[length];
  GetCurrentDirectory(length, value);
  return value;
}

LPTSTR GetExeDir()
{
  TCHAR value[MAX_PATH];
  GetModuleFileName(NULL, value, MAX_PATH);

  PathRemoveFileSpec(value);
  return _tcsdup(value);
}

BOOL SetConfigPath()
{
  if (!GetModuleFileName(NULL, CONFIG_PATH, MAX_PATH))
  {
    return FALSE;
  }

  if (!PathRemoveFileSpec(CONFIG_PATH))
  {
    return FALSE;
  }

  if (!PathAppend(CONFIG_PATH, CONFIG_FILE))
  {
    return FALSE;
  }

  return TRUE;
}

UINT ReadInt(LPCTSTR key, UINT defaultValue)
{
  UINT value = GetPrivateProfileInt(CONFIG_APP, key, defaultValue, CONFIG_PATH);
  fprintf_s(stderr, "ReadInt: %s=%u\n", key, value);
  return value;
}

BOOL ReadBool(LPCTSTR key, BOOL defaultValue)
{
  TCHAR value[10];
  DWORD length = GetPrivateProfileString(CONFIG_APP, key, defaultValue ? TEXT("1") : TEXT("0"), value, _countof(value), CONFIG_PATH);
  _ftprintf_s(stderr, TEXT("ReadBool: %s=%s\n"), key, value);

  if ((length == 1 && _tcsnicmp(value, TEXT("1"), 1) == 0) ||
      (length == 4 && _tcsnicmp(value, TEXT("true"), 4) == 0) ||
      (length == 3 && _tcsnicmp(value, TEXT("yes"), 3) == 0))
  {
    return TRUE;
  }

  if ((length == 1 && _tcsnicmp(value, TEXT("0"), 1) == 0) ||
      (length == 5 && _tcsnicmp(value, TEXT("false"), 5) == 0) ||
      (length == 2 && _tcsnicmp(value, TEXT("no"), 2) == 0))
  {
    return FALSE;
  }

  return defaultValue;
}

LPTSTR ReadStr(LPCTSTR key, LPCTSTR defaultValue)
{
  DWORD size = 256;
  LPTSTR value = new TCHAR[size];

  DWORD length = GetPrivateProfileString(CONFIG_APP, key, defaultValue, value, size, CONFIG_PATH);
  _ftprintf_s(stderr, TEXT("ReadStr: %s=%s\n"), key, value);
  return value;
}

BOOL WriteInt(LPCTSTR key, UINT value)
{
  TCHAR buffer[8];
  _stprintf_s(buffer, TEXT("%u"), value);
  return WritePrivateProfileString(CONFIG_APP, key, buffer, CONFIG_PATH);
}

BOOL WriteBool(LPCTSTR key, BOOL value)
{
  return WritePrivateProfileString(CONFIG_APP, key, value ? TEXT("true") : TEXT("false"), CONFIG_PATH);
}

BOOL WriteStr(LPCTSTR key, LPCTSTR value)
{
  return WritePrivateProfileString(CONFIG_APP, key, value, CONFIG_PATH);
}

BOOL ENABLE;
INTERNET_SCHEME SCHEME;
LPWSTR HOST_NAME;
DWORD HOST_NAME_LENGTH;
INTERNET_PORT PORT;

BOOL ReadConfig()
{
  ENABLE = ReadBool(CONFIG_ENABLE_KEY, CONFIG_ENABLE_DEFAULT);
  printf_s("Enable: %s\n", ENABLE ? "true" : "false");

  BOOL https = ReadBool(CONFIG_HTTPS_KEY, CONFIG_HTTPS_DEFAULT);
  printf_s("Scheme: %s\n", https ? "https" : "http");
  SCHEME = https ? INTERNET_SCHEME_HTTPS : INTERNET_SCHEME_HTTP;

  LPTSTR host = ReadStr(CONFIG_HOST_KEY, CONFIG_HOST_DEFAULT);
  _tprintf_s(TEXT("Host: %s\n"), host);
#ifdef UNICODE
  size_t length = wcslen(host) + 1;
  HOST_NAME = new WCHAR[length];
  wcscpy_s(HOST_NAME, length, host);
#else
  int length = MultiByteToWideChar(CP_ACP, 0, host, -1, NULL, 0);
  if (!length)
  {
    delete[] host;
    return FALSE;
  }
  HOST_NAME = new WCHAR[length];
  MultiByteToWideChar(CP_ACP, 0, host, -1, HOST_NAME, length);
#endif
  HOST_NAME_LENGTH = length - 1;
  delete[] host;

  UINT port = ReadInt(CONFIG_PORT_KEY, CONFIG_PORT_DEFAULT);
  printf_s("Port: %u\n", port);
  if (port < 0 || port > 65535)
  {
    return FALSE;
  }
  PORT = port;

  return TRUE;
}

BOOL WriteConfig()
{
  WriteBool(CONFIG_ENABLE_KEY, ENABLE);
  WriteBool(CONFIG_HTTPS_KEY, SCHEME == INTERNET_SCHEME_HTTPS);

  LPTSTR host;
#ifdef UNICODE
  host = HOST_NAME;
#else
  int length = WideCharToMultiByte(CP_ACP, 0, HOST_NAME, -1, NULL, 0, NULL, NULL);
  if (!length)
  {
    return FALSE;
  }
  host = new CHAR[length];
  WideCharToMultiByte(CP_ACP, 0, HOST_NAME, -1, host, length, NULL, NULL);
  delete[] HOST_NAME;
#endif
  WriteStr(CONFIG_HOST_KEY, host);
  delete[] host;

  WriteInt(CONFIG_PORT_KEY, PORT);
  return TRUE;
}

HMODULE LoadSystemLibrary(LPCTSTR lpLibFileName)
{
  TCHAR lpBuffer[MAX_PATH];
  if (!GetSystemDirectory(lpBuffer, MAX_PATH))
  {
    return NULL;
  }

  TCHAR lpLibFilePath[MAX_PATH];
  _stprintf_s(lpLibFilePath, MAX_PATH, TEXT("%s\\%s"), lpBuffer, lpLibFileName + 5);
  return LoadLibrary(lpLibFilePath);
}

HMODULE LoadLibrary_fake(LPCTSTR lpLibFileName)
{
#ifdef _DEBUG
  if (AllocConsole())
  {
    FILE *fp;
    freopen_s(&fp, "CONOUT$", "w", stdout);
    freopen_s(&fp, "CONOUT$", "w", stderr);

    LPCTSTR cur = GetCurDir();
    if (cur)
    {
      _tprintf_s(TEXT("CUR: %s\n"), cur);
      delete[] cur;
    }

    LPCTSTR exe = GetExeDir();
    if (exe)
    {
      _tprintf_s(TEXT("EXE: %s\n"), exe);
      delete[] exe;
    }
  }
#endif

  if (SetConfigPath())
  {
    ReadConfig();
  }
  return LoadSystemLibrary(lpLibFileName);
}

#undef LoadLibrary
#define LoadLibrary LoadLibrary_fake

BOOL FreeLibrary_fake(HMODULE hLibModule)
{
  if (SetConfigPath())
  {
    WriteConfig();
  }
  return FreeLibrary(hLibModule);
}

#undef FreeLibrary
#define FreeLibrary FreeLibrary_fake

typedef BOOL(WINAPI *CrackUrl_ptr)(LPCWSTR, DWORD, DWORD, LPURL_COMPONENTSW);

BOOL CrackUrl_fake(CrackUrl_ptr crackUrl_real, LPCWSTR url, DWORD urlLength, DWORD flags, LPURL_COMPONENTSW urlComponents)
{
  if (!ENABLE)
  {
    return crackUrl_real(url, urlLength, flags, urlComponents);
  }

  if (urlComponents->dwHostNameLength <= HOST_NAME_LENGTH)
  {
    return FALSE;
  }

  if (!urlComponents->dwUrlPathLength)
  {
    return FALSE;
  }
  DWORD urlPathLength = urlComponents->dwUrlPathLength;

  if (crackUrl_real(url, urlLength, flags, urlComponents))
  {
    LPWSTR hostName;
    DWORD hostNameLength;

    if (urlComponents->dwHostNameLength == 14 && wmemcmp(urlComponents->lpszHostName, L"api.doaxvv.com", 14) == 0)
    {
      hostName = L"/api";
      hostNameLength = 4;
    }
    if (urlComponents->dwHostNameLength == 25 && wmemcmp(urlComponents->lpszHostName, L"api.doax-venusvacation.jp", 25) == 0)
    {
      hostName = L"/api";
      hostNameLength = 4;
    }
    else if (urlComponents->dwHostNameLength == 16 && wmemcmp(urlComponents->lpszHostName, L"api01.doaxvv.com", 16) == 0)
    {
      hostName = L"/api01";
      hostNameLength = 6;
    }
    else if (urlComponents->dwHostNameLength == 27 && wmemcmp(urlComponents->lpszHostName, L"api01.doax-venusvacation.jp", 27) == 0)
    {
      hostName = L"/api01";
      hostNameLength = 6;
    }
    else if (urlComponents->dwHostNameLength == 15 && wmemcmp(urlComponents->lpszHostName, L"game.doaxvv.com", 15) == 0)
    {
      hostName = L"/game";
      hostNameLength = 5;
    }
    else if (urlComponents->dwHostNameLength == 27 && wmemcmp(urlComponents->lpszHostName, L"cdn01.doax-venusvacation.jp", 27) == 0)
    {
      hostName = L"/cdn01";
      hostNameLength = 6;
    }
    else if (urlComponents->dwHostNameLength == 21 && wmemcmp(urlComponents->lpszHostName, L"doax-venusvacation.jp", 21) == 0)
    {
      hostName = L"/www";
      hostNameLength = 4;
    }
    else
    {
      return FALSE;
    }

    urlComponents->nScheme = SCHEME;
    urlComponents->lpszHostName = HOST_NAME;
    urlComponents->dwHostNameLength = HOST_NAME_LENGTH;
    urlComponents->nPort = PORT;

    if (wmemmove_s(urlComponents->lpszUrlPath + hostNameLength, urlPathLength - hostNameLength, urlComponents->lpszUrlPath, urlComponents->dwUrlPathLength + 1))
    {
      return FALSE;
    }
    if (wmemcpy_s(urlComponents->lpszUrlPath, urlPathLength, hostName, hostNameLength))
    {
      return FALSE;
    }
    urlComponents->dwUrlPathLength += hostNameLength;

    return TRUE;
  }

  return FALSE;
}
