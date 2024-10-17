# Lab 2

## Threat Model
![Threat-model](image-1.png)

**Vragen**
- Zou je op basis van het threat moden "encryption at rest" aanraden?
    - Ja, de gegevens die een cloud admin of intruder kan stelen kunnen heel kwetsbaar zijn.

- Homomorphic encryption aanraden? 
    - Het zou nuttig kunnen zijn maar in mijn model is het probleem vooral bij het onbevoegde toegang tot gevoelige gegevens.

- E2EE en hoe past het in mijn model?
    - E2EE is wanneer berichten worden versleuteld op het moment dat ze door de afzender worden verzonden en pas ontsleuteld door de ontvanger. Zelfs de servers ziet de inhoud niet.
    - Het zou bij mij helpen tegen mensen die gegevens willen stelen, want de gegevens zijn altijd versleuteld.


## Homomorphic encryption
Deze code (in homomorphic.py) maakt gebruik van de Tenseal libraries om veilige berekeningen uit te voeren met behulp van homomorphic encryptie. Hier is een korte uitleg van de belangrijkste onderdelen:

#### Function `setup_context()`
- **Parameters**:
  - `poly_modulus_degree = 2048`: Dit bepaalt de graad van het poly, dit heeft invloeg op de veiligheid en prestaties.
  - `plain_modulus = 1032193`: Dit is de modulus voor de plaintext.

#### Hoofdcode
1. **Context Aanmaken**:
   - `context = setup_context()`: De encryptie context wordt ingestelt.
2. **Getallen Definieren**:
   - `number1 = 75` en `number2 = 326`: 2 getallen die zullen worden opgeteld.
3. **Encryptie**:
   - `enc_number1` en `enc_number2` zijn de versleutelde versies van `number1` en `number2` die worden verkregen met de `bfv_scalar` function van Tenseal.
4. **Optelling**:
   - `enc_result = enc_number1 + enc_number2`: De geencrpyteerde getallen worden opgeteld.
5. **Decryptie**:
   - `result = enc_result.decrypt()`: Het resultaat van de optelling wordt gedecrypt.
#### Resultaat
De code toont de som van de twee getallen (75 en 326) na decryptie van de encrypteerde optelling.

## Shamir Secrect Sharing
Ik heb de sslib libray gebruikt in python dit ging zeer vlot. Ik moest op Linux zitten om dit werkende te krijgen
Het enigste dat mij in de war bracht was de lector die sprak over een cipher text. Ik zal dit zeker navragen in de les!

Share 1: '1-mN1BhzYKdrBA6Ix3SARc1xHlkIgQHimj' <br>
Link naar paste.ee met share 2 erop: https://paste.ee/p/m9E3K

## Post Quantum
Ik heb een post quantum techinque proberen te gebruiken, namelijk Kyber. Dit bleek echter super moeilijk dus ik heb besloten om een **low-level** post quantum encryptie na te boosten. Ik leg eerst uit waarom dit een low-level versie is van post quantum.
- **Asymmetrische Cryptografie**: De techniek (nacl) maakt gebruik van asymmetrische cryptografie, wat betekent dat een paar sleutels (privé en publiek) worden gebruikt om berichten te encrypteren en te decrypteren. Kyber is een post quantum cryptografische techniek die ook asymmetrische cryptografie gebruikt.
- **Verschillen in Veiligheid**: Hoewel de code een basic voorbeeld is van encryptie, biedt het niet dezelfde beveiliging als moderne post quantum algoritme zoals Kyber. Kyber is gebaseerd op lattice based cryptografie, wat een hogere weerstand biedt tegen quantum aanvallen.

In mijn script ```low-level-kyber.py``` probeer ik dit na te boosten. Ik leg kort de code uit hieronder.
1. Genereren van Sleutels: ```private_key = PrivateKey.generate()```
2. Creeren van een Box: ```box = Box(private_key, public_key)```
3. Bericht Encrypteren: ```encrypted_message = box.encrypt(message)```
4. Afdrukken van de resultaten.

## Moeilijkheden
- Post Quantum werkende krijgen (ik heb zelfs mijn WSL kunnen kapot krijgen).
- Uitvinden dat de Shamir library enkel op Linux werkte.
- Verwarring over hoe het verslag te schrijven - hopelijk is hij goed :)

