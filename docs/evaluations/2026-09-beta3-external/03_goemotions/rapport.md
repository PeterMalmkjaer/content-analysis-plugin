# Kvalitetsrapport 3 — GoEmotions

> **AI-skrevet rapport.** Denne rapport er skrevet af en AI-assistent som led i en ekstern evaluering den 9. september 2026. Den kan indeholde fejl, også fejl der ser overbevisende ud. Hovedtallene er efterregnet fra de kodede data den 13. november 2026; [README.md](../README.md) siger, hvad der er kontrolleret, og hvad der ikke er.
>
> **AI-written report.** Written by an AI assistant in an external evaluation on 9 September 2026. It may contain errors, including plausible-looking ones. The headline figures were recomputed from the coded data on 13 November 2026; see [README.md](../README.md) for what was and was not checked.

**Resultat: 43,6/100 i kodningsscore (micro-F1).** Testen omfatter alle **5.427 kommentarer i det officielle testsæt**, kodet mod 27 følelser og kategorien neutral. Scoren beskriver overensstemmelse med datasættets menneskelige annoteringer, ikke en universel procent for korrekt indholdsanalyse.

## Testens omfang og metode

Det komplette officielle `test.tsv` blev downloadet fra Google Research. Trænings- og valideringssættene blev ikke brugt. Alle kommentarer blev bevaret med deres oprindelige ID og fik et stabilt test-ID. Kommentarerne er korte, engelsksprogede Reddit-tekster; den omgivende samtale indgik ikke.

Tre adskilte kodekontekster behandlede hver 1.809 kommentarer med samme faste kodebog. Referenceetiketter og de andre koderes svar var skjult. De første 50 kommentarer i hver del fungerede som pilot uden ændring af kodebogen. Kodningen blev udført i batches med korte begrundelser. En kommentar kunne få flere følelser; neutral blev brugt alene. Definitionerne er operationelle parafraser af datasætartiklens Appendix A, ikke en fuldstændig kopi af den oprindelige træning af menneskelige annotatorer.

Hver kodekontekst gentog også 50 kommentarer fra en anden del, i alt 150 blindt genkodede kommentarer. Disse kommentarer lå i begyndelsen af delene; gentagelsesudvalget var ikke tilfældigt. Først efter afsluttet kodning blev svarene sammenlignet med referencen. De fastfrosne svar er dokumenteret med SHA-256 i scores.json.

## Målt kvalitet

| Mål | Resultat | Fortolkning |
|---|---:|---|
| Micro-F1 × 100, alle kategorier | **43,6** | Samlet balance mellem ekstra og manglende etiketter |
| Præcision | 43,0 % | Andel af AI-etiketterne, som også findes i referencen |
| Recall | 44,1 % | Andel af referenceetiketterne, som genfindes |
| Macro-F1 × 100 | 38,6 | Alle 28 kategorier vægter lige meget |
| Micro-F1 × 100, uden neutral | 41,1 | Sammenligning af de 27 følelseskategorier |
| Macro-F1 × 100, uden neutral | 38,1 | Hver følelse vægter lige meget |
| Helt identisk etiketsæt | 32,9 % | Alle og kun de samme etiketter på kommentaren |
| Dækning | **100 %** | 5.427 af 5.427 kommentarer |

Der var **2791 fælles**, **3694 AI-ekstra** og **3538 reference-ekstra** etiketter. En simpel sammenligning, som altid svarer neutral, giver 30,4 i micro-F1 og 29,6 % helt identiske etiketsæt. Det er en konstrueret basislinje, ikke en kontrolkørsel uden skillen.

Et illustrativt 95 %-bootstrapinterval for micro-F1 er **42,4–44,7**, beregnet med 1.000 genudtræk af kommentarer. Det forudsætter uafhængige kommentarer og omfatter ikke usikkerhed fra modelvalg, gentagne kørsler, ukendt træningseksponering eller afhængigheder mellem Reddit-kommentarer. Det er derfor ikke et samlet usikkerhedsinterval for værktøjets generelle kvalitet.

## Hvor er forbedringsbehovet størst?

De fem laveste F1-resultater blandt kategorier med mindst 20 referenceforekomster er:

| Kategori | Referenceforekomster | AI-forekomster | F1 × 100 |
|---|---:|---:|---:|
| disappointment | 151 | 128 | 19,4 |
| realization | 145 | 146 | 21,3 |
| embarrassment | 37 | 17 | 22,2 |
| disapproval | 267 | 1112 | 22,3 |
| annoyance | 320 | 207 | 23,5 |

