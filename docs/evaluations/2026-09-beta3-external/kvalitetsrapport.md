# Samlet kvalitetsrapport — Content Analysis 5.0.0-beta.3

> **AI-skrevet rapport.** Denne rapport er skrevet af en AI-assistent som led i en ekstern evaluering den 9. september 2026. Den kan indeholde fejl, også fejl der ser overbevisende ud. Hovedtallene er efterregnet fra de kodede data den 13. november 2026; [README.md](README.md) siger, hvad der er kontrolleret, og hvad der ikke er.
>
> **AI-written report.** Written by an AI assistant in an external evaluation on 9 September 2026. It may contain errors, including plausible-looking ones. The headline figures were recomputed from the coded data on 13 November 2026; see [README.md](README.md) for what was and was not checked.

De tre aftalte testforløb er gennemført. **Værktøjet giver efterprøvelige kodninger, men den faglige kodning kræver fortsat menneskelig kontrol.** Resultaterne nedenfor måler hver deres afgrænsede opgave. De dokumenterer ikke kvaliteten af alle værktøjets funktioner.

| Test | Faktisk kodet materiale | Reference | F1-score, 0–100 |
|---|---|---|---:|
| TU Delft-interviews | Alle 7 interviews, 262 tekstenheder | Publicerede forskerkodninger | **60,1** |
| TU Delft / AC-ICT | Hele forfatternes testsæt: 6 rapporter, 184 uddrag, 5 felter | Publiceret AI-analyse med forskerevaluering | **63,1** |
| GoEmotions | Hele det officielle testsæt: 5.427 kommentarer | Menneskelige følelsesannoteringer | **43,6** |

**F1 er en balance mellem ekstra og manglende koder.** Tallet er ikke en procent for, hvor meget af analysen der er objektivt sandt. Især AC-ICT-tallet er overensstemmelse med et andet AI-forløb. Der beregnes derfor ingen samlet gennemsnitlig kvalitetsprocent.

Alle tre datapakker er downloadet. For AC-ICT blev alle 155 PDF’er kontrolleret for åbning og tekstudtræk; den faglige kodningstest omfatter de seks rapporter i det leverede testsæt. Den er ikke en fuld gentagelse af alle oprindelige analysetrin på 155 rapporter. GoEmotions-testen bruger alle testkommentarer, men ingen trænings- eller valideringsdata.

## Styrker

- Alle enheder i de erklærede testsæt blev behandlet, og de endelige tabeller bestod den tekniske validator.
- Kodninger, evidens, frekvenser og uenigheder er gemt, så resultaterne kan gennemgås.
- Separate, blinde kodninger gør det muligt at vurdere konsistens uden at vise koderen referenceetiketterne.

Teknisk validering viser, at data kan kontrolleres. Den beviser ikke, at fortolkningerne er korrekte. I GoEmotions blev hele inputkommentaren tilknyttet automatisk som evidens; dette er ikke en test af modellens citatudvælgelse.

## De vigtigste forbedringer

1. **Skærp kodegrænserne.** Interviewtesten viser problemer med brede erfaringskoder over for konkrete støtte- og infrastrukturelementer. Governance-testen viser især uenighed om, hvornår en anbefaling overhovedet er governance-relevant.
2. **Kontrollér oversete koder og fuld enighed.** En god teknisk rapport og høj konsistens på nogle koder kan skjule manglende temaer eller forskellige komplette kodesæt.
3. **Afprøv rettelser på nye, menneskekodede data.** Denne benchmark bør bevares som baseline. Der er ikke foretaget en efterfølgende tilpasning af den faglige kodning til testsvarene.

Resultaterne gælder denne AI+skill-kørsel. Der er ingen kontrolkørsel uden skillen, og offentlige datasæt kan have været set under modellens træning. Interviewresultatet varierer desuden fra 53,0 til 60,1 afhængigt af, hvordan forskernes kodede passager knyttes til testens tekstenheder; detaljerne står i rapport 1.

## Rapporter og dokumentation

- [Rapport 1: TU Delft-interviews](01_delft_interviews/rapport.md) · Regneark (ikke med i dette repository)
- [Rapport 2: TU Delft / AC-ICT](02_delft_reports/rapport.md) · Regneark (ikke med i dette repository)
- [Rapport 3: GoEmotions](03_goemotions/rapport.md) · Regneark (ikke med i dette repository) · Komplet kontrolpakke (ikke med i dette repository)

Hver rapport angiver datakilde, målemetode, begrænsninger og konkrete forbedringspunkter. Målinger og kildeoplysninger er gemt sammen med rapporterne. Testdato: 9. september 2026.
