#include <winhttp.h>

#include "common.h"

#define WINHTTPOPEN
FAKE(HINTERNET, WINAPI, WinHttpOpen, LPCWSTR pszAgentW, DWORD dwAccessType, LPCWSTR pszProxyW, LPCWSTR pszProxyBypassW, DWORD dwFlags)
{
    dwAccessType = WINHTTP_ACCESS_TYPE_NAMED_PROXY;
    pszProxyW = L"http://localhost:8080";
    return WinHttpOpen_real(pszAgentW, dwAccessType, pszProxyW, pszProxyBypassW, dwFlags);
}
