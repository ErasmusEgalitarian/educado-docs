# SMS Provider Research Comparison

## Introduction
This report documents the research of SMS integrations for **Educado**. Three SMS providers are researched. For each provider the price per 1000 SMS messages as well as pros and cons for integrating the provider are described.

- [PDF](../../database/pdf/sms-provider.pdf)

---

## LabsMobile
LabsMobile offers SMS APIs for different purposes. Of most interest for Educado is the **OTP API**.  

**Cost per 1000 SMS:**
- 13.15 € in Brazil  
- 45.4 € in Denmark  
- 75.3 € in The Netherlands  

**Other conditions:**
- Free verification of codes  
- Minimum purchase of 10 USD / 9 EUR (packs last 18 months)  
- Limited free trial  

**Pros:**
- Straightforward API for OTP services  
- Endpoints: `sendCode`, `resendCode`, `validateCode`, `checkCode`  
- Easy management of verification workflows  
- More APIs available if customization needed  
- Standard HTTP requests (no npm package required)  
- Clear documentation with Node.js examples  

[LabsMobile OTP API](https://www.labsmobile.com/en/sms-api/api-versions/sms-otp)

---

## Twilio

### SMS
**Cost per 1000 SMS:**
- 50 € in Denmark or Brazil  
- 145 € in The Netherlands  

### WhatsApp
Twilio also offers verification via **WhatsApp**, widely used in Brazil.  

**Cost per 1000 messages:**
- $89 (Verify costs $50 + WhatsApp fee $39), regardless of country  

**Cons:**
- Requires npm package (`twilio`)  
- Documentation less clear than others  

[Twilio Verify Docs](https://www.twilio.com/docs/verify)

---

## Infobip
Infobip offers full SMS coverage in Brazil with fast number leasing and free trial.  

**Cost per 1000 SMS:**
- €25 in Brazil  
- €38 in Denmark  
- €80 in The Netherlands  

**Notes:**
- Possible hidden fees (choice of SMS provider may increase costs)  
- OTP available only as **2FA**, making integration more complex  
- Requires installing SDK npm package  

**Cons:**
- Larger bundle size, potential compatibility issues  
- More convoluted OTP setup  

[Infobip SDK Docs](https://www.infobip.com/docs/sdk?page=1)

---

## Recommendation – LabsMobile
LabsMobile provides the **most cost-effective and straightforward option** for Educado’s OTP requirements.  
- Lower pricing across regions compared to Twilio and Infobip  
- Clean, well-documented API for code verification workflows  
- No extra SDKs required → reduced integration complexity  
- Avoids compatibility issues on older devices  

---

## Comparison Table

| Provider       | Price/1000 (Brazil) | Price/1000 (Denmark) | Price/1000 (Netherlands) | Pros                                                                                  | Cons                                                                                           | Recommendation |
|----------------|---------------------|-----------------------|---------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------|
| **Twilio SMS** | €50                 | €49.59                | €145.39                   | Global coverage, integrations, 1000 free SMS (US)                                      | High prices, hard-to-read docs, failed msg fee $0.001                                          | Not recommended |
| **Twilio WhatsApp** | $89 flat rate     | $89 flat rate          | $89 flat rate             | Popular in Brazil, supports Verify API                                                 | Requires WhatsApp account, Verify very expensive, needs npm package                            | Recommended only if WhatsApp is preferred |
| **LabsMobile** | €13.15              | €45.4                 | €75.3                     | Cheap, free trial, no SDK needed, clear docs, easy OTP API with multiple endpoints     | Minimum purchase 10 USD / 9 EUR (packs last 18 months)                                         | **Best option** |
| **Infobip**    | €25                 | €38                   | €80                       | Full Brazil coverage, free trial, OTP with built-in pin verification                   | Requires proprietary SDKs, OTP only via 2FA, possible hidden fees, heavier integration process | Not recommended |

---

### References
- [LabsMobile Pricing](https://www.labsmobile.com/en/purchase-sms-price)  
- [Twilio Verify Quickstart](https://www.twilio.com/docs/verify/quickstarts/node-express)  
- [Twilio WhatsApp Docs](https://www.twilio.com/docs/verify/whatsapp)  
- [Twilio WhatsApp Pricing](https://www.twilio.com/en-us/whatsapp/pricing)  
- [Infobip SDK Docs](https://www.infobip.com/docs/sdk?page=1)  
