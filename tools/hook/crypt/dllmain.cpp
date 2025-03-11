// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"

static BOOL(WINAPI *PointerCryptExportKey)(HCRYPTKEY hKey, HCRYPTKEY hExpKey, DWORD dwBlobType, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen) = CryptExportKey;
static BOOL(WINAPI *PointerCryptImportKey)(HCRYPTPROV hProv, CONST BYTE *pbData, DWORD dwDataLen, HCRYPTKEY hPubKey, DWORD dwFlags, HCRYPTKEY *phKey) = CryptImportKey;
static BOOL(WINAPI *PointerCryptEncrypt)(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen, DWORD dwBufLen) = CryptEncrypt;
static BOOL(WINAPI *PointerCryptDecrypt)(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen) = CryptDecrypt;
static BOOL(WINAPI *PointerCryptHashData)(HCRYPTHASH hHash, CONST BYTE *pbData, DWORD dwDataLen, DWORD dwFlags) = CryptHashData;
static BOOL(WINAPI *PointerCryptStringToBinaryA)(LPCSTR pszString, DWORD cchString, DWORD dwFlags, BYTE *pbBinary, DWORD *pcbBinary, DWORD *pdwSkip, DWORD *pdwFlags) = CryptStringToBinaryA;

VOID PrintHex(CONST BYTE *pbData, DWORD dwDataLen)
{
	BOOL bDataLong = dwDataLen > 1024;
	if (bDataLong)
	{
		dwDataLen = 1024;
	}

	for (DWORD i = 0; i < dwDataLen; i++)
	{
		printf("%02X", pbData[i]);
	}

	if (bDataLong)
	{
		printf("...");
	}
}

BOOL WINAPI DetourCryptExportKey(HCRYPTKEY hKey, HCRYPTKEY hExpKey, DWORD dwBlobType, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen)
{
	std::cout << "CryptExportKey called" << std::endl;

	if (*pdwDataLen == 0)
	{
		if (PointerCryptExportKey(hKey, NULL, PLAINTEXTKEYBLOB, 0, nullptr, pdwDataLen))
		{
			BYTE *DetourPbData = new BYTE[*pdwDataLen];
			if (DetourPbData)
			{
				if (PointerCryptExportKey(hKey, NULL, PLAINTEXTKEYBLOB, 0, DetourPbData, pdwDataLen))
				{
					std::cout << "\tDetourData: ";
					PrintHex(DetourPbData, *pdwDataLen);
					std::cout << std::endl;
				}
				else
				{
					std::cout << "CryptExportKey failed" << std::endl;
				}
				delete[] DetourPbData;
			}
			*pdwDataLen = 0;
		}
		else
		{
			std::cout << "CryptExportKey0 failed" << std::endl;
		}
	}

	if (PointerCryptExportKey(hKey, hExpKey, dwBlobType, dwFlags, pbData, pdwDataLen))
	{
		if (pbData && *pdwDataLen > 0)
		{
			std::cout << "\tExported: ";
			PrintHex(pbData, *pdwDataLen);
			std::cout << std::endl;
		}
		return TRUE;
	}

	return FALSE;
}

BOOL WINAPI DetourCryptImportKey(HCRYPTPROV hProv, CONST BYTE *pbData, DWORD dwDataLen, HCRYPTKEY hPubKey, DWORD dwFlags, HCRYPTKEY *phKey)
{
	std::cout << "CryptImportKey called" << std::endl;

	if (pbData && dwDataLen > 0)
	{
		std::cout << "\tData: ";
		PrintHex(pbData, dwDataLen);
		std::cout << std::endl;
	}

	return PointerCryptImportKey(hProv, pbData, dwDataLen, hPubKey, dwFlags, phKey);
}

BOOL WINAPI DetourCryptEncrypt(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen, DWORD dwBufLen)
{
	std::cout << "CryptEncrypt called" << std::endl;

	if (pbData && *pdwDataLen > 0)
	{
		std::cout << "\tData: ";
		PrintHex(pbData, *pdwDataLen);
		std::cout << std::endl;
	}

	if (PointerCryptEncrypt(hKey, hHash, Final, dwFlags, pbData, pdwDataLen, dwBufLen))
	{
		std::cout << "\tEncrypted: ";
		PrintHex(pbData, *pdwDataLen);
		std::cout << std::endl;
		return TRUE;
	}

	return FALSE;
}

