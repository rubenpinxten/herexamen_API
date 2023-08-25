<div align="center" id="readme-top">

<h1 align="center">Herexamenproject voor API Development</h1>
<p align="center">
    Gemaakt door Ruben Pinxten
    <br />
    <a href="https://github.com/rubenpinxten/herexamen_API/"><strong>Bekijk de bestanden »</strong></a>
    <br />
    <br />
    <a href="https://herexamenopdrachapiruben.netlify.app/">Front-end website</a>
    ·
    <a href="https://system-service-rubenpinxten.cloud.okteto.net/docs">API docs website</a>
  </p>
</div>
<!-- Inhoudstafel-->
<details>
  <summary>Inhoudstafel</summary>
    <ol>
      <li>
        <a href="">Gebouwd met</a>
      </li>
      <li>
        <a href="">Over dit project</a>
        <ul>
          <li>
            <a href="">Front-end API</a>
            <ul>
              <li><a href="">Login</a></li>
              <li><a href="">Get the first quote.</a></li>
              <li><a href="">Get all the quotes.</a></li>
              <li><a href="">Add a quote</a></li>
              <li><a href="">Get a random quote</a></li>
              <li><a href="">Get a title</a></li>
              <li><a href="">Get a Year</a></li>
              <li><a href="">Get all the years</a></li>
              <li><a href="">Get all the titles</a></li>
              <li><a href="">Get the current admin</a></li>
            </ul>
          </li>
          <li>
            <a href="">Back-end API</a>
            <ul>
              <li><a href="">Authorization</a></li>
              <li><a href="">Post token</a></li>
              <li><a href="">Post quote</a></li>
              <li><a href="">Get quote by id</a></li>
              <li><a href="">Put quote by id</a></li>
              <li><a href="">Delete quote by id</a></li>
              <li><a href="">Get a random quote</a></li>
              <li><a href="">Get title by id</a></li>
              <li><a href="">Delete title by id</a></li>
              <li><a href="">Get year by id</a></li>
              <li><a href="">Delete year by id</a></li>
              <li><a href="">Get all quotes</a></li>
              <li><a href="">Get all titles</a></li>
              <li><a href="">Get all years</a></li>
              <li><a href="">Get current Admin</a></li>
              <li><a href="">Create an admin</a></li>
              <li><a href="">Get admin by username</a></li>
              <li><a href="">Delete admin by username</a></li>
            </ul>
          </li>
          <li>
            <a href="">Postman requests</a>
            <ul>
              <li><a href="">Post token</a></li>
              <li><a href="">Post quote</a></li>
              <li><a href="">Get quote by id</a></li>
              <li><a href="">Put quote by id</a></li>
              <li><a href="">Delete quote by id</a></li>
              <li><a href="">Get a random quote</a></li>
              <li><a href="">Get title by id</a></li>
              <li><a href="">Delete title by id</a></li>
              <li><a href="">Get year by id</a></li>
              <li><a href="">Delete year by id</a></li>
              <li><a href="">Get all quotes</a></li>
              <li><a href="">Get all titles</a></li>
              <li><a href="">Get all years</a></li>
              <li><a href="">Get current Admin</a></li>
              <li><a href="">Create an admin</a></li>
              <li><a href="">Get admin by username</a></li>
              <li><a href="">Delete admin by username</a></li>
            </ul>
          </li>
      </li>
        </ul>
      </li>
    </ol>
</details>


## Gebouwd met :

[![FastAPI][FastAPI.py]][FastAPI-url]
[![Python][Python.py]][Python-url]
[![Html][Html.html]][Html-url]
[![AlpineJS][Alpine.js]][Alpine-url]
[![Javascript][Bootstrap.css]][Bootstrap-url]


## Over dit project

Ik voor dit project gekozen om bekende film quotes weer te geven aan de gebruiker. De reden dat ik hier voor het gekozen is eigenlijk heel simpel gezien ik nogal graag films kijk.

<!-- Front-end -->
### Front-end API

#### Login front-end

#### Get the first quote

#### Get all the quotes

#### Add a quote

#### Get a random quote

#### Get a title

#### get a year

#### Get all the years

#### Get all the titles

#### Get the current admin

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Back-end -->
### Back-end API

Hier kan je al de verschillende POST, GET, PUT en Delete endpoints zien dat ik heb.

![BackendDocks]

#### Authorize back-end
Sommige zaken in deze API kunnen enkel gedaan worden als je Admin bent, zoals het verwijderen van data uit de database. In de Back-end kan je inloggen door op de knop te drukken zoals hieronder.

![buttonAuthorizeBackEnd]

Vorvolgens moet je gewoon je username en password ingeven en ben je ingelogd.

![authorize-backend]

En dit is het resultaat als je op authorize klikt.

![AuthorizeResultBackEnd]

#### Post token back-end

Deze POST endpoint geeft een oAuth2 token terug van de API, Dize wordt op de achtergrond gebruikt om aan te geven of een request van een Admin is gekomen of niet.

![PostTokenBackEnd]

