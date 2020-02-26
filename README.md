# Tietokantasovellus

# Projektin kuvaus
Ideana tehdä ruokatilaus-sovellus ravintolalle. Ravintolalla on annoksia. Asiakas voi koostaa annoksista tilauksen ja lähettää sen raflalle. Ravintolan omistaja voi luoda ravintoloita, muokata ravintolan tietoja, nähdä tilaukset, lisätä annoksia listalle sekä muokata ja poistaa listalla olevia annoksia.
   
# Dokumentaatio   
[Tietokantakaavio](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/tietokantakaavio.jpg)       
[Työaikakirjanpito](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.MD)     
[Käyttötapaukset + Technical Tasks](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.MD)   
   
# Käytettävissä   
[Heroku](https://roni-tietokantasovellus.herokuapp.com)   
   
# Käyttöohjeet   
## Asiakas:    
   
Root sivulla [https://roni-tietokantasovellus.herokuapp.com](https://roni-tietokantasovellus.herokuapp.com) asiakas voi nähdä listan ravintoloista, joilla on ruokalistalla annoksia. Asiakas voi siirtyä tekemään tilauksen painamalla Visit-nappulaa haluamansa ravintolan kohdalla.   
  
Ravintoloiden sivulla (root/ravintolanId) asiakas voi tehdä tilauksia. Painele haluamiesi tuotteiden kohdalla Add To Order. Kun tilaus on valmis, siirry lähettämään tilaus painamalla Move To Checkout, täytä yhteystiedot aukeavaan lomakkeeseen ja paina Send Order. Saat vastauksena kuitin, jossa näkyy tilauksen tiedot. Takaisin ravintolalistaan pääsee yläreunassa olevasta nappulasta.    
  
## Ravintolan Omistaja:  
    
Kirjaudu sisään tai luo uusi ravintola osoitteessa [https://roni-tietokantasovellus.herokuapp.com/login](https://roni-tietokantasovellus.herokuapp.com/login).  
Esimerkkitunnukset:   
Käyttäjä: Maija    
Salasana: Maija         
  
Huomaa, että uudelle ravintolalle pitää lisätä annoksia ruokalistalle, ennenkuin se näkyy asiakasnäkymän listauksessa.    
Huomaa, että salasanoja ei encryptata millään tavalla lähettäessä tai db:seen tallennettaessa, niin älä käytä testatessa mitään aitoa salasanaa.   
Sivusto siirtää käyttäjän automaattisesti käyttäjään liitetyn ravintolan hallinnasta vastaavalle sivulle.    
Menupalkista voi valita, haluaako katsoa sisään tulleita tilauksia (Manage orders), muokata ravintolan ruokalistaa (Manage Menu Items) tai muokata ravintolan tietoja/ poistaa ravintolan (Manage Restaurant Info).   
Tilauksia voi vain selata, ruokalistan annoksia lisätä, poistaa ja päivittää. Poistaminen ei oikeasti poista annosta, vaan ainoastaan tekee siitä inaktiivisen, jotta vanhojen tilausten annokset näkyvät oikein. Inaktiivisia annoksia ei voi selata mistään, mutta ne näkyvät vanhoissa tilauksissa normaalisti.   
Ravintolan tietoja voi muuttaa tai ravintolan voi poistaa (myös käyttäjä poistuu tämän pyynnön tehdessä.)   
