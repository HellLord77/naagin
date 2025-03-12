#include <winhttp.h>

#include "common.h"

#ifndef _DEBUG
#include <wchar.h>

#define WINHTTPCRACKURL
FAKE(BOOL, WINAPI, WinHttpCrackUrl, LPCWSTR pwszUrl, DWORD dwUrlLength, DWORD dwFlags, LPURL_COMPONENTS lpUrlComponents)
{
    if (lpUrlComponents->dwHostNameLength < 9)
    {
        SetLastError(ERROR_NOT_ENOUGH_MEMORY);
        return FALSE;
    }

    if (!lpUrlComponents->dwUrlPathLength)
    {
        SetLastError(ERROR_INVALID_PARAMETER);
        return FALSE;
    }
    DWORD lpszUrlPathLengthMax = lpUrlComponents->dwUrlPathLength;

    if (WinHttpCrackUrl_real(pwszUrl, dwUrlLength, dwFlags, lpUrlComponents))
    {
        LPWSTR lpszHostName;
        DWORD dwHostNameLength;
        if (lpUrlComponents->dwHostNameLength == 14 && !wmemcmp(lpUrlComponents->lpszHostName, L"api.doaxvv.com", 14))
        {
            lpszHostName = L"/api";
            dwHostNameLength = 4;
        }
        else if (lpUrlComponents->dwHostNameLength == 15 && !wmemcmp(lpUrlComponents->lpszHostName, L"game.doaxvv.com", 15))
        {
            lpszHostName = L"/game";
            dwHostNameLength = 5;
        }
        else if (lpUrlComponents->dwHostNameLength == 16 && !wmemcmp(lpUrlComponents->lpszHostName, L"api01.doaxvv.com", 16))
        {
            lpszHostName = L"/api01";
            dwHostNameLength = 6;
        }
        else
        {
            SetLastError(ERROR_WINHTTP_INVALID_URL);
            return FALSE;
        }

        lpUrlComponents->nScheme = INTERNET_SCHEME_HTTP;
        lpUrlComponents->lpszHostName = L"localhost";
        lpUrlComponents->dwHostNameLength = 9;
        lpUrlComponents->nPort = 8000;

        if (wmemmove_s(lpUrlComponents->lpszUrlPath + dwHostNameLength, lpszUrlPathLengthMax - dwHostNameLength, lpUrlComponents->lpszUrlPath, lpUrlComponents->dwUrlPathLength))
        {
            SetLastError(ERROR_NOT_ENOUGH_MEMORY);
            return FALSE;
        }
        if (wmemcpy_s(lpUrlComponents->lpszUrlPath, lpszUrlPathLengthMax, lpszHostName, dwHostNameLength))
        {
            SetLastError(ERROR_WINHTTP_INTERNAL_ERROR);
            return FALSE;
        }

        return TRUE;
    }

    return FALSE;
}
#else
#define WINHTTPOPEN
FAKE(HINTERNET, WINAPI, WinHttpOpen, LPCWSTR pszAgentW, DWORD dwAccessType, LPCWSTR pszProxyW, LPCWSTR pszProxyBypassW, DWORD dwFlags)
{
    dwAccessType = WINHTTP_ACCESS_TYPE_NAMED_PROXY;
    pszProxyW = L"http://localhost:8080";
    return WinHttpOpen_real(pszAgentW, dwAccessType, pszProxyW, pszProxyBypassW, dwFlags);
}
#endif
