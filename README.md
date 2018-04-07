# README
<!--
- zdobycie niezbędnej wiedzy redukuje zapotrzebowanie na nowe próbki
- nasycenie wiedzą można mierzyć przez RFSD
- HyperplaneSlow, SEASudden - widać, że odpowiedni dobór potrafi nawet przyspieszyć uczenie
- i to uzasadnia parametr budżetu, który pozornie wydawał się zbędny
- dla elecNormNew mamy nadal klasyfikator, który zachowuje się jak losowy
- zmniejszenie chunka działa pozytywnie przez zwiększenie częstotliwości uczenia (częstsze powtarzanie procesu uczenia)
-->

![](figures/RBFGradualRecurring.png)
![](figures/RBFNoDrift.png)
![](figures/RBFBlips.png)
![](figures/SEASuddenFaster.png)
![](figures/SEASudden.png)
![](figures/LEDNoDrift.png)
![](figures/LED.png)
![](figures/HyperplaneFaster.png)
![](figures/HyperplaneSlow.png)
![](figures/elecNormNew.png)
![](figures/covtypeNorm.png)
![](figures/poker-lsn.png)

<!--
Pozytywny wpływ na jakość klasyfikacji (a również na dynamikę krzywej uczenia) mają zarówno liczba neuronów w warstwie ukrytej (im więcej tym lepiej), jak i liczba próbek znajdujących się w pojedynczym chunku (im mniej tym lepiej).

Bujda: Zmniejszenie wielkości chunka wpływa też negatywnie na stabilność wyniku.
-->
