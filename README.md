# RTU Sporta centra studentu nodarbību kalendāra pārnešana uz excel (projekta darbs dip225).
# 231RDB019 projekta darbs.

## Apraksts
Sports ir liela daļa no daudzu studentu ikdienas un RTU sporta centrs piedāvā plašu klāstu ar nodarbībām uz, kurām var pieteikties viņu interneta vietnē.
Bieži sanāk skatīties pa nodarbību kalendāru un meklēt laikus un brīvas vietas, kādi vēl ir pieejami.
Tas atvieglotu šo lēno uzdevumu, ja būtu visi dati par konkrētām sporta nodarbībām savākti pārskatāmi vienuviet.
## Projekta uzdevums
Projekta uzdevums ir izstrādāt Python programmatūru, kas ar tīmekļa skrāpēšanas palīdzību spētu automātiski no RTU sporta centra nodarbību kalendāra pieteikumu mājaslapas "https://www.rtu.lv/lv/sports/sporta-nodarbibas/pieteikties-nodarbibam" nolasīt - no paša lietotāja, pēc izvēles ievadīta notikuma - informāciju, kā datumu, laiku, adresi un pieteikušos dalībnieku skaitu visiem šī sporta notikumiem līdz nākamās nedēļas beigām (nākotnē tālāki notikumi kalendārā nebija vēl pievienoti). Tālāk šo visu informāciju apvienotu Excel tabulā, pārskatāmā veidā.
## Izmantotās bibliotēkas
![alt text](attēli/bib.png)
1. Selenium. Šī bibliotēka tika izmantota, lai varētu veikt automatizētu tīmekļa skrāpēšanu. Selenium webdriver ar selenium.webdriver.chrome.service ir vissvarīgākā daļa no bibliotēkas, kas atver un kontrolē interneta pārlūka "Google Chrome" logu, lai spētu veikt darbības tajā, kā nospiest pogas vai lai nolasītu informāciju no mājaslapas. Vēl tiek izmantota selenium.webdriver.common.by klase ar, kuras palīdzību tiek meklēti elementi HTML mājaslapas kodā. Visbeidzot selenium.common.exceptions klase ļauj tikt galā ar izņēmumiem, kas rodas, gadījumā, ja meklētais elements mājaslapā netiek atrasts.
2. Datetime. Datetime bibliotēka ir domāta izmantošanai ar datumiem un laikiem. Manā gadījuma tika izmantota nolūkam, lai iegūtu pašreizējā datuma mēneša un dienas skaitļus, kas veido daļu no mājaslapas URL.
3. Time. Bibliotēka tika lietota sleep() funkcijas dēļ, kas veic noteikta garuma pauzi, kurā netiek nekas darīts, lai Selenium webdriver būtu pietiekams laiks, lai pilnībā ielādētu mājaslapu un programma varētu veikt nākamo funkcionalitāti.
4. Pandas. Pandas ir plaši izmantota datu apstrādes Python bibliotēka. Projektā to izmantoja, lai ievākto informāciju par individuālo nodarbību, kura tika glabāta, kā vārdnīca pārveidotu par "DataFrame" ar DataFrame.from_dict() funkciju, kas ir līdzīga tabulai, kuras tika vēlāk apvienotas. Tad vēl bija izmantota to_excel() funkcija mērķim, lai radītu Excel datni no apvienotajām tabulām.
## Programmatūras izmantošanas metodes un lietošana
Programmas sākumā tiek iegūts šobrīdējā diena un mēnesis, kas tiek likts mājaslapas saites mainīgajā, lai iegūtu pareizo mājaslapas vietu. Tālāk ir sekojošās funkcijas:
1. Funkcija. lietotaja_ievade(). Funkcija prasa lietotājam ievadīt vēlamo sporta nodarbības nosaukumu, kuru meklēs sporta centra kalendārā programma (piemēros var redzēt excel failu rezultātus pēc ievades - "Volejbols" un "Basketbols") , atkārtoti, kamēr lietotājs būs ievadījis ne tukšu un atgriež to kā mainīgo.
2. Funkcija. saites(sports, url). sports - lietotāja ievadītā vērtība 1. funkcijā un url - mājaslapas url no programmas sākuma. Sākotnēji atver pārlūkā mājaslapu, noraida sīkfailus un nodzēš ziņojumu no ekrāna. Tālāk tā meklē cauri elementu tekstiem mājaslapā, vai tie atbilst lietotāja ievadītajam, ja jā tad saglabā saiti uz nodarbības lapu sarakstā, kā arī aiziet uz nākamās nedēļas kalendāra skatu, tur meklējot arī. Pēc cikla pabeigšanas funkcija atgriež sarakstu ar atbilstošajām nodarbību mājaslapām.
3. Funkcija. iegust_tabulas(linki). linki - saraksts ar nodarbību mājaslapām. Iet cauri un atver katru mājaslapu, nolasot informāciju no mājaslapas tabulas, sadalot un pārveidojot par vārdnīcu, tad par "DataFrame", kuras saglabā sarakstā, kā arī pārbauda vai nodarbības datums ir no šodienas vai vēlāk un vai nodarbība nav atcelta. Funkcija atgriež sarakstu ar tabulām beigās.
4. Funkcija. excel_datne(tabulas, sports). tabulas - saraksts ar tabulām no iepriekšējās funkcijas un sports - lietotāja ievadītais. Funkcija pārbauda vai saraksts nav tukšs (izvada kļūmes paziņojumu ja ir), tad apvieno visas tabulas, pārveido vajadzīgo kolonnu vērtības, indeksē pareizi. Visbeidzot, apvienotā tabula tiek eksportēta uz exceli, kas ir gala rezultāts.




