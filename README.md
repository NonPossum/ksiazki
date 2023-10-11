Narzędzie służącym do sprawdzania dostępności i lokalizowania książek na różnych stronach internetowych. Umożliwia wyszukiwanie książek na podstawie zadanych kryteriów i wyświetla wyniki w konsoli.

## Wymagania

- Python 3.x
- Moduł `colorama` (zainstalowany za pomocą `pip install colorama`)

## Instrukcja Użycia

1. Upewnij się, że masz zainstalowanego Pythona 3.x oraz moduł `colorama`.

2. W pliku `ksiazki.json` zdefiniuj książki, które chcesz sprawdzić. Struktura pliku powinna być w formacie JSON i zawierać nazwy książek jako klucze i liste słów kluczowych, które opisują książki.

   Przykład pliku `ksiazki.json`:
   ```json
   {
       "1": "Nazywanie a konieczność",
       "2": "Logika religii Józef Maria"
       // Dodaj kolejne książki
   }
   ```

Planowane Rozbudowy:
Rozszerzenie programu o obsługę kolejnych stron.
Dodanie dodatkowych opcji filtrowania i sortowania wyników.
Ulepszanie interfejsu użytkownika i wizualizacji wyników.
