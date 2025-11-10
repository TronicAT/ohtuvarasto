from varasto import Varasto


def tulosta_getterit(varasto, nimi):
    print(f"{nimi} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def tulosta_setterit(varasto, nimi: str) -> None:
    print(f"{nimi} setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"{nimi}: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"{nimi}: {varasto}")


def testaa_virhe_varasto(parit):
    for tilavuus, alku_saldo in parit:
        var = Varasto(tilavuus, alku_saldo)
        print(f"Varasto({tilavuus}, {alku_saldo}): {var}")


def testaa_mehu(mehua):
    print("Mehu virhetilanteita:")
    virheelliset = [(-100.0, 0), (100.0, -50.7)]
    testaa_virhe_varasto(virheelliset)

    print(f"Mehuvarasto: {mehua}")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")
  

  

def testaa_olut(olutta):
    print("Olut virhetilanteita:")
    virheelliset = [(-100.0, 0), (100.0, -50.7)]
    testaa_virhe_varasto(virheelliset)

    print(f"Olutvarasto: {olutta}")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def luo_varasto(tilavuus, alku_saldo=0.0):
    return Varasto(tilavuus, alku_saldo)


def main():
    mehua = luo_varasto(100.0)
    olutta = luo_varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    tulosta_getterit(olutta, "Olut")
    tulosta_setterit(mehua, "Mehu")
    testaa_mehu(mehua)
    testaa_olut(olutta)


if __name__ == "__main__":
    main()
