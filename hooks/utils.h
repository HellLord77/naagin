#pragma once

#include <windows.h>
#include <tchar.h>
#include <wchar.h>

#include "hook_macro.h"

#define CONFIG_FILE TEXT("./config.ini")
#define CONFIG_APP TEXT("naagin")

#define CONFIG_ENABLE_KEY TEXT("enable")
#define CONFIG_HTTPS_KEY TEXT("https")
#define CONFIG_HOST_KEY TEXT("host")
#define CONFIG_PORT_KEY TEXT("port")

#define CONFIG_ENABLE_DEFAULT TRUE
#define CONFIG_HTTPS_DEFAULT FALSE
#define CONFIG_HOST_DEFAULT TEXT("localhost")
#define CONFIG_PORT_DEFAULT 8000

UINT ReadInt(LPCTSTR key, UINT defaultValue)
{
    return GetPrivateProfileInt(CONFIG_APP, key, defaultValue, CONFIG_FILE);
}

BOOL ReadBool(LPCTSTR key, BOOL defaultValue)
{
    TCHAR value[8];
    DWORD length = GetPrivateProfileString(CONFIG_APP, key, defaultValue ? TEXT("1") : TEXT("0"), value, sizeof(value), CONFIG_FILE);

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

    GetPrivateProfileString(CONFIG_APP, key, defaultValue, value, size, CONFIG_FILE);
    return value;
}

BOOL WriteInt(LPCTSTR key, UINT value)
{
    TCHAR buffer[8];
    _stprintf_s(buffer, TEXT("%u"), value);
    return WritePrivateProfileString(CONFIG_APP, key, buffer, CONFIG_FILE);
}

BOOL WriteBool(LPCTSTR key, BOOL value)
{
    return WritePrivateProfileString(CONFIG_APP, key, value ? TEXT("true") : TEXT("false"), CONFIG_FILE);
}

BOOL WriteStr(LPCTSTR key, LPCTSTR value)
{
    return WritePrivateProfileString(CONFIG_APP, key, value, CONFIG_FILE);
}

BOOL ENABLE;
INTERNET_SCHEME SCHEME;
LPWSTR HOST_NAME;
DWORD HOST_NAME_LENGTH;
INTERNET_PORT PORT;

BOOL ReadConfig()
{
    ENABLE = ReadBool(CONFIG_ENABLE_KEY, CONFIG_ENABLE_DEFAULT);

    BOOL https = ReadBool(CONFIG_HTTPS_KEY, CONFIG_HTTPS_DEFAULT);
    SCHEME = https ? INTERNET_SCHEME_HTTPS : INTERNET_SCHEME_HTTP;

    LPTSTR host = ReadStr(CONFIG_HOST_KEY, CONFIG_HOST_DEFAULT);
#ifdef UNICODE
    HOST_NAME = host;
    int length = wcslen(host);
#else
    int length = MultiByteToWideChar(CP_ACP, 0, host, -1, NULL, 0);
    if (!length)
    {
        return FALSE;
    }
    HOST_NAME = new WCHAR[length];
    MultiByteToWideChar(CP_ACP, 0, host, -1, HOST_NAME, length);
    delete[] host;
#endif
    HOST_NAME_LENGTH = length - 1;

    UINT port = ReadInt(CONFIG_PORT_KEY, CONFIG_PORT_DEFAULT);
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
    ReadConfig();
    return LoadSystemLibrary(lpLibFileName);
}

#undef LoadLibrary
#define LoadLibrary LoadLibrary_fake

BOOL FreeLibrary_fake(HMODULE hLibModule)
{
    WriteConfig();
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
