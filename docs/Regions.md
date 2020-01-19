# Regions

## Territories

The nomenclature of territorial units for statistics (NUTS) classifies territorial units in Europe in different levels:

* NUTS 0: country-level
* NUTS 1: major socio-economic regions
* NUTS 2: basic regions for the application of regional policies
* NUTS 3: small regions for specific diagnoses

## Bidding zones

A bidding zone is the largest geographical area within which market participants are able to exchange energy without capacity allocation. There are three types of bidding zones:

1. national borders (e.g., France or the Netherlands) - majority of bidding zones in Europe
2. larger than national borders (e.g., Germany and Luxembourg or the Single Electricity Market for the island of Ireland)
3. smaller zones within individual countries (e.g., Italy, Norway or Sweden)

The bidding zones in European electricity markets and surrounding regions are illustrated in the map below.

![](images/market-map-entsoe.png)

*Bidding zones in Europe. This map is created using the base map with bidding zone borders from ENTSO-E Transparency Platform's cross-border physical flow map as a guide.*

The table below below lists bidding zones in Europe by country and market operator.

*Bidding zones and market operators in Europe.*

**Country** | **Markets** | **Zones**
--- | --- | ---
Belgium (BE) | Belpex | BE
Germany (DE) | EEX, EPEX | DE-LU
Denmark (DK) | EEX, Nord Pool | DK1, DK2
France (FR) | EEX, EPEX | FR
Netherlands (NL) | APX | NL
Norway (NO) | EEX, Nord Pool | NO1, NO2, NO3, NO4, NO5
Sweden (SE) | EEX, Nord Pool | SE1, SE2, SE3, SE4
United Kingdom (UK) | APX, N2EX | GB, IE-SEM

The United Kingdom is comprised of Great Britain (GB) and Northern Ireland. Northern Ireland is part of the Single Electricity Market of the island of Ireland (IE-SEM), which it shares with the Republic of Ireland (IE). Prior to 01/10/2018, Germany was part of the DE-AT-LU bidding zone, together with Austria (AT) and Luxembourg (LU), which had split into the DE-LU and AT bidding zones, as reported by European Network of Transmission Systems Operators for Electricity (ENTSO-E) below:

>*[...] DE-AT-LU bidding zone split on the 23rd of August. BZN|DE-AT-LU will be separated into 2 new bidding zones BZN|DE-LU and BZN|AT.*
>
>*New bidding zones will be active from the 1st of October, however, first data submissions, like month ahead forecasts, are expected from the 1st of September.*
>
>*Validity end date for BZN|DE-AT-LU is the end of September 2018. [...]*

Mapping bidding zones to NUTS 3 territories is straightforward for Belgium, Germany, France and Netherlands (bidding zone type 1 or 2) -- all NUTS 3 territories in these countries have the same bidding zone.

Denmark and United Kingdom are both conveniently separated into two zones that are easily distinguishable. For Denmark, these are Western Denmark (NUTS IDs containing DK03-DK05) and Southern Denmark (NUTS IDs containing DK01-DK02). For United Kingdom, these are Great Britain (NUTS IDs containing UKC-UKM) and Northern Ireland (NUTS IDs containing UKN).

There is no clear indication of the bidding zone boundaries for Norway and Sweden, so some assumptions were made. Both countries have multiple smaller bidding zones (type 3) with flexible borders . This was done to optimise allocation of resources and reduce the overall price of electricity. Norway has five zones and Sweden has four zones. By cross-referencing Nord Pool market data, NUTS 3 data and county maps of Norway and Sweden, the territories are split into the bidding zones as shown in the table below. Nord Pool associates each bidding zone with a major reference city in that zone. However, there were six cities for Norway instead of the expected five. Historical Nord Pool market data for Norway suggests that two cities, Trondheim and Molde, have had the same system price since 2003. The ELSPOT area change log also confirms that Trondheim and Molde are city references for the NO3 bidding zone . Therefore, these two cities are grouped into the same bidding zone, which also satisfies what the maps suggest.

*Bidding zones and their territories for Norway and Sweden, approximated based on Nord Pool market data, NUTS 3 data and county maps of Norway and Sweden.*

