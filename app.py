import streamlit as st

def arvioi_mPFS_mOS(deleetio: int):
    # Palauttaa (mPFS, mOS) kk vain jos deleetio ≥ 20 %, muuten (None, None)
    if deleetio >= 90:
        return 8.4, 31.2
    elif deleetio >= 80:
        return 13.8, 45.6
    elif deleetio >= 70:
        return 18.8, 38.1
    elif deleetio >= 60:
        return 21.0, 38.1
    elif deleetio >= 50:
        return 20.2, 32.5
    elif deleetio >= 40:
        return 21.0, 32.5
    elif deleetio >= 30:
        return 22.0, 38.1
    elif deleetio >= 20:
        return 23.9, 37.0
    else:
        return None, None

def arvioi_riski():
    st.title("Multippeli myelooman riskiluokitus (portaittain)")

    # 1) 17p-deleetio
    deleetio_17p = st.number_input(
        "Kuinka suuressa osassa soluja todetaan 17p-deleetio? (0–100 %)",
        min_value=0, max_value=100, step=1
    )

    korkea_riski = False

    # Ensisijainen portaan arviointi 17p-deleetiolla
    mPFS, mOS = arvioi_mPFS_mOS(deleetio_17p)
    if mPFS is not None:
        korkea_riski = True
        st.warning("Korkea riski: 17p-deleetio ≥ 20 %. Jos potilaalla on samanaikainen TP53 mutaatio, ennuste on estimaattia huonompi.")
        st.write(f"**Arvioitu mPFS:** {mPFS:.1f} kk")
        st.write(f"**Arvioitu mOS:** {mOS:.1f} kk")

    # 2) Muut kriteerit arvioidaan vain jos ei vielä korkea riski
    if not korkea_riski:
        tp53 = st.radio("Onko potilaalla TP53-mutaatio/deleetio?", ["Ei", "Kyllä"], horizontal=True)
        if tp53 == "Kyllä":
            korkea_riski = True
            st.warning(
            "Korkea riski: TP53-muutos\n\n"
            "Jos deleetio, mOS n. 75 kk ja jos mutaatio, mOS n. 54-60 kk)"
        )


    if not korkea_riski:
        t_1416 = st.radio("Onko potilaalla t(14;16)?", [
            "Ei tai ainoana muutoksena (harvinainen)",
            "Kyllä, yhdessä del(1p32) tai 1q+ kanssa"
        ])
        if t_1416.startswith("Kyllä"):
            korkea_riski = True
            st.warning("Korkea riski: t(14;16) + del(1p32) tai 1q+\n\n"
            "Jos WT tai ainoana muutoksena, mOS 92 kk, jos del(1p32) tai 1q+ kanssa, mOS 61 kk"
        )

    if not korkea_riski:
        t_4414 = st.radio("Onko potilaalla t(4;14)?", [
            "Ei tai ainoana muutoksena",
            "Kyllä, yhdessä del(1p32)/1q+ kanssa"
        ])
        if t_4414.startswith("Kyllä"):
            korkea_riski = True
            st.warning("Korkea riski: t(14;16) + del(1p32) tai 1q+\n\n"
            "Jos ainoana muutoksena, mOS ei saavutettu, jos del(1p32) tai 1q+ kanssa, mOS 70 kk"
        )
    if not korkea_riski:
        del_1p32_1q = st.radio(
            "Onko bialleelinen del(1p32) tai del(1p32) ja 1q+?",
            ["Ei", "Kyllä"], horizontal=True
        )
        if del_1p32_1q == "Kyllä":
            korkea_riski = True
            st.warning("Korkea riski: bialleelinen del(1p32) tai del(1p32) ja 1q+\n\n"
            "Jos bialleelinen del(1p32) tai del(1p32) ja 1q+, mOS 39 kk"
        )

    if not korkea_riski:
        b2m_krea = st.radio(
            "Onko B2M > 5,5 mg/dL ja samanaikaisesti normaali krea?",
            ["Ei", "Kyllä"], horizontal=True
        )
        if b2m_krea == "Kyllä":
            korkea_riski = True
            st.warning("Korkea riski: B2M/krea-yhdistelmä\n\n"
            "Jos B2M >5.5 mg/dL, ainoa muutos tai yhdessä korkean riskin geneettisten muutosten kanssa, mOS 63-75 kk"
        )

    # Lopputulos aina näkyviin
    st.markdown("---")
    if korkea_riski:
        st.success("➡️ Riskiluokka: **KORKEA**")
        # Jos haluat TP53-lisätiedot näkyviin lopputulososiossa:
        st.markdown(
            """
    **TP53-muutos**

    Deleetio, mOS n. 75 kk ja mutaatio, mOS n. 54–60 kk)
            """
        )
    else:
        st.info("➡️ Riskiluokka: **MATALA**")
        st.markdown(
            """
    - Jos 1q+ ainoana muutoksena, mOS 96 kk  
    - Jos monoalleelinen del(1p32), mOS 77 kk  
    - Jos ei mitään em., ennuste paras, eikä mOS ole 9 v seurannassa saavutettu.
            """
        )
    
if __name__ == "__main__":
    arvioi_riski()