En markant forskel er **disapproval**: AI’en bruger kategorien 1.112 gange mod referencens 267. Også caring anvendes oftere, 367 mod 135. De stærkeste kategorier er gratitude (F1 85,9), love (69,4) og amusement (60,5). Resultaterne varierer altså betydeligt mellem kategorierne.

Tabellen viser, hvor en faglig gennemgang og tydeligere grænseeksempler bør begynde. Få AI-forekomster i forhold til referencen peger på mulig underkodning; mange kan pege på for bred anvendelse. De enkelte uenigheder skal læses i deres tekst, før de erklæres fejl.

De sjældneste kategorier har et særligt spinkelt målegrundlag:

| Kategori | Referenceforekomster | F1 × 100 |
|---|---:|---:|
| grief | 6 | 28,6 |
| pride | 16 | 33,3 |
| relief | 11 | 25,6 |

En enkelt uenighed kan flytte disse kategoriers score mærkbart. Rapporten undlader derfor at bruge en god samlet score som dokumentation for sikker genkendelse af alle følelser.

## Gentagelighed og teknisk kvalitet

De 150 blindt genkodede kommentarer gav **85,1 i F1-overensstemmelse** og **76,0 % helt samme etiketsæt** mellem AI-kørslerne. Gennemsnitlig kappa pr. kategori var 0,762, med interval 0,000–1,000 blandt definerede værdier. Det måler konsistens mellem AI-kontekster, ikke menneskelig interkoderreliabilitet eller tidsmæssig drift. Det mindre og ikke-tilfældige gentagelsesudvalg kan ikke repræsentere alle kategoriers stabilitet.

Alle test-ID’er er dækket præcis én gang i den primære kodning, og alle etiketter er gyldige. Den komplette inputkommentar er tilknyttet hver kodetildeling automatisk via ID. Den ordrette evidens er derfor kontrollerbar **ved konstruktion**; dette tester ikke modellens evne til selv at udvælge eller gengive et citat.

**Validatorstatus: `RESULT: PASS`** for alle 6.485 kodetildelinger. Den fulde log findes i `validation.txt`. Den kontrollerer struktur, kildeoverensstemmelse og frekvenser. Den afgør ikke, om den valgte følelse er semantisk rigtig.

## Hvad dokumenterer testen?

Resultatet gælder **denne AI-kørsel med Content Analysis 5.0.0-beta.3** på korte engelske Reddit-kommentarer. Der er ikke kørt en parallel analyse uden skillen, så forbedringer kan ikke tilskrives skillen alene. Følelser kan være tvetydige, og menneskelige referenceetiketter er ikke et ufejlbarligt facit. Det officielle testsæt er filtreret efter annotatoroverensstemmelse og repræsenterer derfor ikke alle rå kommentarer eller alle former for uenighed.

**En forskel mellem protokol og reference:** 181 referencekommentarer kombinerer neutral med mindst én følelse, mens den faste AI-protokol krævede neutral alene. Det gør fuld etiketsætenighed umulig på disse 3,3 % af kommentarerne og påvirker også F1. Referencen og førstekodningen er bevaret uændret; resultatet uden neutral er derfor særlig relevant. Pilotens 50 kommentarer pr. kontekst var desuden mindre end skillens generelle 10 %-anbefaling, fordi denne test på forhånd fastlagde pilot og kodebog.

GoEmotions er et offentligt benchmark og kan have indgået i modellens træningsmateriale; det kan ikke kontrolleres her. Testen dokumenterer heller ikke kvalitet på dansk, lange interviews, nye domæner eller induktiv udvikling af temaer.

**Næste forbedring bør være at undersøge de svageste kategorier og deres grænser til beslægtede følelser og neutral.** Brug nye kommentarer med uafhængig menneskelig kodning til at afprøve ændringer. Bevar dette resultat som baseline, så forbedringer ikke blot afspejler tilpasning til kendte testsvar.

## Dokumentation

`audit_workbook.xlsx` samler kodninger, frekvenser, referenceforskelle, kategoriscores og gentagelseskontrol. `audit_bundle.zip` indeholder også de 5.427 separate kildefiler til genkørsel af validatoren. Originalt testsæt, kodebog, metodeprotokol, koderes noter og målinger ligger ved rapporten.

Datakilde: [Google Research — GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions). Metode og datasæt: [Demszky m.fl. (2020)](https://aclanthology.org/2020.acl-main.372/). Se SOURCE.md for kreditering og testens ændringer af dataformatet.
