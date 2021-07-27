import requests
import json

apiURL="https://api.exchangerate.host/latest?base="

while True:

    status=input("1) Döviz bozdurma\n2) Çıkış\nSeçiminiz: ")
    
    if status=="1":    
        
        try:
            print("\nLütfen aşağıda belirtilen anahtar kelimelerle işlem yapınız!\n")
            print("Döviz değişimi için anahtar kelimeler: ")
            print('\nAED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD',
            'BDT', 'BGN', 'BHD', 'BIF', '\nBMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 
            'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', '\nCNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 
            'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', '\nFKP', 'GBP', 'GEL', 
            'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 
            '\nILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 
            'KMF', 'KPW', 'KRW', '\nKWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 
            'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', '\nMRO', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 
            'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', '\nPEN', 'PGK', 'PHP', 'PKR', 
            'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', '\nSGD', 
            'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT',
            'TND', 'TOP', '\nTRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND',
            'VUV', 'WST', 'XAF', 'XAG', 'XAU', '\nXCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 
            'ZMW', 'ZWL',"\n",sep="   ")
            bozulan_doviz=input("Bozulan döviz türü: ")
            alinan_doviz=input("Alınan döviz türü: ")
            miktar=float(input(f"Kaç adet {bozulan_doviz} bozdurmak istiyorsunuz: "))
            result=requests.get(apiURL+bozulan_doviz)
            result=json.loads(result.text)
            print(f'\n{result["date"]}\n\n1 {bozulan_doviz} = {result["rates"][alinan_doviz]} {alinan_doviz}')
            print(f'{miktar} {bozulan_doviz} = {miktar*result["rates"][alinan_doviz]} {alinan_doviz} \n')
        
        except Exception as e :
            print(e)
    
    elif status=="2":
        break
    
    else:
        print("Lütfen geçerli bir işlem yapınız")