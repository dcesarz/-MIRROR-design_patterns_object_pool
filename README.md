# Wzorce: Pule obliczeń

| Termin oddania | Punkty     |
|----------------|:-----------|
| 25.04.2021 23:00|  10       |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:

- punkty uzyskania za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
Utworzyć trzy pule obiektów reprezentujących trzy rodzaje konfigurowalnych i skomplikowanych obliczeń podstawowych.
Obiekty te zawierają stan reprezentujący zarówno stan konfiguracji, jak i obliczeń.

- każda pula powinna umożliwiać współbieżne korzystanie ze swoich zasobów przez wiele współbieżnych wątków
  obliczających (podobnie jak w przykładzie z wykładu)
- każda pula powinna się automatycznie powiększać tak, by zoptymalizować zarówno czas oczekiwania na dostępność obiektów
  w puli, jak i minimalizować liczbę obiektów w puli; nowe obiekty w puli powinny być wytwarzane przy wykorzystaniu
  wzorca prototyp
- każdy wątek obliczający jest tworzony z wykorzystaniem wzorca builder i ustalamy w nim ile i jakich obiektów
  reprezentujących obliczenia musi pobrać z puli i jak je skonfigurować
- po skompletowaniu wszystkich niezbędnych obiektów z puli wątek wykonuje obliczenia, po czym zwraca obiekty do puli i
  się kończy.

Zbadać optymalność algorytmu zarządzania elementami puli oraz zależność liczby wątków obliczających ich złożoności
obliczeniowej i liczby niezbędnych obiektów w pulach.

Do zaproponowanych rozwiązań załączyć odpowiednie testy wydajnościowe / funkcjonalne. Można używać narzędzi do
profilowania kodu dedykowanych danej technologii. 
