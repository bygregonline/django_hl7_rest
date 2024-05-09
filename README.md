# django_hl7_rest
 <h3> HL7 Miroservice </h3>
---

 ![Image of HL7 logo](https://cql.hl7.org/dist/hl7-logo.png)

---

steps

```

gh repo clone bygregonline/django_hl7_rest
cd django_hl7_rest
docker build -t your_name/hl7:latest .
docker run -d -p 8000:8000 your_name/hl7:latest

 curl http://localhost:8000/hl7\?data\=RXA%7C0%7C1%7C20141215%7C20141115%7C141%5Einfluenza%2C+SEASONAL+36%5ECVX%5E90658%5EInfluenza+Split%5ECPT%7C999%7C%7C%7CC0%5EHISTORIC\&format\=json |jq



{
  "version": "2.5",
  "field": "RXA",
  "data": {
    "GIVE_SUB_ID_COUNTER": "0",
    "ADMINISTRATION_SUB_ID_COUNTER": "1",
    "DATE_TIME_START_OF_ADMINISTRATION": "20141215",
    "DATE_TIME_END_OF_ADMINISTRATION": "20141115",
    "ADMINISTERED_CODE": "141 influenza, SEASONAL 36 CVX 90658 Influenza Split CPT",
    "ADMINISTERED_AMOUNT": "999",
    "ADMINISTRATION_NOTES": "C0 HISTORIC"
  }
}


```