BOOL WINAPI DetourCryptDecrypt(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE *pbData, DWORD *pdwDataLen)
{
	std::cout << "CryptDecrypt called" << std::endl;

	if (pbData && *pdwDataLen > 0)
	{
		std::cout << "\tData: ";
		PrintHex(pbData, *pdwDataLen);
		std::cout << std::endl;
	}

	if (PointerCryptDecrypt(hKey, hHash, Final, dwFlags, pbData, pdwDataLen))
	{
		std::cout << "\tDecrypted: ";
		PrintHex(pbData, *pdwDataLen);
		std::cout << std::endl;
		return TRUE;
	}

	return FALSE;
}

BOOL WINAPI DetourCryptHashData(HCRYPTHASH hHash, CONST BYTE *pbData, DWORD dwDataLen, DWORD dwFlags)
{
	std::cout << "CryptHashData called" << std::endl;

	if (pbData && dwDataLen > 0)
	{
		std::cout << "\tData: ";
		PrintHex(pbData, dwDataLen);
		std::cout << std::endl;
	}

	return PointerCryptHashData(hHash, pbData, dwDataLen, dwFlags);
}

BOOL WINAPI DetourCryptStringToBinaryA(LPCSTR pszString, DWORD cchString, DWORD dwFlags, BYTE *pbBinary, DWORD *pcbBinary, DWORD *pdwSkip, DWORD *pdwFlags)
{
	std::cout << "CryptStringToBinaryA called" << std::endl;

	if (cchString == 0)
	{
		std::cout << "\tString: " << pszString << std::endl;
	}
	else
	{
		std::cout << "\tString: ";
		std::cout.write(pszString, cchString);
		std::cout << std::endl;
	}

	if (PointerCryptStringToBinaryA(pszString, cchString, dwFlags, pbBinary, pcbBinary, pdwSkip, pdwFlags))
	{
		if (pbBinary && *pcbBinary > 0)
		{
			std::cout << "\tBinary: ";
			PrintHex(pbBinary, *pcbBinary);
			std::cout << std::endl;
		}
		return TRUE;
	}

	return FALSE;
}

VOID NewConsole()
{
	FILE *file;

	if (AllocConsole())
	{
		freopen_s(&file, "CONOUT$", "w", stdout);
		freopen_s(&file, "CONOUT$", "w", stderr);
		freopen_s(&file, "CONIN$", "r", stdin);
	}
}

VOID InstallHook()
{
	DetourTransactionBegin();
	DetourUpdateThread(GetCurrentThread());

	DetourAttach(&(PVOID &)PointerCryptExportKey, DetourCryptExportKey);
	DetourAttach(&(PVOID &)PointerCryptImportKey, DetourCryptImportKey);
	DetourAttach(&(PVOID &)PointerCryptEncrypt, DetourCryptEncrypt);
	DetourAttach(&(PVOID &)PointerCryptDecrypt, DetourCryptDecrypt);
	DetourAttach(&(PVOID &)PointerCryptHashData, DetourCryptHashData);
	DetourAttach(&(PVOID &)PointerCryptStringToBinaryA, DetourCryptStringToBinaryA);

	DetourTransactionCommit();
}

VOID RemoveHook()
{
	DetourTransactionBegin();
	DetourUpdateThread(GetCurrentThread());

	DetourDetach(&(PVOID &)PointerCryptExportKey, DetourCryptExportKey);
	DetourDetach(&(PVOID &)PointerCryptImportKey, DetourCryptImportKey);
	DetourDetach(&(PVOID &)PointerCryptEncrypt, DetourCryptEncrypt);
	DetourDetach(&(PVOID &)PointerCryptDecrypt, DetourCryptDecrypt);
	DetourDetach(&(PVOID &)PointerCryptHashData, DetourCryptHashData);
	DetourDetach(&(PVOID &)PointerCryptStringToBinaryA, DetourCryptStringToBinaryA);

	DetourTransactionCommit();
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
	if (DetourIsHelperProcess())
	{
		return TRUE;
	}

	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		NewConsole();
		DetourRestoreAfterWith();
		InstallHook();
		break;
	case DLL_PROCESS_DETACH:
		RemoveHook();
		FreeConsole();
		break;
	}
	return TRUE;
}