#### Post quote back-end
Om een Quote toe te voegen aan de database moet je gewoon zoals in de afbeelding hieronder de quote, de titel van de film en het jaartal van de film toevegen. Het mooien hier van is dat je niet 3 vershillende POST endpoints moet hebben gezien ook de IDs van zowel de titel als het jaartal automatisch worden toegevoegd.

![PostQuoteBackEnd1]

Als je dit hebt gedaan en dan nog op de knop Execute hebt gedrukt ziet je resultaat er zo uit.

![PostQuoteBackEnd2]

#### Get quote by id back-end

Deze GET endpoint geeft aan de hand van een ID de bijhorende quote weer, maar ook de IDs van het jaartal en de titel worden weergegeven.

![GetQuoteByIdBAckEnd]

#### Put quote by id back-end

Met deze PUT endpoint kan je een bepaalde quote aanpassen aan de hand van de bijhorende ID.

![PutQuoteByIdBackEnd]

#### Delete quote by id back-end

Met dit DELETE endpoint kan er een quote worden verwijderd aan de hand van de bijhorende ID.

![DeleteQuoteByIdBackEnd]

#### Get random quote back-end

Deze GET endpoint geeft een random quote terug uit de databse. Maar dit werkt niet.

![GetQuoteRandomBackEnd]

#### Get title by id back-end

Deze GET endpoint geeft aan de hand van een ID de bijhorende Title.

![GetTitleByIdBackEnd]

#### Delete title by id back-end

Deze DELETE endpoint verwijderd een title uit de database aan de hand van de bijhorende ID.

![DeleteTitleByBackEnd]

#### Get year by id back-end

Deze GET endpoint geeft aan de hand van een ID het bijhorende jaar.

![GetYearsByIdBackEnd]

#### Delete year by id back-end

Deze DELETE endpoint verwijderd een jaar uit de database aan de hand van de bijhorende ID.

![DeleteYearsByIdBackEnd]

#### Get all quotes back-end

Deze GET endpoint geeft alle quotes weer uit de database. Dit heeft in het verleden al gewerkt, maar op moment van indienen werkt het niet.

![GetAllQuotesBackEnd]

#### Get all titles back-end

Deze GET endpoint geeft alle titels weer uit de database. Dit heeft in het verleden al gewerkt, maar op moment van indienen werkt het niet.

![GetAllTitlesBackEnd]

#### Get all Years back-end

Deze GET endpoint geeft alle jaren weer uit de database. Dit heeft in het verleden al gewerkt, maar op moment van indienen werkt het niet.

![GetAllYearsBackEnd]

#### Get current admin back-end
Om te zien welke admin op dit moment is ingelogd moet je gewoon op execute drukken en krijg je als resultaat te zien welke admin op dit moment is ingelogd.

![GetAdminCurrentBackEnd]

#### Post admin back-end
Om een admin aan te maken moet je gewoon een username en password invullen en op execute drukken.

![CreateAdminBackEnd1]
![CreateAdminBackEnd2]

#### Get admin by username back-end
Om de id van een Admin op te vragen moet je gewoon zoals hier onder gewoon de username ingeven en krijg je als resultaat de id terug.

![GetAdminUsernameBackend]

#### Delete admin by username back-end

Deze DELETE endpoint verwijderd een admin acount aan de hand van de gebruikersnaam.

![DeleteAdminUsernamBackEnd]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Postman requests
Hier ga ik aan de hand van Postman requests toenen hoe de verschillende endpoints van de API werken.

#### Post token 

![PostTokenPostman]

#### Post quote 

![PostNewQuotePostman]

#### Get quote by id 

![PostGetQuoteByidPostman]

#### Put quote by id 

![PutQuotePostman]

#### Delete quote by id 

![DeleteQuotesPostman]

#### Get random quote 

![GetQuoteRandomPostman]

#### Get title by id 

![GetTitleByIdPostman]

Bij deze afbeelding zou ik nog even bij willen vermeleden dat de array "quotes" leeg is omdat we net bij "Delete quote by id" de bijhorende quote hebben verwijderd.

#### Delete title by id 

![DeleteTitleByIdPostman]

#### Get year by id 

![GetYearsByIdPostman]

#### Delete year by id 

![DeleteYearesByIdPostman]

#### Get all quotes 

![GetAllQuotesPostman]

#### Get all titles 

![GetAllTitlesPostman]

#### Get all Years 

![GetAllYearsPostman]

#### Get current admin 

![GetAdminPostman]

#### Post admin 

![PostAdminPostman]

#### Get admin by username 

![GetAdminUsernamePostman]

#### Delete admin by username

![DeleteAdminUsernamPostman]

[FastAPI.py]: https://img.shields.io/badge/-%F0%9F%97%B2%20FastAPI-019486?style=for-the-badge
[FastAPI-url]: https://fastapi.tiangolo.com/
[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Html.html]: https://img.shields.io/badge/HTML-E54C21?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://www.w3schools.com/html/
[Alpine.js]: https://img.shields.io/badge/Alpine.js-77C1D2?style=for-the-badge&logo=javascript&logoColor=white
[Alpine-url]: https://alpinejs.dev/
[Bootstrap.css]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/

