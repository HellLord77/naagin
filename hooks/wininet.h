#include <wininet.h>

#include "common.h"

#define INTERNETOPENW
FAKE(HINTERNET, WINAPI, InternetOpenW, LPCWSTR lpszAgent, DWORD dwAccessType, LPCWSTR lpszProxy, LPCWSTR lpszProxyBypass, DWORD dwFlags)
{
    dwAccessType = INTERNET_OPEN_TYPE_PROXY;
    lpszProxy = L"http://localhost:8080";
    return InternetOpenW_real(lpszAgent, dwAccessType, lpszProxy, lpszProxyBypass, dwFlags);
}