**Bidding zone** | **Reference cities** | **Counties** | **NUTS 3 IDs**
-- | -- | ------ | ---
NO1 | Oslo | Oslo, Akershus, Hedmark, Oppland, Østfold, Buskerud, Vestfold, Telemark | NO011-034
NO2 | Kristiansand | Aust-Agder, Vest-Agder, Rogaland | NO041-043
NO3 | Trondheim, Molde | Sogn og Fjordane, Møre og Romsdal, Trøndelag | NO052-060
NO4 | Tromsø | Nordland, Troms, Finnmark | NO071-073
NO5 | Bergen | Hordaland | NO051
SE1 | Luleå | Norrbotten | SE332
SE2 | Sundsvall | Gävleborg, Västernorrland, Jämtland, Västerbotten | SE313-331
SE3 | Stockholm | Stockholm, Uppsala, Södermanland, Östergötland, Örebro, Västmanland, Jönköping, Gotland, Västra Götaland, Värmland, Dalarna | SE110-211, SE214, SE232-312
SE4 | Malmö | Kronoberg, Kalmar, Blekinge, Halland, Skåne | SE212-213, SE221-231

## Transmission system operators and interconnections

Europe has multiple TSOs and cross-border interconnections. These are listed, along with the bidding zones, in the table below.

*TSOs and cross-border interconnections in Europe. Data: European Network of Transmission System Operators for Electricity.*

**Country**<sup>[^4]</sup> | **TSOs** | **Cross-border interconnections** | **Bidding zones**
-|-----|---|---
BE | Elia System Operator | FR, LU, NL, UK | BE
DK | Energinet | DE, NO, SE | DK1, DK2
DE | TransnetBW, TenneT TSO, Amprion, 50Hertz Transmission | AT, CH, CZ, DK, FR, LU, NL, PL, SE | DE-LU
FR | Réseau de Transport d'Electricité | BE, CH, DE, ES, IT, UK | FR
NL | TenneT TSO | BE, DE, NO, UK | NL
NO | Statnett | DK, FI, NL, SE | NO1, NO2, NO3, NO4, NO5
SE | Svenska Kraftnät | DK, FI, DE, LT, NO, PL | SE1, SE2, SE3, SE4
UK | National Grid Electricity Transmission, System Operator for Northern Ireland, Scottish Hydro Electric Transmission, ScottishPower Transmission | BE, FR, IE, NL | GB, IE-SEM

[^4]: *CH - Switzerland; CZ - Czech Republic; ES - Spain; FI - Finland; IT - Italy; LT - Lithuania; PL - Poland; SK - Slovakia.*

## References

1. "[NUTS - Nomenclature of territorial units for statistics - Eurostat](https://ec.europa.eu/eurostat/web/nuts/background)."
2. "[Bidding Zones Literature Review](https://www.ofgem.gov.uk/sites/default/files/docs/2014/10/fta_bidding_zone_configuration_literature_review_1.pdf)," Ofgem, July 2014.
3. "[Data view - Cross-Border Physical Flow - ENTSO-E Transparency Platform](https://transparency.entsoe.eu/transmission-domain/physicalFlow/show?name=&defaultValue=true&viewType=MAP&areaType=BORDER_BZN)."
4. "[Power | Statkraft](https://www.statkraft.com/market-operations/standard-energy-products/power-electricity/)."
5. "[See market data for all areas | Nord Pool](http://www.nordpoolspot.com/Market-data1/)."
6. "[EPEX SPOT SE: About EPEX SPOT](http://www.epexspot.com/en/companyinfo/about_epex_spot)."
7. "[DE-AT-LU Bidding zone split - News - ENTSO-E Transparency Platform](https://transparency.entsoe.eu/news/widget?id=5b7c1e9b5092e75a10bab903)."
8. "[European Commission - PRESS RELEASES - Press release - Antitrust: Commission increaseselectricity trading capacity on the Swedish borders](http://europa.eu/rapid/press-release_IP-10-425_en.htm?locale=en)," 14 April 2010.
9. "[List of changes in day-ahead and intraday areas](https://www.nordpoolspot.com/globalassets/download-center/day-ahead/elspot-area-change-log.pdf)," Nord Pool.
10. "[Counties of Norway](https://en.wikipedia.org/w/index.php?title=Counties_of_Norway&oldid=890663009)," Wikipedia. 2 April 2019.
11. "[Counties of Sweden](https://en.wikipedia.org/w/index.php?title=Counties_of_Sweden&oldid=882806371)," Wikipedia. 11 February 2019.
12. "[ENTSO-E Transparency Platform](https://transparency.entsoe.eu/)."
13. "[Regional Security Coordinators FAQ](https://www.entsoe.eu/major-projects/rscis/)."
14. "[Overview of European Electricity Markets](https://ec.europa.eu/energy/sites/ener/files/documents/overview_of_european_electricity_markets.pdf)," European Union, Brussels, Belgium, February 2016.