<!-- -->

[backend-url]: https://system-service-rubenpinxten.cloud.okteto.net/docs
<!-- Authorize backend -->
[authorize-backend]: Pictures/Authorize_back_end.png
[buttonAuthorizeBackEnd]: Pictures/ButtonAuthorizeBackEnd.png
[AuthorizeResultBackEnd]: Pictures/AuthorizeResultBackEnd.png
<!-- Post Admin Backend -->
[CreateAdminBackEnd1]: Pictures/POST_Admin_Back_end_Deel_1.png
[CreateAdminBackEnd2]: Pictures/POST_Admin_Back_end_Deel_2.png
<!-- Get Admin Username Backend -->
[GetAdminUsernameBackend]: Pictures/GetAdminUsernameBackEnd.png
<!-- Get Current Admin Back-end -->
[GetAdminCurrentBackEnd]: Pictures/GetCurrentAdminBackEnd.png
<!-- Post quote Back-end -->
[PostQuoteBackEnd1]: Pictures/POST_Admin_Back_end_Deel_1.png
[PostQuoteBackEnd2]: Pictures/POST_Admin_Back_end_Deel_2.png

[GetYearsByIdBackEnd]: Pictures/GetYearsByIdBackEnd.png
[DeleteYearsByIdBackEnd]: Pictures/DeleteYearsByIdBackEnd.png
[GetAllQuotesBackEnd]: Pictures/GetAllQuotesBackEnd.png
[GetAllTitlesBackEnd]: Pictures/GetAllTitlesBackEnd.png
[GetAllYearsBackEnd]: Pictures/GetAllYearsBackEnd.png
[DeleteAdminUsernamBackEnd]: Pictures/DeleteAdminBackEnd.png
[BackendDocks]: Pictures/BackendDocks.png
[GetQuoteByIdBAckEnd]: Pictures/GetQuoteByIDBackEnd.png
[PutQuoteByIdBackEnd]: Pictures/PutQuoteByIDBackEnd.png
[DeleteQuoteByIdBackEnd]: Pictures/DeleteQuoteByIDBackEnd.png
[GetQuoteRandomBackEnd]: Pictures/GetQuoteRandomBackEnd.png
[GetTitleByIdBackEnd]: Pictures/GetTitleByIdBackEnd.png
[DeleteTitleByBackEnd]: Pictures/DeleteTitleByIdBackEnd.png
[GetYearsByIdBackEnd]: Pictures/GetYearsByIdBackEnd.png
[PostTokenBackEnd]: Pictures/PostTokenBackEnd.png


<!-- Postman Requests -->
[PostTokenPostman]: Pictures/PostTokenPostman.png
[PostNewQuotePostman]: Pictures/POSTNewQuote.png
[PostGetQuoteByidPostman]: Pictures/GetQuoteByIdPostman.png
[PutQuotePostman]: Pictures/PUTQuotePostman.png
[DeleteQuotesPostman]: Pictures/DeleteQuotesPostman.png
[GetQuoteRandomPostman]: Pictures/GetQuoteRandomPostman.png
[GetTitleByIdPostman]: Pictures/GetTitleByIdPostman.png
[DeleteTitleByIdPostman]: Pictures/DeleteTitleByIdPostman.png
[GetYearsByIdPostman]: Pictures/GetYearsByIdPostman.png
[DeleteYearesByIdPostman]: Pictures/DeleteYearsByIdPostman.png
[GetAllQuotesPostman]: Pictures/GetAllQuotesPostman.png
[GetAllTitlesPostman]: Pictures/GetAllTitlesPostman.png
[GetAllYearsPostman]: Pictures/GetAllYearsPostman.png
[GetAdminPostman]: Pictures/GetAdminPostman.png
[PostAdminPostman]: Pictures/PostAdminPostman.png
[GetAdminUsernamePostman]: Pictures/GetAdminUsernamePostman.png
[DeleteAdminUsernamPostman]: Pictures/DeleteAdminPostman.png

<!-- Front End -->

[LoginFrontEnd]: Pictures/LoginFrontEnd.png
[GetTheFirstQuoteFrontEnd]: Pictures/GetTheFirstQuoteFrontEnd.png
[GetAllTheQuotes]: Pictures/GetAllTheQuotesFrontEnd.png
[AddAQuoteFrontEnd]: Pictures/AddAQuoteFrontEnd.png
[GetARandomQuoteFrontEnd]: Pictures/GetARandomQuoteFrontENd.png
[GetATitleFrontEnd]: Pictures/GetAtitleFrontEnd.png
[GetAYearFrontEnd]: Pictures/GetAYearFrontEnd.png
[GetAllTheYearsFrontENd]: Pictures/GetAllTheYearsFrontEnd.pngµ
[GetAllTheTitlesFrontEnd]: Pictures/GetAllTheTitlesFrontEnd.png
[GetTheCurrentAdminFrontEnd]: Pictures/GetTheCurrentAdminFrontEnd.png
