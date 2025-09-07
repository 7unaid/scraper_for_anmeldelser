# En webscraper for å automatisere søket etter nye produkter
Dette Python-scriptet er utviklet for å automatisere prosessen med å innhente og analysere data fra en nettside, samt oppsummere salgsverdi og suksessjanse for videresalg, spesielt for å identifisere produkter som er verdt å dropshippe. I eksempelet over brukes en nøytral side hvor det vises amerikanske delstater med de beste vinne/tape-forholdene i en sportslig kontekst. Scriptet benytter flere moduler for å oppnå dette, inkludert requests for å hente nettsidens HTML-innhold, BeautifulSoup for å analysere HTML-strukturen og trekke ut nødvendig informasjon, samt pandas for å håndtere og manipulere dataene.

Først henter scriptet sideinnholdet fra en gitt webadresse, og bruker BeautifulSoup til å finne alle tabellrader som inneholder ønsket data. For hver rad utvinnes det delstatens navn, antall seire, og antall tap, og samler disse i en liste. Denne listen konverteres deretter til en såkalt dataframe for lettere kunne manipulere dataen.

Deretter grupperer scriptet dataene etter delstat, summerer antall seire og tap, og beregner et vinne/tape-forhold for hver delstat. Delstatene sorteres basert på dette forholdet for å identifisere hvilke som har de beste prestasjonene.

Etter å ha organisert dataene, forbereder scriptet en tekstbasert oppsummering av resultatene som sendes til OpenAI's GPT-modell for å få en vurdering av hvilke delstater som potensielt er verdt å investere i.

Til slutt opretter scriptet loggfil, slik at informasjonen kan gjennomgås senere. I tilfelle nettsidens struktur ikke samsvarer med forventningene, har scriptet innebygde kontroller for å unngå feil og gir tilbakemelding hvis ingen data blir funnet.
