# Tietokantasovellus

# Projektin kuvaus
Ideana tehdä ruokatilaus-sovellus ravintolalle. Ravintolalla on annoksia. Asiakas voi koostaa annoksista tilauksen. Tarkemmat tiedot tämän toteuttamiseen käytetyistä eri luokista ja niiden suhteista löytyy dokumentaation tietokantakaaviosta. Tällä hetkellä ideana on vain yksi ravintola, joskin ajattelin luoda ravintoloille oman taulun, jotta ohjelma olisi laajennettavissa myöhemmin.
  
# Dokumentaatio
[Tietokantakaavio](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/tietokantakaavio.jpg)     
[Työaikakirjanpito](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.MD)  
[Käyttötapaukset + Technical Tasks](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.MD)

# Käytettävissä
[Heroku](https://roni-tietokantasovellus.herokuapp.com)

# Käyttöohjeet
Asiakas:

Root sivulla [https://roni-tietokantasovellus.herokuapp.com](https://roni-tietokantasovellus.herokuapp.com) asiakas voi tehdä tilauksia. Painele haluamiesi tuotteiden kohdalla Add To Order. Kun tilaus on valmis, siirry lähettämään tilaus painamalla Move To Checkout, täytä yhteystiedot aukeavaan lomakkeeseen ja paina Send Order. Saat vastauksena kuitin, jossa näkyy tilauksen tiedot.  
  
  Ravintolan Omistaja:  
  
Kirjaudu sisään osoitteessa [https://roni-tietokantasovellus.herokuapp.com/auth/login](https://roni-tietokantasovellus.herokuapp.com/auth/login) tunnuksilla Käyttäjä: Admin , Salasana: Password. Sivusto siirtää käyttäjän automaattisesti käyttäjään liitetyn ravintolan tilaustenhallinnasta vastaavalle sivulle. Sivulla näkyy aiemmat tilaukset. Uudet tilaukset tulevat näkyviin kunhan päivität sivua. Kellonajat ovat atm. 2h väärässä, johtuen tietokannan default aikavyöhykkeestä.
