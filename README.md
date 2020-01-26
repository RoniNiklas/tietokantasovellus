# Tietokantasovellus

# Projektin kuvaus
Ideana tehdä ruokatilaus-sovellus ravintolalle. Ravintolalla on annoksia. Asiakas voi koostaa annoksista tilauksen. Tarkemmat tiedot tämän toteuttamiseen käytetyistä eri luokista ja niiden suhteista löytyy dokumentaation tietokantakaaviosta. Tällä hetkellä ideana on vain yksi ravintola, joskin ajattelin luoda ravintoloille oman taulun, jotta ohjelma olisi laajennettavissa myöhemmin.

# Käyttötapaukset

User Story # 1 Completed  
As a customer, I want to see what items are available, so that I can decide what I want to order  
User Story # 2 Completed  
As a customer, I want to make an order, so that I can get food  
User Story # 3 Completed  
As a customer, I want to save my info, so that I an place an order faster the next time I use the app  
User Story # 4 Completed
As a restaurant owner, I want to see the orders that have been placed, so that I can send the customer food  
  
--- Potential future user stories, not prioritized     
As a customer, I want to save an order template, so that I can place an order faster the next time I use the app  
As a customer, I want to see my old orders, for whatever reason  
As a restaurant owner, I want to add menu items, so that users can order new menu items  
As a restaurant owner, I want to delete menu items, so that I can stop serving items that do not create profit  
As a restaurant owner, I want to create a new restaurant on the app  
  
# Dokumentaatio
[Tietokantakaavio](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/tietokantakaavio.jpg)     
[Työaikakirjanpito](https://github.com/RoniNiklas/tietokantasovellus/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito)  

# Käytettävissä
[Heroku](https://roni-tietokantasovellus.herokuapp.com)

# Käyttöohjeet
Asiakas:

Root sivulla [https://roni-tietokantasovellus.herokuapp.com](https://roni-tietokantasovellus.herokuapp.com) asiakas voi tehdä tilauksia. Painele haluamiesi tuotteiden kohdalla Add To Order. Kun tilaus on valmis, siirry lähettämään tilaus painamalla Move To Checkout, täytä yhteystiedot aukeavaan lomakkeeseen ja paina Send Order. Saat vastauksena kuitin, jossa näkyy tilauksen tiedot.  
  
  Ravintolan Omistaja
Kirjaudu sisään osoitteessa [https://roni-tietokantasovellus.herokuapp.com/auth/login](https://roni-tietokantasovellus.herokuapp.com/auth/login). Sivusto siirtää käyttäjän automaattisesti käyttäjään liitetyn ravintolan tilaustenhallinnasta vastaavalle sivulle. Sivulla näkyy aiemmat tilaukset. Uudet tilaukset tulevat näkyviin kunhan päivität sivua.
