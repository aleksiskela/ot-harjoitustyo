classDiagram
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "2" Noppa
    Monopoli "1" -- "2...8" Pelaaja
    Monopoli "1" -- "1" Aloitusruutu
    Monopoli "1" -- "1" Vankila
    Pelaaja "1" -- "1" Pelinappula
    Pelaaja "0...1" -- "0...*" Katu
    Pelilauta "1" *-- "40" Ruutu
    Pelinappula "0...8" -- "1" Ruutu
    Ruutu "1" <|-- "1" Aloitusruutu
    Ruutu "1" <|-- "1" Vankila
    Ruutu "1" <|-- "*" Katu
    Ruutu "1" <|-- "*" Sattuma
    Ruutu "1" <|-- "*" Yhteismaa
    Ruutu "1" <|-- "*" Asema
    Ruutu "1" <|-- "*" Laitos
    Katu "1" -- "0...4" Talo
    Katu "1" -- "0...1" Hotelli
    class Pelaaja{
        rahaa
    }
    class Ruutu{
        seuraavaRuutu()
    }
    class Aloitusruutu{
        toiminto()
    }
    class Vankila{
        toiminto()
    }
    class Sattuma{
        toiminto()
    }
    class Yhteismaa{
        toiminto()
    }
    class Katu{
        nimi
        toiminto()
    }
    class Asema{
        toiminto()
    }
    class Laitos{
        toiminto()
    }