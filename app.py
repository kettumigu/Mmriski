def arvioi_riski():
    print("Multippeli myelooman riskiluokitus (portaittain)")

    # Geneettinen riski arvioidaan portaittain
    try:
        deleetio_17p = int(input("Kuinka suuressa osassa soluja todetaan 17p deleetio? (0-100): "))
    except ValueError:
        print("Virheellinen syöte. Anna numero välillä 0-100.")
        return

    if deleetio_17p >= 20:
        print("
➡️ Riskiluokka: KORKEA (17p deleetio ≥ 20%)")
        return

    tp53 = input("Onko potilaalla TP53-mutaatio/deleetio? (kyllä/ei): ").strip().lower()
    if tp53 == "kyllä":
        print("
➡️ Riskiluokka: KORKEA (TP53-muutos)")
        return

    t_1416 = input("Onko potilaalla t(14;16)? (1 = Ei tai ainoana muutoksena, 2 = Kyllä del(1p32)/1q+ kanssa): ").strip()
    if t_1416 == "2":
        print("
➡️ Riskiluokka: KORKEA (t(14;16) + del(1p32)/1q+)")
        return

    t_4414 = input("Onko potilaalla t(4;14)? (1 = Ei tai ainoana muutoksena, 2 = Kyllä del(1p32)/1q+ kanssa): ").strip()
    if t_4414 == "2":
        print("
➡️ Riskiluokka: KORKEA (t(4;14) + del(1p32)/1q+)")
        return

    del_1p32_1q = input("Onko bialleelinen del(1p32) tai del(1p32) ja 1q+? (1 = Ei, 2 = Kyllä): ").strip()
    if del_1p32_1q == "2":
        print("
➡️ Riskiluokka: KORKEA (bialleelinen del(1p32) tai del(1p32) ja 1q+)")
        return

    # Jos mikään geneettinen ei osoita korkeaa riskiä, kysytään B2M/krea
    b2m_krea = input("Onko B2M >5,5 mg/dL ja samanaikaisesti normaali krea? (1 = Ei, 2 = Kyllä): ").strip()
    if b2m_krea == "2":
        print("
➡️ Riskiluokka: KORKEA (B2M/krea-yhdistelmä)")
    else:
        print("
➡️ Riskiluokka: MATALA")

if __name__ == "__main__":
    arvioi_riski()

